import allure
import pytest
from selenium.webdriver.common.by import By
from base.home_page import Currency
from utilities.config_reader import ConfigHomePage
from utilities.logs_genrator import LogsGenrator

currencyButton=ConfigHomePage.GetCurrencyLocattion()
log = LogsGenrator.logs_gen()
demoProductPriceLocation=ConfigHomePage.GetDemoPriceLocation()

@pytest.fixture()
def ClickingCurrencyButton(setup):
    log.info(f"[+] -> Clicking the currency button")
    setup.find_element(By.XPATH,currencyButton).click()
    return setup

@allure.title("Select Dollar as the currency")
@allure.feature("Multi-Currency Support")
@allure.label("test_id","TC-009")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Test to verify the change in product currency when selecting the currency as Dollar")
def test_009(ClickingCurrencyButton):
    testCaseID = "TC-009"
    dollarButton = ConfigHomePage.GetDollarlocation()
    browser = Currency(ClickingCurrencyButton)
    browser.SelectingCurrency(dollarButton,"$")
    browser.CurrencyValidation(demoProductPriceLocation,"$",testCaseID)

@allure.title("Select Euro as the currency")
@allure.feature("Multi-Currency Support")
@allure.label("test_id","TC-007")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Test to verify the change in product currency when selecting the currency as Euro")
def test_007(ClickingCurrencyButton):
    testCaseID = "TC-007"
    euroButton=ConfigHomePage.GetEurolocation()
    browser = Currency(ClickingCurrencyButton)
    browser.SelectingCurrency(euroButton,"€")
    browser.CurrencyValidation(demoProductPriceLocation,"€",testCaseID)

@allure.title("Select Pound as the currency")
@allure.feature("Multi-Currency Support")
@allure.label("test_id","TC-008")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Test to verify the change in product currency when selecting the currency as Pound")
def test_008(ClickingCurrencyButton):
    testCaseID = "TC-008"
    poundButton=ConfigHomePage.GetPoundlocation()
    browser = Currency(ClickingCurrencyButton)
    browser.SelectingCurrency(poundButton,"£")
    browser.CurrencyValidation(demoProductPriceLocation,"£",testCaseID)
