from pathlib import Path
from os import path

project_folder = Path(__file__).parent.parent

source_data = path.join(project_folder,'source_data')

eurostat_main_source_folder = path.join(source_data,'Eurostat_excess_mortality')

eurostat_combined_files = path.join(eurostat_main_source_folder,'Combined_files')

eurostat_raw_files = path.join(eurostat_main_source_folder,'Raw_files')

output_data = path.join(project_folder, 'output_data')

code = path.join(project_folder, 'code')

scraping = path.join(code, 'scraping')

drivers = path.join(scraping, 'drivers')



