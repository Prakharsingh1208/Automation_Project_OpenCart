import logging
import time
import selenium
import pytest
import self
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import select

from utilities.logs_genrator import LogsGenrator
from test_case.conftest import setup, browser
from utilities.config_reader import ConfigHomePage
from base_page import home_page


url = ConfigHomePage.gethomepageurl()
SearchBarLocation = ConfigHomePage.GetSearchBarLocation()
SearchBarButton = ConfigHomePage.GetSearchButton()
ValidQuery = ConfigHomePage.GetValidQuery()
InvalidQuery = ConfigHomePage.GetInvalidQuery()
InvalidQueryResponse = ConfigHomePage.GetInvalidQueryResponse()
HomePageTitle = ConfigHomePage.GetHomePageTitle()
SqlPayload = ConfigHomePage.GetSqlPayload()
CurrencyButtonLocation = ConfigHomePage.GetCurrencyLocattion()
DollarLocation = ConfigHomePage.GetDollarlocation()
PoundLocation = ConfigHomePage.GetPoundlocation()
EuroLocation = ConfigHomePage.GetEurolocation()
DemoPriceLocation = ConfigHomePage.GetDemoPriceLocation()
ProductAddToCartLocation = ConfigHomePage.GetProductAddToCartLocation_Xpath()
CartInfoLocation = ConfigHomePage.GetCartInfoLocation()
EmptyCartMessage = ConfigHomePage.GetEmptyCartMessage()

class Test_HomePageTitleVerfication:
    log = LogsGenrator.logs_gen()
    def test_001(self,setup):
        testCaseID = 'TC-001'
        driver = setup
        browser = home_page.HomepageTitleVerification(driver)
        browser.home_page_title_verification(HomePageTitle,testCaseID)



class Test_SearchFeathure:
    log = LogsGenrator.logs_gen()
    def test_002(self,setup):
        testCaseID = 'TC-002'
        driver = setup
        browser = home_page.SearchBar(driver)
        browser.Search_bar_test_data_entery(SearchBarLocation,ValidQuery)
        browser.ClickingSearchButton(SearchBarButton)
        browser.Search_bar_validation_valid_test_data(ValidQuery,testCaseID)

    def test_003(self,setup):
        testCaseID = 'TC-003'
        driver = setup
        browser = home_page.SearchBar(driver)
        browser.Search_bar_test_data_entery(SearchBarLocation,InvalidQuery)
        browser.ClickingSearchButton(SearchBarButton)
        browser.Search_bar_validation_invalid_test_data(InvalidQueryResponse,testCaseID)

    def test_004(self,setup):
        testCaseID = 'TC-004'
        driver = setup
        browser = home_page.SearchBar(driver)
        browser.Search_bar_test_data_entery(SearchBarLocation,'')
        browser.ClickingSearchButton(SearchBarButton)
        browser.Search_bar_validation_invalid_test_data(InvalidQueryResponse,testCaseID)

    def test_005(self,setup):
        testCaseID = 'TC-005'
        driver = setup
        browser = home_page.SearchBar(driver)
        browser.Search_bar_test_data_entery(SearchBarLocation,'!@#$%^&*()_+_)(*&^%$#{}|}":?><')
        browser.ClickingSearchButton(SearchBarButton)
        browser.Search_bar_validation_invalid_test_data(InvalidQueryResponse,testCaseID)

    def test_006(self,setup):
        testCaseID = 'TC-006'
        driver = setup
        browser = home_page.SearchBar(driver)
        browser.Search_bar_test_data_entery(SearchBarLocation,SqlPayload)
        browser.ClickingSearchButton(SearchBarButton)
        browser.Search_bar_validation_invalid_test_data(InvalidQueryResponse,testCaseID)

class Test_Curency:
    log = LogsGenrator.logs_gen()
    def test_007(self,setup):
        testCaseID = 'TC-007'
        driver = setup
        browser = home_page.Currency(driver)
        browser.ClickCurrencyButton(CurrencyButtonLocation)
        browser.SelectingCurrency(EuroLocation,'€')
        browser.CurrencyValidation(DemoPriceLocation,'€',testCaseID)

    def test_008(self,setup):
        testCaseID = 'TC-008'
        driver = setup
        browser = home_page.Currency(driver)
        browser.ClickCurrencyButton(CurrencyButtonLocation)
        browser.SelectingCurrency(PoundLocation,'£')
        browser.CurrencyValidation(DemoPriceLocation,'£',testCaseID)

    def test_009(self,setup):
        testCaseID = 'TC-009'
        driver = setup
        browser = home_page.Currency(driver)
        browser.ClickCurrencyButton(CurrencyButtonLocation)
        browser.SelectingCurrency(DollarLocation,'$')
        browser.CurrencyValidation(DemoPriceLocation,'$',testCaseID)

class Test_Cart:
    log = LogsGenrator.logs_gen()
    def test_010(self,setup):
        testCaseID = 'TC-010'
        drive = setup
        browser = home_page.AddToCart(drive)
        browser.ClickAddtoCart(ProductAddToCartLocation)
        browser.CartValidation(CartInfoLocation,EmptyCartMessage,testCaseID)

    def test_011(self,setup):
        testCaseID = 'TC-011'
        drive = setup
        browser = home_page.AddToCart(drive)
        browser.CartValidation(CartInfoLocation,EmptyCartMessage,testCaseID)



