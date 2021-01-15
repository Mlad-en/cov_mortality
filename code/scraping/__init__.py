from mh_utils import *

if __name__ == '__main__':

    DATES = {'start_date': (2020, 6, 6),
             'end_date': (2020, 6, 7),
             }
    file_name = save_raw_mh_articles(DATES)
    df = generate_raw_mortality_per_person(file_name)
    df_clean = generate_person_attributes(df)