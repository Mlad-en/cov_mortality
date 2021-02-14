

if __name__ == '__main__':
    # Scrape Ministry of Health of Bulgaria
    # from mh_utils import *
    # from code.folder_constants import source_mortality_bg_auto
    # from os import path
    #
    # DATES = {'start_date': (2021, 1, 1),
    #          'end_date': (2021, 2, 5),
    #          }
    # # file_name = save_raw_mh_articles(DATES)
    # file = 'bg_mh_raw_article_text_from_(2021, 1, 1)_to_(2021, 2, 5).csv'
    # loc = source_mortality_bg_auto
    # file_path = path.join(loc, file)
    # df = generate_raw_mortality_per_person(file_path)
    # df_clean = generate_person_attributes(df)

    # Get Life Expectancies for different __countries
    from code.analysis.calc_pyll import calc_pyll_cz
    from code.url_constants import LIFE_EXPECTANCY_DATA
    from code.folder_constants import output_pyll_bg, source_mortality_bg_auto
    from code.scraping.get_covid_deaths_cz import get_cz_cov_mortality, get_cov_mort_and_lf_expectancy
    from code.scraping.get_life_expectancies import get_life_expectancy_cl, merge_cz_files
    #
    country_data = LIFE_EXPECTANCY_DATA
    files = []
    for key, countries_regions in country_data.items():
        file = get_life_expectancy_cl(
            filename=countries_regions['init_file'],
            sheet_name=countries_regions.get('sheet_name'),
            url_dict=countries_regions['url_dict'],
            page_file=countries_regions['page_file'],
            pf_name=countries_regions['pf_name'],
            columns=countries_regions['columns'],
            rename_columns=countries_regions['rename_columns'],
            start_index=countries_regions['start_index'],
            end_index=countries_regions.get('end_index')
        )
        files.append(file)

    cz_files = [file for file in files if 'cz' in file]
    cz_combined_le = merge_cz_files(cz_files[0], cz_files[1])
    cz_combined_mort = get_cz_cov_mortality()

    pyll_total_cz = get_cov_mort_and_lf_expectancy(cz_combined_le,
                                                   cz_combined_mort,
                                                   'Czechia - RAW PYLL(total).csv')

    pyll_40_64_cz = get_cov_mort_and_lf_expectancy(cz_combined_le,
                                                   cz_combined_mort,
                                                   'Czechia - RAW PYLL(40-64).csv',
                                                   start_age=40,
                                                   end_age=64)

    calc_pyll_cz(pyll_total_cz, 'Czechia - Calculated PYLL(Total).csv')
    calc_pyll_cz(pyll_40_64_cz, 'Czechia - Calculated PYLL(40-64).csv')

    bg_combined_le = 'C:\\Users\\mmladenov\\Desktop\\github_repos\\cov_mortality\\source_data\\Life Expectancies\\bg_life_expectancy.csv'
    bg_combined_mort = 'C:\\Users\\mmladenov\\Desktop\\github_repos\\cov_mortality\\source_data\\Covid-19 Mortality\\Bulgaria\\Combined\\Combined_bg_Cov_19_mortality.xlsx'
    pyll_total_bg = get_cov_mort_and_lf_expectancy(bg_combined_le,
                                                   bg_combined_mort,
                                                   output_pyll_bg,
                                                   'Bulgaria - RAW PYLL(total).csv',
                                                   sheet_name='combined_without_unk')

    pyll_40_64_bg = get_cov_mort_and_lf_expectancy(bg_combined_le,
                                                   bg_combined_mort,
                                                   output_pyll_bg,
                                                   'Bulgaria - RAW PYLL(40-64).csv',
                                                   start_age=40,
                                                   end_age=64,
                                                   sheet_name='combined_without_unk')

    calc_pyll_cz(pyll_total_bg, output_pyll_bg, 'Bulgaria - Calculated PYLL(Total).csv')
    calc_pyll_cz(pyll_40_64_bg, output_pyll_bg, 'Bulgaria - Calculated PYLL(40-64).csv')