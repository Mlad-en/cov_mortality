from os import path

import requests
import pandas as pd

from code.folder_constants import source_pyll_le
from code.url_constants import LIFE_EXPECTANCY_DATA_PACKAGED
from code.utils import FileSaver


class LifeExpectancy:

    def __init__(self, country):
        self.__saver = FileSaver
        self.__countries = LIFE_EXPECTANCY_DATA_PACKAGED
        self.country = country

    def __get_life_expectancy_cl(self, data) -> str:
        """

        :param data:
        :return:
        """
        url = data['url_dict']['main'] + data['url_dict'][data['page_file']][data['pf_name']]
        req = requests.get(url)

        sheet = data.get('sheet_name', 0)
        df = pd.read_excel(req.content, sheet_name=sheet)

        df = df[data['columns']]
        index_start_rows = df.index[df[data['start_index'][0]] == data['start_index'][1]].tolist()

        if data.get('end_index'):
            index_end_rows = df.index[df[data['end_index'][0]] == data['end_index'][1]].tolist()
            df = df.iloc[index_start_rows[0] + 1:index_end_rows[0]]
        else:
            df = df.iloc[index_start_rows[0] + 1:]

        df.dropna(how='all', axis=0, inplace=True)

        df.columns = data['rename_columns']
        sex = data['rename_columns'][1:]

        # Merge Men and Women categories under a single column - Sex.
        # All data(values) for both sexes is then transferred to the Life_Expectancy column.
        df = pd.melt(df, id_vars=['Age'], value_vars=sex, var_name='Sex', value_name='Life_Expectancy')

        file = self.__saver(df, source_pyll_le, data['init_file'])
        file.save_file_csv()
        return file.file_path

    def __merge_files(self, files) -> str:
        """
        Function merges the life expectancy files for __countries where life expectancy is split
        :return: Returns the file path of the generated file
        """

        file_men = path.join(source_pyll_le, files[0])
        file_women = path.join(source_pyll_le, files[1])

        df_men = pd.read_csv(file_men, converters={'Age': int})
        df_women = pd.read_csv(file_women)

        frames = [df_men, df_women]
        both_sexes = pd.concat(frames)

        file_name = 'cz_life_expectancy_both_sexes.csv'
        file = self.__saver(both_sexes, source_pyll_le, file_name)
        return file.save_file_csv()

    def get_le_raw_data(self) -> str:
        """
        :return:
        """
        if len(self.__countries[self.country]) == 1:
            return self.__get_life_expectancy_cl(*self.__countries[self.country])
        else:
            files = []
            for file in self.__countries[self.country]:
                files.append(self.__get_life_expectancy_cl(file))
            return self.__merge_files(files)