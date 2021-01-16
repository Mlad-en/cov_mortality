import datetime
from os import path

import pandas as pd
import numpy as np
from requests import get
from bs4 import BeautifulSoup

from code.url_constants import BG_NSI_URL
from code.folder_constants import source_data


def get_mortality_in_bulgaria():
    '''
    Function scrapes the Bulgarian National Statistics Institute for Excess Death.

    It then generates a file with the excess death for 2020 comparing it with a 5-year average.

    Finally the function returns the file path of the file.
    '''
    url = BG_NSI_URL['main'] + BG_NSI_URL['pages']['mortality_per_week']
    req = get(url)
    page = BeautifulSoup(req.content, 'lxml')
    mortality_per_week_file = page.find(
        lambda tag: tag.name == 'a' and 'Умирания в България по седмици в периода' in tag.text)
    mortality_per_week_path = mortality_per_week_file['href']
    file_req = get(BG_NSI_URL['main'] + mortality_per_week_path)

    df = pd.read_excel(file_req.content, engine='openpyxl')

    df.dropna(axis=1, how='all', inplace=True)
    headers = df.iloc[2]
    df.dropna(axis=0, how='any', inplace=True)
    df.columns = headers
    df.rename(columns={df.columns[0]: "Year"}, inplace=True)
    df.replace('x', np.nan, inplace=True)

    avg_years_start = df[df['Year'].str.startswith('2015')].index.values[0]
    avg_years_end = df[df['Year'].str.startswith('2019')].index.values[0]
    analyzed_year = df[df['Year'].str.startswith('2020')].index.values[0]

    excess_death = pd.DataFrame()
    excess_death['average_death'] = df.loc[avg_years_start:avg_years_end].mean()
    death_2020 = df.loc[analyzed_year]
    excess_death['death_2020'] = death_2020
    excess_death = excess_death[excess_death['death_2020'] != '-']
    excess_death['excess_death'] = excess_death['death_2020'] - excess_death['average_death']

    excess_death.reset_index(inplace=True)
    excess_death.rename(columns={excess_death.columns[0]: "Week"}, inplace=True)
    excess_death['Week'] = excess_death['Week'].str.replace('W', '')

    scrape_date = datetime.date.today()
    file_name = f'BG_excess_mortality_scrdt({scrape_date}).csv'
    location = source_data
    file_location = path.join(location, file_name)
    excess_death.to_csv(file_location, encoding='utf-8-sig', index=False)

    return file_location


