import allure
import pytest
from base_page.unit.Search_bar import Search_Bar_Test
from utilities.config_reader import SearchBar_config

url=SearchBar_config.get_base_url()
search_bar_location=SearchBar_config.get_search_bar_location()
search_button_location=SearchBar_config.get_search_button_location()
product_catalog_location=SearchBar_config.get_product_catalog()

@pytest.fixture
def search_setup(setup):
    setup.get(url)
    yield setup
    return setup

@pytest.mark.parametrize(("search_query","test_case_id"),[
    ("iphone","TC_SB_01_01"),
    ("IpHoNe","TC_SB_01_02"),
    ("ducjevdckx827","TC_SB_02_01"),
    ("!@#$%^&^%$#$%^","TC_SB_03_01"),
    ("' OR 1=1 --","TC_SB_04_01"),
    ("","TC_SB_05_01")
])
@allure.title("Testing the search bar with")
@allure.severity(allure.severity_level.CRITICAL)
def test_sending_search_parameter(search_setup,search_query,test_case_id):
    browser=Search_Bar_Test(search_setup)
    browser.entering_the_search_parameter(search_bar_location,search_query,test_case_id)
    browser.click_on_search_button(search_button_location)
    browser.search_verification(product_catalog_location,test_case_id)



