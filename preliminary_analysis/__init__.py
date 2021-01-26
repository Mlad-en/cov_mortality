# from os import path, listdir, rename
#
# from zipfile import ZipFile
#
# from code.scraping.mortality_eurostat import get_eurostat_mortality_by_5y_intervals
# from code.folder_constants import *
#
# for year in range(2015, 2021):
#     decode_years = {
#         2015: 53,
#         2016: 52,
#         2017: 52,
#         2018: 52,
#         2019: 52,
#         2020: 53,
#     }
#     get_eurostat_mortality_by_5y_intervals(year, 10, decode_years[year])
#
#     # TO_DO - Turn code below into a decorator
#     filename = max([path.join(eurostat_raw_files, file) for file in listdir(eurostat_raw_files)], key=path.getctime)
#     rename(filename, path.join(eurostat_raw_files, f'EUROSTAT_RAW_YEAR_{year}.zip'))
#
#     zip_file = max([path.join(eurostat_raw_files, file) for file in listdir(eurostat_raw_files)], key=path.getctime)
#     with ZipFile(zip_file, 'r') as obj:
#         list_files = obj.infolist()
#         files = [file.filename for file in list_files if 'data' in file.filename.lower()]
#         obj.extract(member=files[0], path=eurostat_raw_files, pwd=None)
#
#     filename = path.join(eurostat_raw_files, files[0])
#     final_file_name = path.join(eurostat_raw_files, f'EUROSTAT_RAW_YEAR_{year}.csv')
#     rename(filename, final_file_name)
#