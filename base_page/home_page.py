import time

from  selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from utilities.config_reader import Config
from utilities.logs_genrator import LogsGenrator

log = LogsGenrator.logs_gen()
class HomepageTitleVerification:

    log = LogsGenrator.logs_gen()

    def __init__(self,driver):
        self.driver = driver

    def open_home_page(self,url):
        self.log.info("[+] -> Opening the Home page")
        self.driver.get(url)
        self.log.info("[+] -> Maximizing the windows")
        self.driver.maximize_window()

    def home_page_title_verification(self):
        self.log.info("[+] -> Verifying the title")
        if self.driver.title == "Your Store":
            self.log.info("[+] -> Title verification passed")
            assert True
            self.driver.quit()
        else:
            self.log.info("[+] -> Title verification failed")
            assert False
            self.driver.quit()



class SearchBar:

    log = LogsGenrator.logs_gen()

    def __init__(self,driver):
        self.driver = driver

    def open_home_page(self,url):
        self.log.info("[+] -> Opening the Home page")
        self.driver.get(url)
        self.log.info("[+] -> Maximizing the windows")
        self.driver.maximize_window()


    def Search_bar_test_data_002(self,location,query):
        self.driver.find_element(By.XPATH,location).send_keys(query)
        self.log.info("[+] -> Entering the test data for TC_002")

    def ClickingSearchButton(self,button):
        self.driver.find_element(By.XPATH,button).click()
        self.log.info("[+] -> Clicking the search button")

    def Search_bar_validation_002(self):
        if 'iPhone' in self.driver.page_source:
            self.log.info("[+] -> TC_002 Passed")
            self.driver.quit()
            assert True
        else:
            self.log.info("[+] -> TC_002 Failed")
            self.driver.quit()
            assert False











