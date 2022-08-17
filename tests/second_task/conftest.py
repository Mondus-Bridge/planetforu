import pytest
from selenium import webdriver
from selenium.webdriver.chrome.options import Options as chrome_options
from selenium.webdriver.chrome.service import Service



@pytest.fixture
def get_chrome_options():
    options = chrome_options()
    options.add_experimental_option('excludeSwitches', ['enable-logging'])
    options.add_argument('headless')  # Use headless|chrome if you do not need a browser UI
    options.add_argument('--start-maximized')
    options.add_argument('--window-size=1980,1080')
    return options


@pytest.fixture(scope="function")
def browser(get_chrome_options):
    options = get_chrome_options
    s = Service(executable_path = "F:\\PFM\\driver_chrome\\chromedriver.exe") #this handle this error: DeprecationWarning: executable_path has been deprecated, please pass in a Service object
    browser = webdriver.Chrome(service=s, options = options)
    yield browser
    print("\nquit browser..")
    browser.quit()