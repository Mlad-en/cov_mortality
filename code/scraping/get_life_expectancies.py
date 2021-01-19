from os import path
from typing import Dict, List, Union

import requests
import pandas as pd

from code.folder_constants import source_data


def get_life_expectancy_cl(filename: str, url_dict: Dict, page_file: str, pf_name: str,
                 columns: List, rename_columns: List, start_index: List,
                 end_index: Union[List, None] = None, sheet_name: Union[str, None] = None) -> str:
    '''
    Country Level (cl) function - function makes a request to a given statistics institution's web page.
    It downloads a file containing the institution's life expectancy for their country.
    :param filename: the file naming convention for the resulting file
    :param url_dict: The URL structure of the given statistics institution's page
    :param page_file: (pages | files) <-- within the URL structure of the statistic institution's page
    :param pf_name: The page or file name
    :param columns: The column names of the
    :param rename_columns:
    :param start_index: Location of the columns in the given file
    :param end_index: Optional - the end index for given file (needed if the institution provides additional data in their tables that is not required).
    :param sheet_name: Optional - the sheet name of the file that is being parsed from a given institution
    :return: Returns the file path of the generated file
    '''

    url = url_dict['main'] + url_dict[page_file][pf_name]
    req = requests.get(url)

    if sheet_name:
        df = pd.read_excel(req.content, sheet_name=sheet_name)
    else:
        df = pd.read_excel(req.content)

    df = df[columns]
    index_start_rows = df.index[df[start_index[0]] == start_index[1]].tolist()

    if end_index:
        index_end_rows = df.index[df[end_index[0]] == end_index[1]].tolist()
        df = df.iloc[index_start_rows[0] + 1:index_end_rows[0]]
    else:
        df = df.iloc[index_start_rows[0] + 1:]

    df.columns = rename_columns

    directory = source_data
    file_path = path.join(directory, filename)

    df.to_csv(file_path, index=False)
    return file_path


def merge_cz_files(file_men: str, file_women: str) -> str:
    '''

    :param file_men:
    :param file_women:
    :return:
    '''

    file_men = path.join(source_data, file_men)
    file_women = path.join(source_data, file_women)

    df_men = pd.read_csv(file_men)
    df_women = pd.read_csv(file_women)

    df_women.dropna(how='any', axis=0, inplace=True)
    df_women['age'] = df_women['age'].astype('int')

    df_men.dropna(how='any', axis=0, inplace=True)
    df_men['age'] = df_men['age'].astype('int')

    both_sexes = df_men.merge(df_women, on='age', how='left')
    both_sexes = both_sexes.round(2)

    file_name = 'cz_life_expectancy_both_sexes'
    file_path = path.join(source_data, file_name)
    both_sexes.to_csv(file_path, index=False)

    return file_path



if __name__ == '__main__':
    # merge_cz_files('cz_life_expectancy_men.csv','cz_life_expectancy_women.csv')

#     from code.url_constants import LIFE_EXPECTANCY_DATA
#
#     country_data = LIFE_EXPECTANCY_DATA
#     for key, country in country_data.items():
#         file = get_life_expectancy_cl(
#             init_file=country['init_file'],
#             sheet_name=country.get('sheet_name'),
#             url_dict=country['url_dict'],
#             page_file=country['page_file'],
#             pf_name=country['pf_name'],
#             columns=country['columns'],
#             rename_columns=country['rename_columns'],
#             start_index=country['start_index'],
#             end_index=country.get('end_index')
#         )
#         print(f'finished with {file}')