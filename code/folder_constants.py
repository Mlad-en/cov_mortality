from pathlib import Path
from os import path

project_folder = Path(__file__).parent.parent

source_data = path.join(project_folder,'source_data')

output_data = path.join(project_folder, 'output_data')

code = path.join(project_folder, 'code')

scraping = path.join(code, 'scraping')

drivers = path.join(scraping, 'drivers')



