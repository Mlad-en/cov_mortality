MH_TITLE_ARTICLE_PATTERN = r'^[1-9]+.+(корона|COVID)'

MH_SPIT_BY_GENDER_ARTICLE_PATTERN = r'(мъж|жена|бебе)'

MH_RAW_ARTICLE_TEXT_COLUMNS = ['title', 'link', 'date', 'article_text']

MH_PER_PERSON_COLUMNS = [
    'date', 'person_data_raw', 'gender',
    'age', 'no_comorbidity', 'diabetes',
    'cardiac', 'neurological', 'pulmonary',
    'oncological', 'hepatological', 'pneumonia',
    'unknown'
]

MH_PER_PERSON_COMORBIDITY = {
    'diabetes': ['диабет'],
    'cardiac': ['сърдеч'],
    'hematological': ['хематологич'],
    'neurological': ['неврологич'],
    'pulmonary': ['белодроб'],
    'pneumonia': ['пневмония'],
    'oncological': ['онкологич'],
    'hepatological': ['чернодроб'],
    'nephrological': ['бъбре'],
    'unknown': ['неуточнено'],
}

MH_PER_PERSON_AGE_PATTERN = r'[\d]+'

EUROSTAT_AGES = ['ck_Y_LT5', 'ck_Y5-9', 'ck_Y10-14', 'ck_Y15-19', 'ck_Y20-24', 'ck_Y25-29', 'ck_Y30-34',
                 'ck_Y35-39', 'ck_Y40-44', 'ck_Y45-49', 'ck_Y50-54', 'ck_Y55-59', 'ck_Y60-64', 'ck_Y65-69',
                 'ck_Y70-74', 'ck_Y75-79', 'ck_Y80-84', 'ck_Y85-89', 'ck_Y_GE90', ]

EUROSTAT_COUNTRIES = ['ck_BE', 'ck_BG', 'ck_PL', 'ck_ES', 'ck_FR',
                      # 'ck_RO',
                      ]

EUROSTAT_BG_CITIES = ['ck_BG311', 'ck_BG312', 'ck_BG313', 'ck_BG314', 'ck_BG315', 'ck_BG321', 'ck_BG322',
                      'ck_BG323', 'ck_BG324', 'ck_BG325', 'ck_BG331', 'ck_BG332', 'ck_BG333', 'ck_BG334',
                      'ck_BG341', 'ck_BG342', 'ck_BG343', 'ck_BG344', 'ck_BG411', 'ck_BG412', 'ck_BG413',
                      'ck_BG414', 'ck_BG415', 'ck_BG421', 'ck_BG422', 'ck_BG423', 'ck_BG424', 'ck_BG425', ]

EUROSTAT_SEXES = ['ck_F', 'ck_M']

EUROSTAT_AGES_CONVERSION = {
    'Less than 5 years': '0-4',
    'From 5 to 9 years': '5-9',
    'From 10 to 14 years': '10-14',
    'From 15 to 19 years': '15-19',
    'From 20 to 24 years': '20-24',
    'From 25 to 29 years': '25-29',
    'From 30 to 34 years': '30-34',
    'From 35 to 39 years': '35-39',
    'From 40 to 44 years': '40-44',
    'From 45 to 49 years': '45-49',
    'From 50 to 54 years': '50-54',
    'From 55 to 59 years': '55-59',
    'From 60 to 64 years': '60-64',
    'From 65 to 69 years': '65-69',
    'From 70 to 74 years': '70-74',
    'From 75 to 79 years': '75-79',
    'From 80 to 84 years': '80-84',
    'From 85 to 89 years': '85-89',
    '90 years or over': '90+',
}

EUROSTAT_AGES_AVERAGES = {
    '0-4': 2, '5-9': 7, '10-14': 12, '15-19': 17,
    '20-24': 22, '25-29': 27, '30-34': 32, '35-39': 37,
    '40-44': 42, '45-49': 47, '50-54': 52, '55-59': 57,
    '60-64': 62, '65-69': 67, '70-74': 72, '75-79': 77,
    '80-84': 82, '85-89': 87, '90+': 92,
}

EUROSTAT_COMBINE_FILES_BY_WEEK = {
    'reduce_columns': ['YEAR', 'WEEK', 'GEO', 'SEX', 'AGE', 'Value'],
    'avg_per_year_group': ['YEAR', 'WEEK', 'GEO', 'SEX', 'AGE'],
    'group_by': ['GEO', 'WEEK', 'SEX', 'AGE'],
    'by': 'by_week_',
}
EUROSTAT_UPPER_BOUND_WORKING_GROUP = [
    '40-44',
    '45-49',
    '50-54',
    '55-59',
    '60-64',
]

EUROSTAT_COMBINE_FILES_TOTAL = {
    'reduce_columns': ['YEAR', 'GEO', 'SEX', 'AGE', 'Value'],
    'avg_per_year_group': ['YEAR', 'GEO', 'SEX', 'AGE'],
    'group_by': ['GEO', 'SEX', 'AGE'],
    'by': 'total_',
}

EUROSTAT_BG_CITIES_LIST = [
    'Blagoevgrad',
    'Burgas',
    'Dobrich',
    'Gabrovo',
    'Haskovo',
    'Kardzhali',
    'Kyustendil',
    'Lovech',
    'Montana',
    'Pazardzhik',
    'Pernik',
    'Pleven',
    'Plovdiv',
    'Razgrad',
    'Ruse',
    'Shumen',
    'Silistra',
    'Sliven',
    'Smolyan',
    'Sofia',
    'Sofia (stolitsa)',
    'Stara Zagora',
    'Targovishte',
    'Varna',
    'Veliko Tarnovo',
    'Vidin',
    'Vratsa',
    'Yambol',
]

EUROSTAT_COUNTRIES_LIST = ['Bulgaria', 'Poland', 'Belgium', 'France', 'Spain']

YEARS_WEEKNUMS_MAPPING = {
    2015: 53,
    2016: 52,
    2017: 52,
    2018: 52,
    2019: 52,
    2020: 53,
}
