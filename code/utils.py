from os import path

import pandas as pd


class FileSaver:
    def __init__(self, dataframe: pd.DataFrame, directory: str, filename: str):
        self.df = dataframe
        self.directory = directory
        self.filename = filename
        self.file_path = path.join(self.directory, self.filename)

    def save_file_csv(self, reset_index = None) -> str:
        if reset_index:
            self.df.reset_index().to_csv(self.file_path, index=False, encoding='utf-8-sig')
        else:
            self.df.to_csv(self.file_path, index=False, encoding='utf-8-sig')
        return self.file_path