from time import sleep
from os import path, listdir, rename
from typing import Dict
from zipfile import ZipFile

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

from code.folder_constants import drivers, eurostat_raw_files
from code.url_constants import EUROSTAT_MORTALITY


class WebDriver:
    def __init__(self, driver):
        self.driver = driver

    def __enter__(self):
        return self.driver

    def __exit__(self, exc_type, exc_val, exc_tb):
        self.driver.quit()


def locate_and_click_element(browser, select_type: str, element_str: str, clicks: int = 1) -> None:
    '''
    Function will search for an element and once located it will click on it a given amount of times(default=1).
    :param browser: the webdriver handling the website interaction
    :param select_type: the search parameter (id, xpath, css, class)
    :param element_str: The actual element search string (e.g. id1)
    :param clicks: Optional parameter: The amount of clicks performed on the given element
    :return:
    '''

    sel_type = {
        'id': By.ID,
        'xpath': By.XPATH,
        'css': By.CSS_SELECTOR,
        'class': By.CLASS_NAME
    }
    item = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((sel_type[select_type], element_str)))
    for click in range(clicks):
        item.click()


def get_eurostat_mortality_by_5y_intervals(search_params: Dict) -> None:
    '''
    Function will scrape the Eurostat's report for mortality and extract csv files based on a given set of search params.
    :param search_params: Dictionary of search parameters (sex, age, location) for data extraction.
    :return: Function does not return values.
    '''

    # Set browser type, download location and driver location
    chrome_options = webdriver.ChromeOptions()
    prefs = {'download.default_directory': eurostat_raw_files}
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
            # Select search param (age, sex, time, countries_regions)
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
        locate_and_click_element(browser, select_type='css', element_str='input[value="Download in CSV Format"]')

        sleep(15)


def extract_eurostat_files(location: str, year: int, group: str):
    '''
    Function renames the most recently downloaded file in the given location.
    It will then extract a csv file from it that contains the word 'data' in it.
    Finally it will rename the extracted file.

    Warning: The most recent file in the given location must be a zip file.
    :param location: The location where the the file to extracted from is stored.
    The file that will be extracted will be extracted in the same file.
    :param group:
    :param year: The year contained in the file in question. This is needed for the naming convention of the file.
    :return: Function returns the file path of the extracted csv file
    '''

    filename = max([path.join(location, file) for file in listdir(location)], key=path.getctime)
    rename(filename, path.join(location, f'EUROSTAT_RAW_YEAR_{group}_{year}.zip'))

    zip_file = max([path.join(location, file) for file in listdir(location)], key=path.getctime)
    with ZipFile(zip_file, 'r') as obj:
        list_files = obj.infolist()
        files = [file.filename for file in list_files if 'data' in file.filename.lower()]
        obj.extract(member=files[0], path=location, pwd=None)

    filename = path.join(location, files[0])
    file_path = path.join(location, f'EUROSTAT_RAW_YEAR_{group}_{year}.csv')
    rename(filename, file_path)

    return file_path