import allure
from base.home_page import AddToCart
from utilities.config_reader import ConfigHomePage
from utilities.logs_genrator import LogsGenrator

log = LogsGenrator.logs_gen()
location=ConfigHomePage.GetProductAddToCartLocation_Xpath()
cart_info_location=ConfigHomePage.GetCartInfoLocation()
empty_cart_message=ConfigHomePage.GetEmptyCartMessage()



@allure.label("Categories","TC-010")
@allure.title("Adding product to cart from home page")
@allure.feature("Shopping Cart")
@allure.severity(allure.severity_level.CRITICAL)
@allure.description("Test to verify that product can be added to cart from home page.")
def test_010(setup):
    test_case_id="TC-010"
    browser=AddToCart(setup)
    browser.ClickAddtoCart(location)
    browser.CartValidation(cart_info_location,empty_cart_message,test_case_id)

@allure.label("test_id","TC-011")
@allure.title("Verifying cart status when new user open the website")
@allure.feature("Shopping Cart")
@allure.severity(allure.severity_level.NORMAL)
@allure.description("Test to verify that cart should be empty upon opening the website as a new user.")
def test_011(setup):
    test_case_id="TC-011"
    browser=AddToCart(setup)
    browser.CartValidation(cart_info_location,empty_cart_message,test_case_id)

