import time

import pytest
from selenium import webdriver
from selenium.common import NoSuchElementException
from selenium.webdriver.common.by import By

# driver  = webdriver.Chrome()
# driver.find_element(By.XPATH,)

class Cart:
    def __init__(self,driver):
        self.driver=driver

    def adding_to_cart_homepage(self,add_to_cart_location):
        self.driver.find_element(By.XPATH,add_to_cart_location).click()

    def adding_to_cart_product_page(self,add_to_cart_location):
        self.driver.find_element(By.XPATH,add_to_cart_location).click()

    def adding_to_cart_search_page(self,add_to_cart_location):
        self.driver.find_element(By.XPATH,add_to_cart_location).click()

    def clicking_black_cart_button(self,add_to_cart_location):
        self.driver.find_element(By.XPATH,add_to_cart_location).click()

    def clicking_product_page(self,product_page_location):
        self.driver.find_element(By.XPATH,product_page_location).click()

    def verify_the_empty_cart(self,black_cart_info,empty_cart_message):
        info = self.driver.find_element(By.XPATH,black_cart_info).text.split()
        if info == empty_cart_message:
            assert False
        else:
            assert True