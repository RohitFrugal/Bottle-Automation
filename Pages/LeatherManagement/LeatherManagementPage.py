import logging
from selenium import webdriver
from Utilities.utils import Utils
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException





class LeatherManagementPage:
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Leather_management", logLevel=logging.WARNING)

    # Methods
    LEATHER_TAB = (By.ID, "LeatherManagementMenu")
    HEADER_TEXT = (By.XPATH, "//h1[@class='ant-typography product-name']")

    def navigate(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.LEATHER_TAB)).click()
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to locate Nav Item : {str(e)}")

    def get_headerText(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.HEADER_TEXT)).text
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to fetch the title Text : {str(e)}")

