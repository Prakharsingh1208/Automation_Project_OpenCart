import allure
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

class Search_Bar_Test:
    def __init__(self,driver):
        self.driver=driver
    @allure.step("Clicking on search button")
    def click_on_search_button(self,search_button_location):
        self.driver.find_element(By.XPATH,search_button_location).click()

    @allure.step("Entering the search query")
    def entering_the_search_parameter(self,search_bar_location,search_query,test_case_id):
        self.driver.find_element(By.XPATH,search_bar_location).send_keys(search_query)

    @allure.step("verifying the search results")
    def search_verification(self,product_catalog_location,test_case_id):
        try:
            product = self.driver.find_element(By.XPATH, product_catalog_location)
            if test_case_id in ["TC_SB_01_01", "TC_SB_01_02"]:
                assert "iPhone" in product.text, f"Expected 'iPhone' in search results, but got: {product.text}"
            else:
                assert not product.is_displayed(), f"Unexpected product found for {test_case_id}"
        except NoSuchElementException:
            if test_case_id in ["TC_SB_01_01", "TC_SB_01_02"]:
                assert False, f"Expected 'iPhone' to be found, but no product was displayed."
            else:
                assert True