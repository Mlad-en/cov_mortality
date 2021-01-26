from code.analysis.eurostat_excess_mortality import *
from code.analysis.get_mortality_details import calc_avg_mortality_by_period
from code.analysis.get_excess_mortality import calc_bg_excess_mortality

from code.scraping.excess_mortality_utils import get_mortality_in_bulgaria
from code.scraping.mortality_eurostat import get_eurostat_mortality_by_5y_intervals, extract_eurostat_files
from code.scraping_constants import *

from code.folder_constants import eurostat_raw_files


# scraped_file = get_mortality_in_bulgaria()
# total_mortality = calc_bg_excess_mortality(scraped_file)
# mortaliry_oct_dec = calc_bg_excess_mortality(scraped_file, 43, 53)
# print(total_mortality)
# print(mortaliry_oct_dec)
#
# file = ''
# calc_avg_mortality_by_period(file, 'date')
# calc_avg_mortality_by_period(file, 'weeknum')

# EUROSTAT FILES - Turn into a function


def get_eurostat_excess_mortality_data(year_weeks, regions_countries: List, sex: List,
                                       raw_file_append_desc: str, combined_file_name, exclude_reg_cntry: Union[List, None] = None):
    '''

    :param year_weeks:
    :param regions_countries:
    :param sex:
    :param raw_file_append_desc:
    :param combined_file_name:
    :param exclude_reg_cntry:
    :return:
    '''
    files = []
    decode_years = year_weeks
    geography = regions_countries
    sex = sex

    for year, weeks in decode_years.items():
        # generates the week number - year mapping that is used when scraping the eurostat website
        yw_list = [f'ck_{year}W{week:02d}' for week in range(10, weeks + 1)]

        search_params = {
            'GEO': geography,
            'AGE': EUROSTAT_AGES,
            'TIME': yw_list,
            'SEX': sex
        }

        get_eurostat_mortality_by_5y_intervals(search_params)
        file = extract_eurostat_files(eurostat_raw_files, year, raw_file_append_desc)
        files.append(file)

    prev_years = files[0:-1]
    current_year = files[-1]
    f_name = combined_file_name

    weekly_file_name = 'weekly_' + f_name
    eurostat_combined_weekly_file = merge_eurostat_files(prev_years, current_year, weekly_file_name, exclude_reg_cntry,
                                                         incl_week=True)
    total_file_name = 'total_' + f_name
    eurostat_combined_total_file = merge_eurostat_files(prev_years, current_year, total_file_name, exclude_reg_cntry)

    return eurostat_combined_weekly_file, eurostat_combined_total_file


if __name__ == '__main__':
    combined_cntry_weekly, combined_cntry_total = get_eurostat_excess_mortality_data(YEARS_WEEKNUMS_MAPPING,
                                                                                     regions_countries=EUROSTAT_COUNTRIES,
                                                                                     sex=EUROSTAT_SEXES,
                                                                                     raw_file_append_desc='by_COUNTRIES_F_M_WEEKLY',
                                                                                     combined_file_name='excess_mortality_by_age_gender_pscore_EU_countries.csv',
                                                                                     exclude_reg_cntry=['Romania'])

    combined_cities_weekly, combined_cities_total = get_eurostat_excess_mortality_data(YEARS_WEEKNUMS_MAPPING,
                                                                                       regions_countries=EUROSTAT_BG_CITIES,
                                                                                       sex=EUROSTAT_SEXES,
                                                                                       raw_file_append_desc='by_BG_CITIES_F_M_WEEKLY',
                                                                                       combined_file_name='excess_mortality_by_age_gender_pscore_bg_cities.csv')

    file_name = 'excess_mortality_gender_ages_from_From 40 to 64 years_BG_PO_BE_FR_ES_by_country.csv'
    calc_mort_by_cntry_gndr_and_age_groups(combined_cntry_total, EUROSTAT_COUNTRIES_LIST,
                                           EUROSTAT_UPPER_BOUND_WORKING_GROUP, file_name)

    file_name = 'excess_mortality_gender_ages_from_From 40 to 64 years_by_bg_cities.csv'
    calc_mort_by_cntry_gndr_and_age_groups(combined_cities_total, EUROSTAT_BG_CITIES_LIST,
                                           EUROSTAT_UPPER_BOUND_WORKING_GROUP, file_name)

    file_name = 'average_mortality_age_by_locale_and_gender_countries.csv'
    calc_average_excess_mortality_age(combined_cntry_weekly, EUROSTAT_COUNTRIES_LIST, file_name)

    file_name = 'average_mortality_age_by_locale_and_gender_bg_cities.csv'
    calc_average_excess_mortality_age(combined_cities_weekly, EUROSTAT_BG_CITIES_LIST, file_name)
