import allure
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from utilities.logs_genrator import LogsGenrator

class WishList:
    log = LogsGenrator.logs_gen()
    def __init__(self,driver):
        self.driver=driver

    @allure.step("Clicking wishlist button from the product catalog on homepage")
    def click_add_wish_list_button_product(self,product_wishlist_button_xpath):
        self.log.info("[+] -> clicking on the add to wishlist button from homepage product catalog")
        self.driver.find_element(By.XPATH,product_wishlist_button_xpath).click()

    @allure.step("verifying the Wishlist feature ")
    def validating_wishlist(self,wishlist_info_xpath,empty_wishlist_info,test_case_id,test_case_nature):
        info = self.driver.find_element(By.XPATH,wishlist_info_xpath).text
        if '+' == test_case_nature:
            if info != empty_wishlist_info:
                self.log.info(f"[+] -> {test_case_id} Passed: wishlist is not empty upon clicking add to wishlist from product catalog")
                assert True
            else:
                self.log.info(f"[+] -> {test_case_id} Failed ! : wishlist empty despite adding the product to wishlist from homepage")
                self.driver.save_screenshot(fr'C:\Users\pranj\OneDrive\Desktop\Automation_Project_OpenCart\screenshots\{test_case_id}.png')
                allure.attach(self.driver.get_screenshot_as_png(),name=f"{test_case_id} Screenshot",attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"[+] -> {test_case_id} Failed ! :- Wish List is empty despite adding the product to wishlist {info}")

        elif '-' == test_case_nature:
            if info == empty_wishlist_info:
                self.log.info(f"[+] -> {test_case_id} Passed: wishlist is empty when the new user access the homepage")
                assert True
            else:
                self.log.info(f"[+] -> {test_case_id} Passed: wishlist is not upon clicking add to wishlist from product catalog: {info} != {empty_wishlist_info}")
                self.driver.save_screenshot(fr'C:\Users\pranj\OneDrive\Desktop\Automation_Project_OpenCart\screenshots\{test_case_id}.png')
                allure.attach(self.driver.get_screenshot_as_png(), name=f"{test_case_id} Screenshot",attachment_type=allure.attachment_type.PNG)
                raise AssertionError(f"[+] -> {test_case_id} Failed ! :- Wishlist should be empty but it contains an: {info}")
        else:
            raise AssertionError("Invalid test case nature")