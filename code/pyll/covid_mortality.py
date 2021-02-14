from os import path

import pandas as pd

from code.folder_constants import source_mortality_cz, source_mortality_bg_combined
from code.url_constants import CZ_COV_URL
from code.utils import FileSaver


class GetFullCovidMortality:

    def __init__(self, country):
        self.saver = FileSaver
        self.country = country
        self.country_mapping = {
            'Bulgaria': self.__bg_mortality,
            'Czechia': self.__get_cz_cov_mortality
        }

    @staticmethod
    def __bg_mortality():
        bg_mortality = path.join(source_mortality_bg_combined, 'Combined_bg_Cov_19_mortality.xlsx')
        return bg_mortality

    def __get_cz_cov_mortality(self) -> str:
        url = CZ_COV_URL['main'] + CZ_COV_URL['files']['mortality_by_age_gender']
        df = pd.read_csv(url)

        df['datum'] = pd.to_datetime(df['datum'], format='%Y-%m-%d').dt.date
        df['Sex'] = df.apply(lambda x: 'Male' if x['pohlavi'] == 'M' else 'Female', axis=1)

        df.rename(columns={'datum': 'Date', 'vek': 'Age'}, inplace=True)
        df = df[['Date', 'Age', 'Sex']]

        file_name = 'cz_covid_19_mortality_by_age_gender.csv'
        file = self.saver(df, source_mortality_cz, file_name)
        file.save_file_csv()
        return file.file_path

    def get_covid_mortality(self):
        file = self.country_mapping.get(self.country)()
        if file:
            return file