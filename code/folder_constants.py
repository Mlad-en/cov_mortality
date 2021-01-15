from pathlib import Path
from os import path

project_folder = Path(__file__).parent.parent

source_data = path.join(project_folder,'source_data')

output_data = path.join(project_folder, 'output_data')