import pytest
from selenium import webdriver
from selenium.webdriver.chrome.webdriver import WebDriver


def pytest_AddOption(parser):
    parser.addoption("--browser",action="store",default="chrome",help="This flag can allow us to choose the browser we want to execute out test cases on chrome,firefox and edge." )
    return parser

@pytest.fixture()
def browser(request):
    return request.config.getoption("--browser")

@pytest.fixture()
def setup(browser):
    global driver
    if browser == "chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    elif browser=="edge":
        driver=webdriver.Edge()
    else:
        raise AssertionError("Please give the valid browser option")

    yield driver
    driver.quit()
    return driver