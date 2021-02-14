from os import path
from typing import Dict, List, Union

import requests
import pandas as pd

from code.folder_constants import source_pyll_le


def get_life_expectancy_cl(filename: str, url_dict: Dict, page_file: str, pf_name: str,
                           columns: List, rename_columns: List, start_index: List,
                           end_index: Union[List, None] = None, sheet_name: Union[str, None] = None) -> str:
    '''
    Country Level (cl) function - function makes a request to a given statistics institution's web page.
    It downloads a file containing the institution's life expectancy for their countries_regions.
    :param filename: the file naming convention for the resulting file
    :param url_dict: The URL structure of the given statistics institution's page
    :param page_file: (pages | files) <-- within the URL structure of the statistic institution's page
    :param pf_name: The page or file name
    :param columns: The column names of the
    :param rename_columns: Name of the new column headers (used to standardize the header language to English)
    :param start_index: Location of the columns in the given file
    :param end_index: Optional - the end index for given file (needed if the institution provides additional data in their tables that is not required).
    :param sheet_name: Optional - the sheet name of the file that is being parsed from a given institution
    :return: Returns the file path of the generated file
    '''

    url = url_dict['main'] + url_dict[page_file][pf_name]
    req = requests.get(url)

    if sheet_name:
        df = pd.read_excel(req.content, sheet_name=sheet_name)
    else:
        df = pd.read_excel(req.content)

    df = df[columns]
    index_start_rows = df.index[df[start_index[0]] == start_index[1]].tolist()

    if end_index:
        index_end_rows = df.index[df[end_index[0]] == end_index[1]].tolist()
        df = df.iloc[index_start_rows[0] + 1:index_end_rows[0]]
    else:
        df = df.iloc[index_start_rows[0] + 1:]

    df.columns = rename_columns
    sex = rename_columns[1:]
    df = pd.melt(df, id_vars=['Age'], value_vars=sex, var_name='Sex', value_name='Life_Expectancy')

    directory = source_pyll_le
    file_path = path.join(directory, filename)

    df.to_csv(file_path, index=False)
    return file_path


def merge_cz_files(file_men: str, file_women: str) -> str:
    '''
    Function merges the life expectancy files for men and women in Czechia
    :param file_men: source file for life expectancy for men
    :param file_women: source file for life expectancy for men
    :return: Returns the file path of the generated file
    '''

    file_men = path.join(source_pyll_le, file_men)
    file_women = path.join(source_pyll_le, file_women)

    df_men = pd.read_csv(file_men)
    df_women = pd.read_csv(file_women)

    df_women.dropna(how='any', axis=0, inplace=True)
    df_women['Age'] = df_women['Age'].astype('int')

    df_men.dropna(how='any', axis=0, inplace=True)
    df_men['Age'] = df_men['Age'].astype('int')

    frames = [df_men, df_women]
    both_sexes = pd.concat(frames)
    both_sexes = both_sexes.round(2)

    file_name = 'cz_life_expectancy_both_sexes.csv'
    file_path = path.join(source_pyll_le, file_name)
    both_sexes.to_csv(file_path, index=False)

    return file_path
