import logging
import time
from time import sleep

import allure

from utilities.logs_genrator import LogsGenrator
import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# driver  = webdriver.Chrome()
# driver.find_element(By.XPATH,)
class Cart:
    logs = LogsGenrator.logs_gen()
    def __init__(self,driver):
        self.driver=driver

    @allure.step("Adding product to cart from home page")
    def adding_to_cart_homepage(self,add_to_cart_location):
        self.logs.info(f"adding product to cart from homepage")
        self.driver.find_element(By.XPATH,add_to_cart_location).click()

    @allure.step("adding product to cart from product page")
    def adding_to_cart_product_page(self,add_to_cart_location):
        self.logs.info(f"adding product to cart from product description")
        self.driver.find_element(By.XPATH,add_to_cart_location).click()

    @allure.step("adding product to cart from search page")
    def adding_to_cart_search_page(self,add_to_cart_location):
        self.logs.info(f"adding product to cart from search page")
        self.driver.find_element(By.XPATH,add_to_cart_location).click()

    @allure.step("Clicking on 'add to cart' button")
    def clicking_black_cart_button(self,add_to_cart_location):
        self.logs.info(f"Clicking on 'add to cart' button")
        self.driver.find_element(By.XPATH,add_to_cart_location).click()

    @allure.step("Adding product to cart from product page")
    def clicking_product_page(self,product_page_location):
        self.logs.info(f"going to product page")
        self.driver.find_element(By.XPATH,product_page_location).click()

    @allure.step("Validating the cart")
    def verify_the_empty_cart(self,black_cart_info,empty_cart_message,success_prompt_location,test_case_id):
        info = self.driver.find_element(By.XPATH,black_cart_info).text.split()
        time.sleep(1)
        success_prompt = self.driver.find_element(By.XPATH,success_prompt_location)
        self.logs.info(f"verifying the cart and visibility of the success prompt")
        if info == empty_cart_message and not(success_prompt.is_displayed()):
            self.logs.info(f"{test_case_id} Failed !")
            assert False
        else:
            self.logs.info(f"{test_case_id} Passed !")
            assert True

    @allure.step("Validating the cart")
    def verify_multiple_item_in_cart(self,black_cart_button_item_lists,test_case_id):
        self.logs.info(f"Verifying if we can add multiple items in cart")
        self.driver.execute_script("return document.querySelectorAll('table.table-striped tr')")
        items = self.driver.find_elements(By.XPATH, black_cart_button_item_lists)
        if len(items) == 2:
            self.logs.info(f"Test case {test_case_id} Passed !")
            assert True
        else:
            self.logs.info(f"Test case {test_case_id} Failed !{items}")
            assert False



