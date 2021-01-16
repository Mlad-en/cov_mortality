from datetime import date, timedelta
from os import path
from typing import Dict, Tuple, Generator, Union


from bs4 import BeautifulSoup
import re
import requests
import pandas as pd

from code.folder_constants import source_data
from code.mh_scraping_constants import *
from code.url_constants import BG_MH_URL


def generate_dates_between_periods(dates: Dict[str, Tuple[int, int, int]]) -> Generator[Tuple[str, str], None, None]:
    '''
    Function takes in
    :param dates: Periods should be provided in a Dictionary format as follows:
    {'start_date':(YEAR, MM, DD),
    'end_date': (YEAR, MM, DD)}
    E.g. start date: (2020.04.20) || end date: (2020.04.25)
    :return: Returns a generator of string start and end dates between given periods, incrementing by 1.
    End Date is excluded from the return generator.
    '''

    start_date = date(*dates['start_date'])
    end_date = date(*dates['end_date'])
    delta = end_date - start_date
    for i in range(delta.days):
        start_range = start_date + timedelta(days=i)
        end_range = start_date + timedelta(days=i + 1)
        yield start_range.strftime('%d.%m.%Y'), end_range.strftime('%d.%m.%Y')


def get_mh_articles(s_range: str, e_range: str) -> requests.models.Response:
    '''Returns request response object of the Ministry of Health of Bulgaria website with Covid-19-related
    articles posted between a given date period.
    '''
    URL = BG_MH_URL['main'] + BG_MH_URL['pages']['news']['landing_page']
    params = {
        BG_MH_URL['pages']['news']['page_params']['start_date']: s_range,
        BG_MH_URL['pages']['news']['page_params']['end_date']: e_range,
    }
    req = requests.get(URL, params=params)
    return req


def parse_stats_article_links(req: requests.models.Response) -> Union[Tuple[str, str], Tuple[None, None]]:
    '''Returns a tuple of strings containing the title and link to articles containing Covid-19 statistics'''
    soup = BeautifulSoup(req, 'lxml')
    stats_article = soup.find_all('a', text=re.compile(TITLE_ARTICLE_PATTERN))
    if stats_article:
        article_link = BG_MH_URL['main'] + stats_article[0]['href'][1:]  # strips leading slash "/"
        title = stats_article[0].text
        return article_link, title
    else:
        return None, None


def parse_article_text_and_date(article_link: str) -> Tuple[str, str]:
    '''Returns a tuple containing the date and article text from a given article link'''
    req = requests.get(article_link)
    soup = BeautifulSoup(req.content, 'lxml')
    date = soup.find('time').text
    article_text = soup.find('div', class_='single_news').text
    return date, article_text


def save_raw_mh_articles(period_dict: Dict[str, Tuple[int, int, int]]) -> str:
    '''
    Function saves a csv file with all articles related to COVID between the provided period of the function input.
    The function will return the file path of the generated file.
    :param period_dict: Periods should be provided in a Dictionary format as follows:
    {'start_date':(YEAR, MM, DD),
    'end_date': (YEAR, MM, DD)}
    E.g. start date: (2020.04.20) || end date: (2020.04.25)
    :return: File name of the generated file, in the following format:
    MH_raw_article_text_from_{START_DATE}_to_{END_DATE}.csv
    '''

    df = pd.DataFrame(columns=RAW_ARTICLE_TEXT_COLUMNS)

    for start_range, end_range in generate_dates_between_periods(period_dict):
        page = get_mh_articles(start_range, end_range)
        page_content = parse_stats_article_links(page.content)
        link, title = page_content

        if link:
            dt, article_text = parse_article_text_and_date(link)
        else:
            dt, article_text = None, None

        data = {
            'date': start_range,
            'title': title,
            'link': link,
            'dt_str': dt,
            'article_text': article_text
        }
        df = df.append(data, ignore_index=True)

    file_name = f'MH_raw_article_text_from_{period_dict["start_date"]}_to_{period_dict["end_date"]}.csv'
    location = source_data
    file_location = path.join(location, file_name)
    df.to_csv(file_location, encoding='utf-8-sig', index=False)

    return file_location


def generate_raw_mortality_per_person(original_file: str) -> pd.DataFrame:
    '''
    Function parses articles from a provided csv file and generates a dataframe with raw person information about
    persons that have passed from COVID-19.
    :param original_file: Receives a file path to csv file with articles about COVID from the Bulgarian Ministry of Health.
    :return: Returns a Data frame with person records about persons that have passed from COVID-19.
    '''

    raw_per_person_df = pd.DataFrame(columns=PER_PERSON_COLUMNS)
    raw_article_text_df = pd.read_csv(original_file)

    for index in raw_article_text_df.index:
        article_text = raw_article_text_df.at[index, 'article_text']
        date = raw_article_text_df.at[index, 'date']
        mortality_groups_extract = re.finditer(SPIT_BY_GENDER_ARTICLE_PATTERN, article_text)
        start_ranges = [mortality_group.start() for mortality_group in mortality_groups_extract]

        if start_ranges:
            mortality_snippet = []

            if len(start_ranges) > 1:
                for index in range(0, len(start_ranges) - 1):
                    article_start_index = start_ranges[index]
                    article_end_index = start_ranges[index + 1]
                    mortality_line = article_text[article_start_index:article_end_index]
                    mortality_snippet.append(mortality_line)

            final_line_start = start_ranges[-1]
            final_line_end = article_text.find('\n', final_line_start)
            mortality_line = article_text[final_line_start:final_line_end]
            mortality_snippet.append(mortality_line)

            for person_mortality in mortality_snippet:
                data = {
                    'date': date,
                    'person_data_raw': person_mortality.strip('\n')
                }
                raw_per_person_df = raw_per_person_df.append(data, ignore_index=True)

    return raw_per_person_df


def generate_person_attributes(df: pd.DataFrame) -> str:
    '''
    Function receives a data frame object with raw person data and parses it for comorbities, age and sex of the person.
    The function saves a csv file of the generated dataframe and returns the file path to the file.
    :param df: Receives dataframe object with raw per person data scraped from the Bulgarian Ministry of Health.
    :return: Returns the file path of the created csv file.
    '''
    unknown = 'ненамерено'

    df = df

    for index in df.index:
        person_data = df.at[index, 'person_data_raw']

        for attr_name, attr_values in PER_PERSON_COMORBIDITY.items():
            for attr in attr_values:
                if attr in person_data:
                    df.at[index, attr_name] = 'Y'
                    break
            else:
                df.at[index, attr_name] = 'N'

        no_comorbidity = 'Y' if 'придружаващи заболявания' in person_data \
                                and ('без' in person_data or 'няма' in person_data) \
            else ''
        df.at[index, 'no_comorbidity'] = no_comorbidity

        gender = 'мъж' if 'мъж' in person_data else 'жена' if 'жена' in person_data else unknown
        df.at[index, 'gender'] = gender

        try:
            age = re.findall(PER_PERSON_AGE_PATTERN, person_data)[0]
            df.at[index, 'age'] = age
        except (TypeError, IndexError):
            continue

    file_name = f'PER_PERSON_DATA.csv'
    location = source_data
    file_location = path.join(location, file_name)
    df.to_csv(file_location, encoding='utf-8-sig', index=False)

    return file_location