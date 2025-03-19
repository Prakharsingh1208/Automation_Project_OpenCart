import time

import pytest
import allure
from allure_commons.types import Severity
from selenium.webdriver.support.wait import WebDriverWait

from base_page.unit.cart import Cart
from base_page.unit.Search_bar import Search_Bar_Test
from utilities.config_reader import Cart_config
from utilities.config_reader import SearchBar_config

addtocart_home_page = Cart_config.get_add_to_cart_home_page_location()
addrocart_home_page_2 = Cart_config.get_addtocart_homepage_2()
addtocart_search_page = Cart_config.get_add_to_cart_search_page_location()
addtocart_product_page = Cart_config.get_add_to_cart_product_page_location()
product_page_location=Cart_config.get_product_page_location()
black_cart_button = Cart_config.get_black_cart_button()
shopping_cart_button = Cart_config.get_shopping_cart_button()
empty_cart_message = Cart_config.get_empty_cart_message()
black_cart_info = Cart_config.get_black_cart_info()
success_prompt = Cart_config.get_success_prompt()
warning_prompt = Cart_config.get_warning_prompt()
black_cart_button_item_list = Cart_config.get_black_cart_button_item_list()
delete_item_from_cart_location=Cart_config.get_delete_item_from_cart_location()

search_bar_location = SearchBar_config.get_search_bar_location()
search_button_location = SearchBar_config.get_search_button_location()
url = SearchBar_config.get_base_url()

@allure.step(f"Opening the {url}  and maximizing window")
@pytest.fixture()
def setup_cart(setup):
    setup.get(url)
    setup.maximize_window()
    yield setup
    return setup

@allure.title("TC_ATC_01_01: Adding product to cart from home page")
@allure.description("Testing by adding the product to cart from home page")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_product_home_page(setup_cart):
        test_case_id='TC_ATC_01_01'
        browser=Cart(setup_cart)
        browser.adding_to_cart_homepage(addtocart_home_page)
        browser.clicking_black_cart_button(black_cart_button)
        browser.verify_the_empty_cart(black_cart_info,empty_cart_message,success_prompt,test_case_id)

@allure.title("TC_ATC_02_01: Adding product to cart from search page")
@allure.description("Testing by adding the product to cart from search page")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_product_search_page(setup_cart):
        test_case_id='TC_ATC_02_01'
        browser=Search_Bar_Test(setup_cart)
        browser.entering_the_search_parameter(search_bar_location,'iphone',test_case_id)
        browser.click_on_search_button(search_button_location)
        browser=Cart(setup_cart)
        browser.adding_to_cart_search_page(addtocart_search_page)
        browser.clicking_black_cart_button(black_cart_button)
        browser.verify_the_empty_cart(black_cart_info,empty_cart_message,success_prompt,test_case_id)

@allure.title("TC_ATC_03_01: Adding product to cart from product description")
@allure.description("Testing by adding the product to cart from product page")
@allure.severity(allure.severity_level.CRITICAL)
def test_add_product_from_product_discription(setup_cart):
        test_case_id='TC_ATC_03_01'
        browser=Cart(setup_cart)
        browser.clicking_product_page(product_page_location)
        browser.adding_to_cart_product_page(addtocart_product_page)
        browser.clicking_black_cart_button(black_cart_button)
        browser.verify_the_empty_cart(black_cart_info,empty_cart_message,success_prompt,test_case_id)


@allure.title("TC_ATC_03_01: Adding Multiple product to cart")
@allure.description("Testing by adding the multiple product to cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_adding_multiple_product_to_cart(setup_cart):
        test_case_id='TC_ATC_05_01'
        browser=Cart(setup_cart)
        browser.adding_to_cart_homepage(addtocart_home_page)
        browser.adding_to_cart_homepage(addrocart_home_page_2)
        setup_cart.refresh()
        browser.clicking_black_cart_button(black_cart_button)
        browser.verify_multiple_item_in_cart(black_cart_button_item_list,test_case_id)


@allure.title("TC_ATC_05_01: Removing the product from 'Shopping Cart'")
@allure.description("Testing by item from cart")
@allure.severity(allure.severity_level.CRITICAL)
def test_remove_item_from_black_button(setup_cart):
        test_case_id='TC_ATC_05_01'
        browser=Cart(setup_cart)
        browser.adding_to_cart_homepage(addtocart_home_page)
        browser.clicking_black_cart_button(black_cart_button)
        browser.click_deleted_addto_cart(delete_item_from_cart_location)
        browser.clicking_black_cart_button(black_cart_button,'-')
        browser.verify_if_the_cart_is_empty(black_cart_info,empty_cart_message,test_case_id)