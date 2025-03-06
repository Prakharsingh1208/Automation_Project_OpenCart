from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

from utilities.logs_genrator import LogsGenrator

log = LogsGenrator.logs_gen()
class HomepageTitleVerification:

    log = LogsGenrator.logs_gen()

    def __init__(self,driver):
        self.driver = driver

    def home_page_title_verification(self,title,testCaseID):
        self.log.info("[+] -> Verifying the title")
        try:
            if self.driver.title == title:
                self.log.info(f"[+] -> {testCaseID} Passed")
                assert True
            else:
                self.log.info(f"[+] -> {testCaseID} Failed")
                AssertionError(f"{testCaseID} Failed")
        finally:
            self.driver.quit()



class SearchBar:

    log = LogsGenrator.logs_gen()

    def __init__(self,driver):
        self.driver = driver

    def Search_bar_test_data_entery(self,location,query):
        self.driver.find_element(By.XPATH,location).send_keys(query)
        self.log.info(f"[+] -> Entering the test data '{query}'")

    def ClickingSearchButton(self,button):
        self.driver.find_element(By.XPATH,button).click()
        self.log.info("[+] -> Clicking the search button")

    def Search_bar_validation_valid_test_data(self,ValidQuery,testCaseID):
        self.log.info(f"[+] -> Validating {testCaseID}")
        try:
            if 'iPhone' in self.driver.page_source:
                self.log.info(f"[+] -> {testCaseID} Passed")
                assert True
            else:
                self.log.info(f"[+] -> {testCaseID} Failed")
                self.driver.save_screenshot(fr'C:\Users\pranj\OneDrive\Desktop\Automation_Project_OpenCart\screenshots\{testCaseID}.png')
                AssertionError(f"{testCaseID} Failed")
        finally:
            self.driver.quit()


    def Search_bar_validation_invalid_test_data(self,InvalidQueryResponse,TestCaseID):
        self.log.info(f"[+] -> Validating {TestCaseID}")
        try:
            if InvalidQueryResponse in self.driver.page_source:
                self.log.info(f"[+] -> {TestCaseID} Passed")
                assert True
            else:
                self.log.info(f"[+] -> {TestCaseID} Failed")
                self.driver.save_screenshot(fr'C:\Users\pranj\OneDrive\Desktop\Automation_Project_OpenCart\screenshots\{TestCaseID}.png')
                AssertionError(f"{TestCaseID} Failed")
        finally:
            self.driver.quit()

class Currency:
    log = LogsGenrator.logs_gen()

    def __init__(self,driver):
        self.driver = driver

    def ClickCurrencyButton(self,CurrencyButtonLocation):
        self.log.info(f"[+] -> Clicking Currency button")
        self.driver.find_element(By.XPATH,CurrencyButtonLocation).click()

    def SelectingCurrency(self,location,value):
        self.log.info(f"[+] -> Selecting Currency '{value}'")
        self.driver.find_element(By.XPATH,location).click()

    def CurrencyValidation(self,DemoProductPriceLocation,CurrencySymbole,TestCaseID):
        price = self.driver.find_element(By.XPATH,DemoProductPriceLocation).text
        self.log.info(f"[+] -> Validating for currency {CurrencySymbole}")
        try:
            if CurrencySymbole in price:
                self.log.info(f"[+] -> {TestCaseID} Passed")
                assert True
            else:
                self.log.info(f"[+] -> {TestCaseID} Failed")
                self.driver.save_screenshot(fr'C:\Users\pranj\OneDrive\Desktop\Automation_Project_OpenCart\screenshots\{TestCaseID}.png')
                AssertionError(f"{TestCaseID} Failed")
        finally:
            self.driver.quit()
class AddToCart:
    log = LogsGenrator.logs_gen()
    def __init__(self,driver):
        self.driver = driver

    def OpenHomePage(self,url):
        self.log.info(f"[+] -> Opening the Home page {url}")
        self.driver.get(url)
        self.log.info(f"[+] -> Maximizing Window")
        self.driver.maximize_window()

    def ClickAddtoCart(self,location):
        self.log.info(f"[+] -> Clicking Add to cart from product")
        self.driver.find_element(By.XPATH,location).click()

    def CartValidation(self,CartInfoLocation,EmptyCartMessage,testCaseID):
        self.log.info(f"[+] -> Validating Add to cart Button")
        cart_info = self.driver.find_element(By.XPATH,CartInfoLocation).text.strip()
        try:
            if EmptyCartMessage == cart_info and testCaseID == 'TC-010':
                self.log.error(
                    f"[+] -> {testCaseID} Failed: Cart is empty when it shouldn't be. Cart info: {cart_info}")
                raise AssertionError(f"Test case {testCaseID} failed: Expected non-empty cart, but cart is empty.")

            elif EmptyCartMessage == cart_info and testCaseID == 'TC-011':
                self.log.info(f"[+] -> {testCaseID} Passed: Cart is empty as expected. Cart info: {cart_info}")
                assert True

            elif EmptyCartMessage != cart_info and testCaseID == 'TC-011':
                self.log.error(
                    f"[+] -> {testCaseID} Failed: Cart should be empty, but it's not. Cart info: {cart_info}")
                raise AssertionError(f"Test case {testCaseID} failed: Expected empty cart({EmptyCartMessage}), but cart is not empty.")

            elif EmptyCartMessage != cart_info and testCaseID =='TC-010':
                self.log.info(f"[+] -> {testCaseID} Passed: Cart is correctly updated. Cart info: {cart_info}")
                assert True
            else:
                AssertionError("[!] -> Something unexpected happened")
        finally:
            self.driver.quit()








