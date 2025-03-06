
import pytest
from selenium import webdriver
from utilities.config_reader import ConfigHomePage
from utilities.logs_genrator import LogsGenrator

url = ConfigHomePage.gethomepageurl()
log = LogsGenrator.logs_gen()

def pytest_addoption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="This flag can allow us to choose the browser we want to execute out test cases on chrome,firefox and edge.")
    return parser

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    try:
        if browser == "chrome":
            driver = webdriver.Chrome()
        elif browser == "firefox":
            driver = webdriver.Firefox()
        elif browser == "edge":
            driver = webdriver.Edge()
        else:
            raise ValueError("Unsupported browser")
    finally:
        log.info(f"------------------------------------------------------")
        log.info(f"[+] -> Opening {browser} browser")
        driver.maximize_window()
        log.info(f"[+] -> Maximizing the window")
        driver.get(url)
        log.info(f"[+] -> Opening the url: {url}")
    return driver
