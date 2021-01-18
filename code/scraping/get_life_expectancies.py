from os import path
from typing import Dict, List, Union

import requests
import pandas as pd

from code.folder_constants import source_data


def request_data(filename: str, url_dict: Dict, page_file: str, pf_name: str,
                 columns: List, rename_columns: List, start_index: int,
                 end_index: Union[int, None]=None, sheet_name: Union[str, None]=None):
    '''
    Function makes a request to a given statistics institution's web page.
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
    file_path = path.join(directory+filename)

    df.to_csv(file_path, index=False)
    return file_path