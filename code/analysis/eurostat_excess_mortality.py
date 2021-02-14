from os import path
from typing import List, Tuple, Union

import pandas as pd
import numpy as np

from code.folder_constants import eurostat_combined_files, output_eurostat_excel
from code.scraping_constants import *


def clean_up_raw_eurostat_files(df: pd.DataFrame, reduce_columns: List,
                                remove_countries_regions: List, rename_value_field:str):
    '''

    :param df:
    :param reduce_columns:
    :param remove_countries_regions:
    :param rename_value_field:
    :return:
    '''
    df[['YEAR', 'WEEK']] = df['TIME'].str.split('W', expand=True)
    df = df[reduce_columns]

    if remove_countries_regions:
        df = df[~df['GEO'].isin(remove_countries_regions)]

    df.rename(columns={'Value': rename_value_field}, inplace=True)
    df = df[~df[rename_value_field].str.contains(":")]
    df[rename_value_field] = df[rename_value_field].str.replace(',', '').astype(int)

    return df


def merge_eurostat_files(prev_year_files: List[str], cur_year: str, file_name: str,
                         exclude_countries_regions: Union[None, List] = None, incl_week: bool = False):
    '''

    :param prev_year_files:
    :param cur_year:
    :param file_name:
    :param exclude_countries_regions:
    :param incl_week:
    :return:
    '''

    bindings = EUROSTAT_COMBINE_FILES_BY_WEEK if incl_week else EUROSTAT_COMBINE_FILES_TOTAL

    prev_year_dfs = [pd.read_csv(file, converters={'Value': str}, encoding='utf-8-sig') for file in prev_year_files]
    avg_prev_years = pd.concat(prev_year_dfs)
    current_year = pd.read_csv(cur_year, converters={'Value': str}, encoding='utf-8-sig')

    avg_prev_years = clean_up_raw_eurostat_files(avg_prev_years, bindings['reduce_columns'],
                                                 exclude_countries_regions, 'average_mortality')
    current_year = clean_up_raw_eurostat_files(current_year, bindings['reduce_columns'],
                                               exclude_countries_regions, 'mortality_current_year')

    avg_prev_years = avg_prev_years.groupby(bindings['avg_per_year_group']).sum('average_mortality').groupby(
        bindings['group_by']).mean()
    current_year = current_year.groupby(bindings['group_by']).sum('mortality_current_year')
    combined = avg_prev_years.merge(current_year, how='inner', on=bindings['group_by'])

    combined['Excess_mortality'] = combined.apply(lambda x: x['mortality_current_year'] - x['average_mortality'], axis=1)
    combined['P_score'] = combined.apply(lambda x: round((x['Excess_mortality'] / x['average_mortality']) * 100, 2)
                                         if x['average_mortality'] != 0 else 0, axis=1)

    combined = combined.reset_index().replace({"AGE": EUROSTAT_AGES_CONVERSION})

    directory = output_eurostat_excel
    file_name = f'{bindings["by"]}' + file_name
    file_path = path.join(directory, file_name)
    combined.to_csv(file_path, index=False, encoding='utf-8-sig')

    return file_path


def calc_mort_by_cntry_gndr_and_age_groups(file_path: str, countries_regions: List, ages: List,
                                           return_file_name: str, gender: Tuple = ('Females', 'Males', 'Total')):
    '''

    :param file_path:
    :param countries_regions:
    :param ages:
    :param return_file_name:
    :param gender:
    :return:
    '''

    df = pd.read_csv(file_path, encoding='utf-8-sig')
    df = df[(df['AGE'].isin(ages)) & (df['GEO'].isin(countries_regions)) & (df['SEX'].isin(gender))]
    df = df.groupby(['GEO', 'SEX']).sum(['average_mortality', 'mortality_current_year', 'Excess_mortality'])
    df['P_score'] = df.apply(lambda x: round((x['Excess_mortality'] / x['average_mortality']) * 100, 2), axis=1)

    directory = output_eurostat_excel
    file_name = return_file_name
    file_path = path.join(directory, file_name)
    df.reset_index().to_csv(file_path, index=False, encoding='utf-8-sig')


def calc_average_excess_mortality_age(file: str, locale: List, return_file_name, week_start: int = 10, week_end: int = 53):
    '''

    :param file:
    :param locale:
    :param return_file_name:
    :param week_start:
    :param week_end:
    :return:
    '''

    df = pd.read_csv(file, encoding='utf-8-sig')

    # Filter by func params and group by locale, sex and age. Then filter on positive excess mortality
    df = df[(df['GEO'].isin(locale)) & (df['WEEK'] >= week_start) & (df['WEEK'] <= week_end)]
    df = df.groupby(['GEO','SEX', 'AGE']).sum(['average_mortality', 'mortality_current_year', 'Excess_mortality'])
    df = df[df['Excess_mortality'] > 0]

    df = df.reset_index()
    df = df[['GEO', 'SEX', 'AGE', 'Excess_mortality']]
    df['AVG'] = df.apply(lambda x: x['Excess_mortality'] * EUROSTAT_AGES_AVERAGES[x['AGE']], axis=1)
    df = df.groupby(['GEO', 'SEX']).sum(['Excess_mortality', 'AVG'])

    df['AVG_TOTAL'] = df.apply(lambda x: x['AVG'] / x['Excess_mortality'], axis=1).round(2)

    directory = output_eurostat_excel
    file_name = return_file_name
    file_path = path.join(directory, file_name)
    df.reset_index().to_csv(file_path, index=False, encoding='utf-8-sig')

    return file_path


def calc_bg_pct_mortality_pct_population(population_df: pd.DataFrame, excess_mort_df: str, return_file_name: str):
    '''

    :param population_df:
    :param excess_mort_df:
    :param return_file_name:
    :return:
    '''
    excess_mort_df = pd.read_csv(excess_mort_df, encoding='utf-8-sig')

    excess_mort_df = excess_mort_df[['GEO', 'SEX', 'Excess_mortality']]
    total_excess_mortality_men = sum(excess_mort_df[excess_mort_df['SEX'] == 'Males']['Excess_mortality'])
    total_excess_mortality_women = sum(excess_mort_df[excess_mort_df['SEX'] == 'Females']['Excess_mortality'])

    excess_mort_df = excess_mort_df.groupby(['GEO', 'SEX']).sum('Excess_mortality').unstack(level=-1)
    values = excess_mort_df.columns.to_flat_index()
    values = [f'{val[0]}_{val[1]}' for val in values]
    excess_mort_df.columns = values

    excess_mort_df['Pct_Exc_Mort_MALES'] = excess_mort_df.apply(
        lambda x: (x['Excess_mortality_Males'] / total_excess_mortality_men) * 100, axis=1).round(2)
    excess_mort_df['Pct_Exc_Mort_FEMALES'] = excess_mort_df.apply(
        lambda x: (x['Excess_mortality_Females'] / total_excess_mortality_women) * 100, axis=1).round(2)

    combined = excess_mort_df.reset_index().merge(population_df, how='inner', left_on='GEO', right_on='pop_Municipalities')
    combined.drop('pop_Municipalities', axis=1, inplace=True)

    directory = output_eurostat_excel
    file_name = return_file_name
    file_path = path.join(directory, file_name)
    combined.reset_index().to_csv(file_path, index=False, encoding='utf-8-sig')

    return file_path