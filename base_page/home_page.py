import time

from  selenium import webdriver
import pytest
from selenium.webdriver.common.by import By
from utilities.config_reader import Config
from utilities.logs_genrator import LogsGenrator

class HomePage:
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

    def Search_bar_validation_01(self,location):
        self.driver.find_element(By.XPATH,location).send_keys("Hello world")
        self.driver.find_element(By.XPATH,)








