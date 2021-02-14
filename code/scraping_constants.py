MH_TITLE_ARTICLE_PATTERN = r'^[1-9]+.+(корона|COVID|коронавирусна)'

MH_SPIT_BY_GENDER_ARTICLE_PATTERN = r'(мъж|жена|бебе)'

MH_RAW_ARTICLE_TEXT_COLUMNS = ['title', 'link', 'date', 'article_text']

MH_PER_PERSON_COLUMNS = [
    'date', 'person_data_raw', 'gender',
    'age', 'no_comorbidity', 'diabetes',
    'cardiovascular', 'neurological', 'pulmonary',
    'oncological', 'hepatological', 'pneumonia',
    'unknown', 'obeasity',
]

MH_PER_PERSON_COMORBIDITY = {
    'diabetes': ['диабет'],
    'cardiovascular': ['сърдеч', ' инфаркт', 'инсулт', 'исхемич', 'хематологич', 'съдов', 'артериална хипертония'],
    'neurological': ['неврологич', 'деменция', 'алцхаймер'],
    'pulmonary': ['белодроб', 'ХОББ', 'хронична обструктивна белодробна болест', 'астма'],
    'pneumonia': ['пневмония'],
    'oncological': ['онкологич', 'рак', 'имунен дефицит'],
    'hepatological': ['чернодроб'],
    'nephrological': ['бъбре'],
    'obeasity': ['затлъстяване'],
    'unknown': ['неуточнено', 'множество придружаващи заболявания', 'множество заболявания'],
}

MH_PER_PERSON_AGE_PATTERN = r'[\d]+'

EUROSTAT_AGES = ['ck_Y_LT5', 'ck_Y5-9', 'ck_Y10-14', 'ck_Y15-19', 'ck_Y20-24', 'ck_Y25-29', 'ck_Y30-34',
                 'ck_Y35-39', 'ck_Y40-44', 'ck_Y45-49', 'ck_Y50-54', 'ck_Y55-59', 'ck_Y60-64', 'ck_Y65-69',
                 'ck_Y70-74', 'ck_Y75-79', 'ck_Y80-84', 'ck_Y85-89', 'ck_Y_GE90', ]

EUROSTAT_COUNTRIES_CODES = ['ck_AT', 'ck_BE', 'ck_BG', 'ck_HR', 'ck_CY', 'ck_CZ', 'ck_DK', 'ck_EE', 'ck_FI', 'ck_FR',
                            'ck_EL', 'ck_HU', 'ck_IT', 'ck_LV', 'ck_LT', 'ck_LU', 'ck_MT', 'ck_NL', 'ck_PL', 'ck_PT',
                            'ck_RO', 'ck_SK', 'ck_SI', 'ck_ES', 'ck_SE'
                            ]

EUROSTAT_BG_CITIES_CODES = ['ck_BG311', 'ck_BG312', 'ck_BG313', 'ck_BG314', 'ck_BG315', 'ck_BG321', 'ck_BG322',
                            'ck_BG323', 'ck_BG324', 'ck_BG325', 'ck_BG331', 'ck_BG332', 'ck_BG333', 'ck_BG334',
                            'ck_BG341', 'ck_BG342', 'ck_BG343', 'ck_BG344', 'ck_BG411', 'ck_BG412', 'ck_BG413',
                            'ck_BG414', 'ck_BG415', 'ck_BG421', 'ck_BG422', 'ck_BG423', 'ck_BG424', 'ck_BG425', ]

EUROSTAT_ES_CITIES_CODES = [
    'ck_ES11', 'ck_ES111', 'ck_ES112', 'ck_ES113', 'ck_ES114', 'ck_ES12', 'ck_ES120', 'ck_ES13', 'ck_ES130', 'ck_ES21',
    'ck_ES211', 'ck_ES212', 'ck_ES213', 'ck_ES22', 'ck_ES220', 'ck_ES23', 'ck_ES230', 'ck_ES24', 'ck_ES241', 'ck_ES242',
    'ck_ES243', 'ck_ES30', 'ck_ES300', 'ck_ES41', 'ck_ES411', 'ck_ES412', 'ck_ES413', 'ck_ES414', 'ck_ES415',
    'ck_ES416',
    'ck_ES417', 'ck_ES418', 'ck_ES419', 'ck_ES42', 'ck_ES421', 'ck_ES422', 'ck_ES423', 'ck_ES424', 'ck_ES425',
    'ck_ES43',
    'ck_ES431', 'ck_ES432', 'ck_ES51', 'ck_ES511', 'ck_ES512', 'ck_ES513', 'ck_ES514', 'ck_ES52', 'ck_ES521',
    'ck_ES522',
    'ck_ES523', 'ck_ES53', 'ck_ES531', 'ck_ES532', 'ck_ES533', 'ck_ES61', 'ck_ES611', 'ck_ES612', 'ck_ES613',
    'ck_ES614',
    'ck_ES615', 'ck_ES616', 'ck_ES617', 'ck_ES618', 'ck_ES62', 'ck_ES620', 'ck_ES63', 'ck_ES630', 'ck_ES64', 'ck_ES640',
    'ck_ES70', 'ck_ES703', 'ck_ES704', 'ck_ES705', 'ck_ES706', 'ck_ES707', 'ck_ES708', 'ck_ES709', ]

EUROSTAT_SEXES = ['ck_F', 'ck_M', 'ck_T']

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

EUROSTAT_TOTAl_AGE_GROUP = [
    '0-4', '5-9', '10-14', '15-19',
    '20-24', '25-29', '30-34', '35-39',
    '40-44', '45-49', '50-54', '55-59',
    '60-64', '65-69', '70-74', '75-79',
    '80-84', '85-89', '90+']

EUROSTAT_UPPER_BOUND_WORKING_GROUP = ['40-44', '45-49', '50-54', '55-59', '60-64', ]

EUROSTAT_WORKING_GROUP = ['15-19', '20-24', '25-29', '30-34', '35-39',
                          '40-44', '45-49', '50-54', '55-59', '60-64']

EUROSTAT_30s_BOUND_WORKING_GROUP = ['30-34', '35-39', ]

EUROSTAT_LATE_60s_RETIRED_GROUP = ['65-69', ]

EUROSTAT_COMBINE_FILES_TOTAL = {
    'reduce_columns': ['YEAR', 'GEO', 'SEX', 'AGE', 'Value'],
    'avg_per_year_group': ['YEAR', 'GEO', 'SEX', 'AGE'],
    'group_by': ['GEO', 'SEX', 'AGE'],
    'by': 'total_',
}

EUROSTAT_BG_CITIES_LIST = [
    'Blagoevgrad', 'Burgas', 'Dobrich', 'Gabrovo', 'Haskovo', 'Kardzhali', 'Kyustendil', 'Lovech', 'Montana',
    'Pazardzhik', 'Pernik', 'Pleven', 'Plovdiv', 'Razgrad', 'Ruse', 'Shumen', 'Silistra', 'Sliven', 'Smolyan',
    'Sofia', 'Sofia (stolitsa)', 'Stara Zagora', 'Targovishte', 'Varna', 'Veliko Tarnovo', 'Vidin', 'Vratsa',
    'Yambol', ]

# noinspection SpellCheckingInspection
EUROSTAT_ES_CITIES_LIST = {
    'Galicia', 'A Coruña', 'Lugo', 'Ourense', 'Pontevedra', 'Principado de Asturias', 'Asturias', 'Cantabria',
    'Cantabria',
    'País Vasco', 'Araba/Álava', 'Gipuzkoa', 'Bizkaia', 'Comunidad Foral de Navarra', 'Navarra', 'La Rioja', 'La Rioja',
    'Aragón', 'Huesca', 'Teruel', 'Zaragoza', 'Comunidad de Madrid', 'Madrid', 'Castilla y León', 'Ávila', 'Burgos',
    'León', 'Palencia', 'Salamanca', 'Segovia', 'Soria', 'Valladolid', 'Zamora', 'Castilla-la Mancha', 'Albacete',
    'Ciudad Real',
    'Cuenca', 'Guadalajara', 'Toledo', 'Extremadura', 'Badajoz', 'Cáceres', 'Cataluña', 'Barcelona', 'Girona', 'Lleida',
    'Tarragona', 'Comunitat Valenciana', 'Alicante/Alacant', 'Castellón/Castelló', 'Valencia/València', 'Illes Balears',
    'Eivissa, Formentera', 'Mallorca', 'Menorca', 'Andalucía', 'Almería', 'Cádiz', 'Córdoba', 'Granada', 'Huelva',
    'Jaén', 'Málaga', 'Sevilla', 'Región de Murcia', 'Murcia', 'Ciudad de Ceuta', 'Ceuta', 'Ciudad de Melilla',
    'Melilla',
    'Canarias', 'El Hierro', 'Fuerteventura', 'Gran Canaria', 'La Gomera', 'La Palma', 'Lanzarote', 'Tenerife', }

EUROSTAT_COUNTRIES_LIST = ['Bulgaria', 'Poland', 'Belgium', 'France', 'Spain']

EUROSTAT_EXTENDED_COUNTRIES_LIST = ['Austria', 'Belgium', 'Bulgaria', 'Croatia', 'Cyprus', 'Czechia',
                                    'Denmark', 'Estonia', 'Finland', 'France', 'Greece', 'Hungary',
                                    'Italy', 'Latvia', 'Lithuania', 'Luxembourg', 'Malta',
                                    'Netherlands', 'Poland', 'Portugal', 'Romania', 'Slovakia',
                                    'Slovenia', 'Spain', 'Sweden'
                                    ]

YEARS_WEEKNUMS_MAPPING = {
    2015: 53,
    2016: 52,
    2017: 52,
    2018: 52,
    2019: 52,
    2020: 53, }