from os import path

import pandas as pd

from code.folder_constants import output_pyll_cz


def calc_pyll_cz(file: str, directory: str, result_file_name: str) -> str:

    df = pd.read_csv(file)

    cntr_pyll = df.groupby(['Sex']).agg(TOTAL_PYLL=('Life_Expectancy','sum'),
                                      PERSON_COUNT=('Age', 'count'),
                                      MEAN_AGE=('Age', 'mean'),
                                      AVG_PYLL=('Life_Expectancy', 'mean')).round(2)

    directory = directory
    file_name = result_file_name
    file_path = path.join(directory, file_name)
    cntr_pyll.reset_index().to_csv(file_path, index=False)

    return file_path