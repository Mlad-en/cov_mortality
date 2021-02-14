from pathlib import Path
from os import path

project_folder = Path(__file__).parent.parent

# Scraping Util Folders
code = path.join(project_folder, 'code')
scraping = path.join(code, 'scraping')
drivers = path.join(scraping, 'drivers')

# Source Data
source_data = path.join(project_folder, 'source_data')
eurostat_main_source_folder = path.join(source_data, 'Eurostat_excess_mortality')
eurostat_combined_files = path.join(eurostat_main_source_folder, 'Combined_files')
eurostat_raw_files = path.join(eurostat_main_source_folder, 'Raw_files')

source_pyll_le = path.join(source_data, 'Life Expectancies')

source_cov_mortality = path.join(source_data, 'Covid-19 Mortality')
source_mortality_cz = path.join(source_cov_mortality, 'Czechia')
source_mortality_bg = path.join(source_cov_mortality, 'Bulgaria')
source_mortality_bg_auto = path.join(source_mortality_bg, 'Automated')
source_mortality_bg_combined = path.join(source_mortality_bg, 'Combined')


# Output Data
output_data = path.join(project_folder, 'output_data')
output_eurostat = path.join(output_data, 'EUROSTAT_DATA')
output_eurostat_ext_countries = path.join(output_eurostat, 'EXTENDED_COUNTRIES')
output_eurostat_excel = path.join(output_eurostat_ext_countries, 'EXCEL')
output_eurostat_latex = path.join(output_eurostat_ext_countries, 'LATEX')
output_pyll = path.join(output_data, 'PYLL')
output_pyll_cz = path.join(output_pyll, 'Czechia')
output_pyll_bg = path.join(output_pyll, 'Bulgaria')


