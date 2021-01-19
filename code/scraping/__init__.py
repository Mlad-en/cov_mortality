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
    # for key, country in country_data.items():
    #     file = get_life_expectancy_cl(
    #         init_file=country['init_file'],
    #         sheet_name=country.get('sheet_name'),
    #         url_dict=country['url_dict'],
    #         page_file=country['page_file'],
    #         pf_name=country['pf_name'],
    #         columns=country['columns'],
    #         rename_columns=country['rename_columns'],
    #         start_index=country['start_index'],
    #         end_index=country.get('end_index')
    #     )
    #     print(f'finished with {file}')
