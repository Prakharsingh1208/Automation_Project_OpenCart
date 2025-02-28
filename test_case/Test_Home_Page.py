import time

import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_case.conftest import setup, browser
from utilities.config_reader import Config
from base_page import home_page

url = Config.gethomepageurl()
SearchBarLocation = Config.GetSearchBarLocation()
class Test_HomePage:
    def test_01(self,setup):
        driver = setup
        browser = home_page.HomePage(driver)
        browser.open_home_page(url)
        browser.home_page_title_verification()

    def test_02(self,setup):
        driver = setup
        browser = home_page.HomePage(driver)
        browser.open_home_page(url)
        browser.Search_bar_validation_01(SearchBarLocation)