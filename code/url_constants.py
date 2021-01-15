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
        'life_expectancy':
            '/bg/content/3018/смъртност-и-средна-продължителност-на-предстоящия-живот-на-населението-по-местоживеене',
    },
    'files': {
        'mortality_per_week': '/bg/node/18121/',
        'life_expectancy': '/sites/default/files/files/data/timeseries/Pop_3.1_tab_mortality_DR.xls',
    }
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
            '&blobheadervalue1=attachment%3B+filename%3DD1T5.xlsx&blobkey=urldata&blobtable'
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