from datetime import date
from os import path
from typing import List, Union, Tuple

import pandas as pd

from code.folder_constants import source_mortality_cz, output_pyll_cz
from code.url_constants import CZ_COV_URL


def get_cz_cov_mortality() -> str:
    url = CZ_COV_URL['main'] + CZ_COV_URL['files']['mortality_by_age_gender']
    df = pd.read_csv(url)

    df['datum'] = pd.to_datetime(df['datum'], format='%Y-%m-%d').dt.date
    df['Sex'] = df.apply(lambda x: 'Male' if x['pohlavi'] == 'M' else 'Female', axis=1)

    df.rename(columns={'datum': 'Date', 'vek': 'Age'}, inplace=True)
    df = df[['Date', 'Age', 'Sex']]

    directory = source_mortality_cz
    file_name = 'cz_covid_19_mortality_by_age_gender.csv'
    file_path = path.join(directory, file_name)
    df.to_csv(file_path, index=False)

    return file_path


def get_cov_mort_and_lf_expectancy(life_expectancy_file: str,
                                   covid_mortality_file: str,
                                   directory: str,
                                   filename: str,
                                   start_date: Union[List, Tuple] = (2020, 3, 1),
                                   end_date: Union[List, Tuple] = (2020, 12, 31),
                                   start_age: int = 0,
                                   end_age: int = 150,
                                   sheet_name: Union[str, None] = None) -> str:

    lf_ex = pd.read_csv(life_expectancy_file)
    if sheet_name:
        cov_mort = pd.read_excel(covid_mortality_file, sheet_name=sheet_name)
    else:
        cov_mort = pd.read_csv(covid_mortality_file)

    cov_mort['Date'] = pd.to_datetime(cov_mort['Date'], format='%Y-%m-%d').dt.date
    cov_mort = cov_mort[
                        (cov_mort['Date'] >= date(year=start_date[0], month=start_date[1], day=start_date[2]))
                        & (cov_mort['Date'] <= date(year=end_date[0], month=end_date[1], day=end_date[2]))
                        & (cov_mort['Age'] >= start_age)
                        & (cov_mort['Age'] <= end_age)
                        ]

    cov_mort = cov_mort.merge(lf_ex, how='inner', on=['Age', 'Sex'])

    directory = directory
    file_name = filename
    file_path = path.join(directory, file_name)
    cov_mort.to_csv(file_path, index=False)

    return file_path
