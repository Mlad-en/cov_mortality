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