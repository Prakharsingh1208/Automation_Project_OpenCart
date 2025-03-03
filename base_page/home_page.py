from selenium.webdriver.common.by import By
from selenium.webdriver.support import select
from selenium.webdriver.support.select import Select

from utilities.logs_genrator import LogsGenrator

log = LogsGenrator.logs_gen()
class HomepageTitleVerification:

    log = LogsGenrator.logs_gen()

    def __init__(self,driver):
        self.driver = driver

    def open_home_page(self,url):
        self.log.info(f"[+] -> Opening the Home page {url}")
        self.driver.get(url)
        self.log.info("[+] -> Maximizing the windows")
        self.driver.maximize_window()

    def home_page_title_verification(self,title,testCaseID):
        self.log.info("[+] -> Verifying the title")
        if self.driver.title == title:
            self.log.info(f"[+] -> {testCaseID} Passed")
            assert True
            self.driver.quit()
        else:
            self.log.info(f"[+] -> {testCaseID} Failed")
            assert False
            self.driver.quit()



class SearchBar:

    log = LogsGenrator.logs_gen()

    def __init__(self,driver):
        self.driver = driver

    def open_home_page(self,url):
        self.log.info(f"[+] -> Opening the Home page {url}")
        self.driver.get(url)
        self.log.info("[+] -> Maximizing the windows")
        self.driver.maximize_window()


    def Search_bar_test_data_entery(self,location,query):
        self.driver.find_element(By.XPATH,location).send_keys(query)
        self.log.info(f"[+] -> Entering the test data '{query}'")

    def ClickingSearchButton(self,button):
        self.driver.find_element(By.XPATH,button).click()
        self.log.info("[+] -> Clicking the search button")

    def Search_bar_validation_valid_test_data(self,ValidQuery,testCaseID):
        self.log.info(f"[+] -> Validating {testCaseID}")
        if 'iPhone' in self.driver.page_source:
            self.log.info(f"[+] -> {testCaseID} Passed")
            self.driver.quit()
            assert True
        else:
            self.log.info(f"[+] -> {testCaseID} Failed")
            self.driver.save_screenshot(fr'C:\Users\pranj\OneDrive\Desktop\Automation_Project_OpenCart\screenshots\{testCaseID}.png')
            self.driver.quit()
            assert False


    def Search_bar_validation_invalid_test_data(self,InvalidQueryResponse,TestCaseID):
        self.log.info(f"[+] -> Validating {TestCaseID}")
        if InvalidQueryResponse in self.driver.page_source:
            self.log.info(f"[+] -> {TestCaseID} Passed")
            self.driver.quit()
            assert True
        else:
            self.log.info(f"[+] -> {TestCaseID} Failed")
            self.driver.save_screenshot(fr'C:\Users\pranj\OneDrive\Desktop\Automation_Project_OpenCart\screenshots\{TestCaseID}.png')
            self.driver.quit()
            assert False

class Currency:
    log = LogsGenrator.logs_gen()

    def __init__(self,driver):
        self.driver = driver

    def open_home_page(self,url):
        self.log.info(f"[+] -> Opening the Home page {url}")
        self.driver.get(url)
        self.log.info("[+] -> Maximizing the windows")
        self.driver.maximize_window()

    def ClickCurrencyButton(self,CurrencyButtonLocation):
        self.log.info(f"[+] -> Clicking Currency button")
        self.driver.find_element(By.XPATH,CurrencyButtonLocation).click()

    def SelectingCurrency(self,location,value):
        self.log.info(f"[+] -> Selecting Currency '{value}'")
        self.driver.find_element(By.XPATH,location).click()

    def CurrencyValidation(self,DemoProductPriceLocation,CurrencySymbole,TestCaseID):
        price = self.driver.find_element(By.XPATH,DemoProductPriceLocation).text
        self.log.info(f"[+] -> Validating for currency {CurrencySymbole}")
        if CurrencySymbole in price:
            self.log.info(f"[+] -> {TestCaseID} Passed")
            self.driver.quit()
            assert True
        else:
            self.log.info(f"[+] -> {TestCaseID} Failed")
            self.driver.save_screenshot(fr'C:\Users\pranj\OneDrive\Desktop\Automation_Project_OpenCart\screenshots\{TestCaseID}.png')
            self.driver.quit()
            assert False










