import time

import allure
import pytest
from selenium.webdriver.common.by import By
from base.home_page import Currency
from utilities.config_reader import ConfigHomepageWishList
from base.HomePage.Wish_list import WishList
from utilities.logs_genrator import LogsGenrator

log = LogsGenrator.logs_gen()
wish_list_info_xpath=ConfigHomepageWishList.get_wish_list_info_xpath()
empty_wish_list_info=ConfigHomepageWishList.get_empty_wish_list_info()
product_wishlist_button_xpath=ConfigHomepageWishList.get_product_wishlist_button_xpath()

@pytest.fixture()
def setup_wish_list(setup):
    setup.maximize_window()
    return setup


@allure.label("test_id","TC-013")
@allure.title("Verify that wish list is empty when new user opens the website")
@allure.feature("Wishlist")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Test to verify that wishlist is empty when new user open the website for the first time.")
def test_wishlist_value_as_new_user(setup_wish_list):
    test_case_id="TC-013"
    browser=WishList(setup_wish_list)
    time.sleep(1)
    browser.validating_wishlist(wish_list_info_xpath,empty_wish_list_info,test_case_id,'-')

@allure.label("test_id","TC-012")
@allure.title("Verify that iVerify the wish feature from homepage without login team")
@allure.feature("Wishlist")
@allure.severity(allure.severity_level.MINOR)
@allure.description("Test to verify that when user add the item to the wishlist, that item should be saved in wishlist.")
def test_wishlist_by_adding_the_product(setup_wish_list):
    test_case_id="TC-012"
    browser=WishList(setup_wish_list)
    browser.click_add_wish_list_button_product(product_wishlist_button_xpath)
    time.sleep(1)
    browser.validating_wishlist(wish_list_info_xpath,empty_wish_list_info,test_case_id,'+')
