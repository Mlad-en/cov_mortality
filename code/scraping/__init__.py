if __name__ == '__main__':
    # Scrape Ministry of Health of Bulgaria
    from mh_utils import *

    DATES = {'start_date': (2020, 3, 1),
             'end_date': (2021, 1, 16),
             }
    # file_name = save_raw_mh_articles(DATES)
    df = generate_raw_mortality_per_person('C:\\Users\\mmladenov\\Desktop\\github_repos\\cov_mortality\\source_data\\MH_raw_article_text_from_(2020, 3, 1)_to_(2021, 1, 16).csv')
    df_clean = generate_person_attributes(df)

    # Get Life Expectancies for different countries
    # from code.url_constants import LIFE_EXPECTANCY_DATA
    # from code.scraping.get_life_expectancies import get_life_expectancy_cl
    #
    # country_data = LIFE_EXPECTANCY_DATA
    # for key, countries_regions in country_data.items():
    #     file = get_life_expectancy_cl(
    #         init_file=countries_regions['init_file'],
    #         sheet_name=countries_regions.get('sheet_name'),
    #         url_dict=countries_regions['url_dict'],
    #         page_file=countries_regions['page_file'],
    #         pf_name=countries_regions['pf_name'],
    #         columns=countries_regions['columns'],
    #         rename_columns=countries_regions['rename_columns'],
    #         start_index=countries_regions['start_index'],
    #         end_index=countries_regions.get('end_index')
    #     )
    #     print(f'finished with {file}')
