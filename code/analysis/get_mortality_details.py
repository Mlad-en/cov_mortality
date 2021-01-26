from os import path
from typing import List, Union

import pandas as pd
import datetime

from code.folder_constants import source_data


def calc_avg_mortality_by_period(init_file: str, group_by: str,
                                 country: str,
                                 dt_format: str,
                                 start_date: Union[List[int], None] = None,
                                 end_date: Union[List[int], None] = None, ) -> str:
    '''
    :param init_file: File name containing data to be analyzed
    :param group_by: (date | weeknum) <- way of aggregating data
    :param country: specify countries_regions iso code
    :param dt_format:
    :param start_date: Optional - start period for calculation provided in the following format:
    [YYYY, MM, DD]
    :param end_date: Optional - end period for calculation provided in the following format:
    [YYYY, MM, DD]
    :return: Returns file path of the generated file
    '''
    init_df = pd.read_csv(init_file)

    init_df['date'] = pd.to_datetime(init_df['date'], format='%d.%m.%Y')
    init_df.insert(1, 'year', init_df['date'].dt.isocalendar().year, True)
    init_df.insert(1, 'weeknum', init_df['date'].dt.isocalendar().week, True)
    init_df['date'] = pd.to_datetime(init_df.date).dt.date

    if start_date and end_date:
        init_df = init_df[(init_df['date'] >= datetime.date(*start_date))
                          & (init_df['date'] <= datetime.date(*end_date))]
    if start_date:
        init_df = init_df[init_df['date'] >= datetime.date(*start_date)]
    if end_date:
        init_df = init_df[init_df['date'] <= datetime.date(*end_date)]

    avg_mortality_by_period = init_df.groupby(['year', group_by, 'gender'])['age'].mean().round(2)

    file_name = f'{country}_average_age_by_gender_by_{group_by}.csv'
    file_path = path.join(source_data, file_name)
    avg_mortality_by_period.to_csv(file_path, encoding='utf-8-sig')

    return file_path