if __name__ == '__main__':
    from mh_utils import *

    DATES = {'start_date': (2020, 3, 1),
             'end_date': (2021, 1, 16),
             }
    file_name = save_raw_mh_articles(DATES)
    df = generate_raw_mortality_per_person(file_name)
    df_clean = generate_person_attributes(df)

