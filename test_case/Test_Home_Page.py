import time

import selenium
import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from test_case.conftest import setup, browser
from utilities.config_reader import ConfigHomePage
from base_page import home_page

url = ConfigHomePage.gethomepageurl()
SearchBarLocation = ConfigHomePage.GetSearchBarLocation()
SearchBarButton = ConfigHomePage.GetSearchButton()
ValidQuery = ConfigHomePage.GetValidQuery()
InvalidQuery = ConfigHomePage.GetInvalidQuery()
InvalidQueryResponse = ConfigHomePage.GetInvalidQueryResponse()

class Test_HomePageTitleVerfication:
    def test_001(self,setup):
        driver = setup
        driver.maximize_window()
        browser = home_page.HomepageTitleVerification(driver)
        browser.open_home_page(url)
        browser.home_page_title_verification()


class Test_SearchFeathure:
    def test_002(self,setup):
        driver = setup
        browser = home_page.SearchBar(driver)
        browser.open_home_page(url)
        browser.Search_bar_test_data_002(SearchBarLocation,ValidQuery)
        browser.ClickingSearchButton(SearchBarButton)
        browser.Search_bar_validation_002()

    def test_003(self,setup):
        driver = setup
        browser = home_page.SearchBar(driver)
        browser.open_home_page(url)
        browser.Search_bar_test_data_002(SearchBarLocation,InvalidQuery)
        browser.ClickingSearchButton(SearchBarButton)
        browser.Search_bar_validation_003(InvalidQueryResponse)

