import pytest
from selenium import webdriver

def pytest_addoption(parser):
    parser.addoption("--browser", action="store", default="chrome", help="Choose browser: chrome, edge, firefox")
    return parser

@pytest.fixture
def browser(request):
    return  request.config.getoption("--browser")

@pytest.fixture
def setup(browser):
    global driver
    if browser=="chrome":
        driver=webdriver.Chrome()
    elif browser=="firefox":
        driver=webdriver.Firefox()
    elif browser=="edge":
        driver=webdriver.Edge()
    else:
        raise AssertionError("Please provide the valid browser")

    yield driver
    driver.quit()
    return driver