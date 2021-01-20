from time import sleep
from os import path, listdir, rename
from zipfile import ZipFile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from code.folder_constants import source_data, drivers
from code.url_constants import EUROSTAT_MORTALITY
from code.scraping_constants import EUROSTAT_AGES, EUROSTAT_SEXES, EUROSTAT_COUNTRIES


class WebDriver:
    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


def locate_and_click_element(browser, select_type: str, element_str: str, clicks: int = 1):
    sel_type = {
        'id': By.ID,
        'xpath': By.XPATH,
        'css': By.CSS_SELECTOR,
        'class': By.CLASS_NAME
    }
    item = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((sel_type[select_type], element_str)))
    for click in range(clicks):
        item.click()


def get_eurostat_mortality_by_5y_intervals(year, week_start, week_end):

    yw_list = [f'ck_{year}W{week:02d}' for week in range(week_start, week_end+1)]

    search_params = {
        'GEO': EUROSTAT_COUNTRIES,
        'AGE': EUROSTAT_AGES,
        'TIME': yw_list,
        'SEX': EUROSTAT_SEXES
    }

    # Set browser type, download location and driver location
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': source_data}
    chrome_options.add_experimental_option('prefs', prefs)
    location = drivers
    file = 'chromedriver.exe'
    file_path = path.join(location, file)
    driver = webdriver.Chrome(file_path, options=chrome_options)

    with WebDriver(driver) as browser:
        url = EUROSTAT_MORTALITY['main'] + EUROSTAT_MORTALITY['pages']['mortality_per_week']
        browser.get(url)
        browser.maximize_window()

        locate_and_click_element(browser, select_type='class', element_str='selectDataButton')

        # Switch to pop-up window
        windows = browser.window_handles
        browser.switch_to.window(windows[1])
        browser.maximize_window()

        for param_name, param_values in search_params.items():
            # Select search param (age, sex, time, country)
            locate_and_click_element(browser, select_type='xpath', element_str=f'//span[contains(text(), "{param_name}")]')
            # Uncheck selection for all search parameters
            locate_and_click_element(browser, select_type='id', element_str='checkUncheckAllCheckboxTable', clicks=2)
            # Set search parameters
            for item in param_values:
                locate_and_click_element(browser, select_type='id', element_str=item)

        locate_and_click_element(browser, select_type='id', element_str='updateExtractionButton')

        #  Switch to main window
        windows = browser.window_handles
        browser.switch_to.window(windows[0])

        locate_and_click_element(browser, select_type='css', element_str='li[class="download"]')
        locate_and_click_element(browser, select_type='css', element_str='input[value="Download in Excel Format"]')

        sleep(15)


if __name__ == '__main__':

    for year in range(2015, 2021):
        decode_years = {
            2015: 53,
            2016: 52,
            2017: 52,
            2018: 52,
            2019: 52,
            2020: 53,
        }
        get_eurostat_mortality_by_5y_intervals(year, 10, decode_years[year])

        # TO_DO - Turn code below into a decorator
        filename = max([path.join(source_data, file) for file in listdir(source_data)], key=path.getctime)
        rename(filename, path.join(source_data, f'EUROSTAT_RAW_YEAR_{year}.zip'))

        zip_file = max([path.join(source_data, file) for file in listdir(source_data)], key=path.getctime)
        with ZipFile(zip_file, 'r') as obj:
            list_files = obj.infolist()
            files = [file.filename for file in list_files if 'data' in file.filename.lower()]
            obj.extract(member=files[0], path=source_data, pwd=None)

        filename = path.join(source_data, files[0])
        rename(filename, path.join(source_data, f'EUROSTAT_RAW_YEAR_{year}.csv'))