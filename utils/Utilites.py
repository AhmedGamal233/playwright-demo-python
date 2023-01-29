import csv
from configparser import ConfigParser
import os

def read_test_data_from_csv_multi_col():
    test_data = []
    with open("test_data/test_data.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        next(data)  # skip header row
        for row in data:
            test_data.append(row)
    return test_data



def read_test_data_from_csv_single_col():
    test_data = []
    with open("test_data/test_data.csv", newline="") as csvfile:
        data = csv.reader(csvfile, delimiter=",")
        next(data)  # skip header row
        for row in data:
            edit ="".join(row)
            test_data.append(edit)
    return test_data

def get_browser(browser) -> dict:
    browser_list = {
        "chrome": {"browser": "chromium"},
        "firefox": {"browser": "firefox"},
        "safari": {"browser": "webkit"},
        "edge": {"browser": "chromium", "channel": "msedge"},
    }
    env_browser: str = os.getenv("BROWSER", browser)
    if env_browser not in browser_list:
        raise Exception("Invalid browser")

    return browser_list[env_browser]



def browserName():
    # instantiate
    config = ConfigParser()
    # parse existing file
    config.read('pytest.ini')
    # read values from a section
    return config.get('Browser', 'browserName')

def base_Url():
    # instantiate
    config = ConfigParser()
    # parse existing file
    config.read('pytest.ini')
    # read values from a section
    return config.get('pytest', 'base_url')