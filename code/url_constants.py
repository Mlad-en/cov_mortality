# Bulgarian Ministry of Health
BG_MH_URL = {
    'main': 'https://www.mh.government.bg/',
    'pages': {
        'news': {
            'landing_page': 'novini/aktualno/',
            'page_params': {'start_date': 'start_date', 'end_date': 'end_date', 'category': 'category'}
        },
    }
}

# Bulgarian National Statistics Institute
BG_NSI_URL = {
    'main': 'https://www.nsi.bg',
    'pages': {
        'mortality_per_week': '/bg/node/18121/',
        'life_expectancy':
            '/bg/content/3018/смъртност-и-средна-продължителност-на-предстоящия-живот-на-населението-по-местоживеене',
        'population_by_region':
        '/en/content/6704/population-districts-municipalities-place-residence-and-sex'
    },
    'files': {
        'mortality_per_week': '/bg/node/18121/',
        'life_expectancy': '/sites/default/files/files/data/timeseries/Pop_3.1_tab_mortality_DR.xls',
        'population_by_region': '/sites/default/files/files/data/timeseries/Pop_6.1.1_Pop_DR_EN.xls'
    }
}

# COVID-19 stats webpage for Bulgaria
BG_EGOV_URL = {
    'main': 'https://data.egov.bg',
    'pages': {},
    'files': {},
    'api': {
        'loc': '/api/getResourceView',
        'key': '4f7be417-16cd-492c-bb2a-03a5a66c175a',
        'resource_uri': {
            'general_stats': 'e59f95dd-afde-43af-83c8-ea2916badd19',
            'by_region_stats': 'cb5d7df0-3066-4d7a-b4a1-ac26525e0f0c',
            'by_age_stats': '8f62cfcf-a979-46d4-8317-4e1ab9cbd6a8',
            'tests_performed_stats': '0ce4e9c3-5dfc-46e2-b4ab-42d840caab92',
        },
    },
}

# United Kingdom Office for National Statistics
UK_ONS_URL = {
    'main': 'https://www.ons.gov.uk',
    'pages': {
        'life_expectancy':
            '/peoplepopulationandcommunity/birthsdeathsandmarriages/lifeexpectancies/'
            'datasets/nationallifetablesgreatbritainreferencetables',
    },
    'files': {
        'life_expectancy': '/file?uri=%2fpeoplepopulationandcommunity%2fbirthsdeathsandmarriages%'
                           '2flifeexpectancies%2fdatasets%2fnationallifetablesgreatbritainreferencetables'
                           '%2fcurrent/nationallifetables3yeargb.xlsx'
    }
}

# Spanish Institute for National Statistics
ES_INE_URL = {
    'main': 'https://www.ine.es',
    'pages': {
        'life_expectancy':
            'https://www.ine.es/ss/Satellite?c=INESeccion_C'
            '&cid=1259926380048&p=1254735110672'
            '&pagename=ProductosYServicios%2FPYSLayout'
    },
    'files': {
        'life_expectancy':
            '/ss/Satellite?blobcol=urldata&blobheader=Unknown+format&blobheadername1=Content-Disposition'
            '&blobheadervalue1=attachment%3B+init_file%3DD1T5.xlsx&blobkey=urldata&blobtable'
            '=MungoBlobs&blobwhere=697%2F241%2FD1T5.xlsx&ssbinary=true'
    }
}

# Czechia National Statistics Office
CZ_CZSO_URL = {
    'main': 'https://www.czso.cz',
    'pages': {
        'life_expectancy':'/csu/czso/umrtnostni-tabulky-za-cr-regiony-soudrznosti-a-kraje-2018-2019'
    },
    'files': {
        'life_expectancy_men': '/documents/10180/121739354/1300632001.xlsx/2056ff1b-2574-4af3-ac47-160b62b2129b?version=1.1',
        'life_expectancy_women': '/documents/10180/121739354/1300632002.xlsx/eda89506-30fa-46e1-b3db-eda58575ba78?version=1.1'
    }
}

#Czechia Covid-19 stats website
CZ_COV_URL = {
    'main': 'https://onemocneni-aktualne.mzcr.cz',
    'pages': {
        'api_list': '/api/v2/covid-19'
    },
    'files': {
        'mortality_by_age_gender': '/api/v2/covid-19/umrti.csv'
    }
}

# Eurostat website providing mortality data per countries_regions, week, gender and age group
EUROSTAT_MORTALITY = {
    'main': 'https://appsso.eurostat.ec.europa.eu',
    'pages': {
        'mortality_per_week': '/nui/show.do?dataset=demo_r_mweek3&lang=en'
    }
}

# __countries life expencancy bindings used for the country-level life expectancy function
LIFE_EXPECTANCY_DATA = {
    'Bulgaria': {
        'partial': False,
        'init_file': 'bg_life_expectancy.csv',
        'sheet_name': '2017-2019',
        'url_dict': BG_NSI_URL,
        'page_file': 'files',
        'pf_name': 'life_expectancy',
        'columns': ['Unnamed: 0', 'Unnamed: 8', 'Unnamed: 9'],
        'rename_columns': ['Age', 'Male', 'Female'],
        'start_index': ['Unnamed: 0', 'Общо за страната'],
        'end_index': ['Unnamed: 0', '100+']
    },
    'United Kingdom': {
        'partial': False,
        'init_file': 'uk_life_expectancy.csv',
        'sheet_name': '2017-2019',
        'url_dict': UK_ONS_URL,
        'page_file': 'files',
        'pf_name': 'life_expectancy',
        'columns': ['National Life Tables, Great Britain','Unnamed: 5', 'Unnamed: 11'],
        'rename_columns': ['Age', 'Male', 'Female'],
        'start_index': ['National Life Tables, Great Britain', 'x'],
    },
    'Czech Republic-MEN': {
        'partial': True,
        'partial_type': 'men',
        'init_file': 'cz_life_expectancy_men.csv',
        'url_dict': CZ_CZSO_URL,
        'page_file': 'files',
        'pf_name': 'life_expectancy_men',
        'columns': ['2019','Unnamed: 9'],
        'rename_columns': ['Age', 'Male'],
        'start_index': ['2019', 'věk (x) age'],
    },
    'Czech Republic-WOMEN': {
        'partial': True,
        'partial_type': 'women',
        'init_file': 'cz_life_expectancy_women.csv',
        'url_dict': CZ_CZSO_URL,
        'page_file': 'files',
        'pf_name': 'life_expectancy_women',
        'columns': ['2019', 'Unnamed: 9'],
        'rename_columns': ['Age', 'Female'],
        'start_index': ['2019', 'věk (x) age'],
    }
}

LIFE_EXPECTANCY_DATA_PACKAGED = {
    'Bulgaria': [LIFE_EXPECTANCY_DATA['Bulgaria']],
    'United Kingdom': [LIFE_EXPECTANCY_DATA['United Kingdom']],
    'Czechia': [LIFE_EXPECTANCY_DATA['Czech Republic-MEN'], LIFE_EXPECTANCY_DATA['Czech Republic-WOMEN']]
}