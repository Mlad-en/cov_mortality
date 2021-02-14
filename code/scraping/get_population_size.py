import pandas as pd
from requests import get

from code.url_constants import BG_NSI_URL


def get_bg_population_by_gender_and_region():
    url = BG_NSI_URL['main'] + BG_NSI_URL['files']['population_by_region']
    req = get(url)

    df = pd.read_excel(req.content, sheet_name='2019', engine='xlrd')

    df.dropna(how='any', axis=0,inplace=True)
    avg_years_start = df[df.iloc[:,0].str.startswith('Municipalities')].index.values[0]
    headers = df.loc[avg_years_start].copy()
    headers = [f'pop_{val}' for val in headers]
    df.columns = headers
    df = df.iloc[1:, 0:4]

    df.drop_duplicates(subset=['pop_Municipalities'], keep='first', inplace=True)

    total_row = df[df.iloc[:, 0].str.startswith('Total')].index.values[0]
    total_men = df.at[total_row, 'pop_Male']
    total_women = df.at[total_row, 'pop_Female']
    total = df.at[total_row, 'pop_Total']

    df['pop_pct_males'] = df.apply(lambda x: (x['pop_Male'] / total_men) * 100, axis=1).round(2)
    df['pop_pct_females'] = df.apply(lambda x: (x['pop_Female'] / total_women) * 100, axis=1).round(2)
    df['pop_pct_total'] = df.apply(lambda x: (x['pop_Total'] / total) * 100, axis=1).round(2)

    return df