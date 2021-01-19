from time import sleep
from os import path

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


def uncheck_default_selection(browser):
    select_all = WebDriverWait(browser, 10).until(EC.element_to_be_clickable((By.ID, 'checkUncheckAllCheckboxTable')))
    select_all.click()
    select_all.click()


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
        buttons = browser.find_elements_by_class_name('selectDataButton')
        buttons[0].click()

        # Switch to pop-up window
        windows = browser.window_handles
        browser.switch_to.window(windows[1])
        browser.maximize_window()

        for param_name, param_values in search_params.items():
            title = browser.find_element_by_xpath(f'//span[contains(text(), "{param_name}")]')
            title.click()
            uncheck_default_selection(browser)

            for item in param_values:
                checkbox = browser.find_element_by_id(item)
                checkbox.click()

        update_button = browser.find_element_by_id('updateExtractionButton')
        update_button.click()

        #  Switch to main window
        windows = browser.window_handles
        browser.switch_to.window(windows[0])

        download_button = browser.find_element_by_css_selector('li[class="download"]')
        download_button.click()

        download_xls = browser.find_element_by_css_selector('input[value="Download in Excel Format"]')
        download_xls.click()
        sleep(15)