TITLE_ARTICLE_PATTERN = r'^[1-9]+.+(корона|COVID)'

SPIT_BY_GENDER_ARTICLE_PATTERN = r'(мъж|жена|бебе)'

RAW_ARTICLE_TEXT_COLUMNS = ['title', 'link', 'date', 'article_text']

PER_PERSON_COLUMNS = ['date', 'person_data_raw', 'gender',
                      'age', 'no_comorbidity', 'diabetes',
                      'cardiac', 'neurological', 'pulmonary',
                      'oncological', 'hepatological', 'pneumonia',
                      'unknown']

PER_PERSON_COMORBIDITY = {
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

PER_PERSON_AGE_PATTERN = r'[\d]+'

EUROSTAT_AGES = ['ck_Y_LT5', 'ck_Y5-9', 'ck_Y10-14', 'ck_Y15-19', 'ck_Y20-24', 'ck_Y25-29', 'ck_Y30-34',
                 'ck_Y35-39', 'ck_Y40-44', 'ck_Y45-49', 'ck_Y50-54', 'ck_Y55-59', 'ck_Y60-64', 'ck_Y65-69',
                 'ck_Y70-74', 'ck_Y75-79', 'ck_Y80-84', 'ck_Y85-89', 'ck_Y_GE90', ]

EUROSTAT_COUNTRIES = ['ck_BE', 'ck_BG', 'ck_PL', 'ck_ES', 'ck_FR', 'ck_RO', ]

EUROSTAT_SEXES = ['ck_F', 'ck_M']
