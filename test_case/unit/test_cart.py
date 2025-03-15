import pytest
from base_page.unit.cart import Cart
from utilities.config_reader import Cart_config
from utilities.config_reader import SearchBar_config

addtocart_home_page = Cart_config.get_add_to_cart_home_page_location()
addtocart_search_page = Cart_config.get_add_to_cart_search_page_location()
addtocart_product_page = Cart_config.get_add_to_cart_product_page_location()
black_cart_button = Cart_config.get_black_cart_button()
shopping_cart_button = Cart_config.get_shopping_cart_button()
empty_cart_message = Cart_config.get_empty_cart_message()
black_cart_info = Cart_config.get_black_cart_info()
success_prompt = Cart_config.get_success_prompt()
warning_prompt = Cart_config.get_warning_prompt()

search_bar_location = SearchBar_config.get_search_bar_location()
search_button_location = SearchBar_config.get_search_button_location()
url = SearchBar_config.get_base_url()

@pytest.fixture()
def setup_cart(setup):
    setup.get(url)
    setup.maximize_window()
    yield setup
    return setup

def test_add_product_home_page(setup_cart):
    browser=Cart(setup_cart)
    browser.adding_to_cart_homepage(addtocart_home_page)
    browser.clicking_black_cart_button(black_cart_button)
    browser.verify_the_empty_cart(black_cart_info,empty_cart_message)


