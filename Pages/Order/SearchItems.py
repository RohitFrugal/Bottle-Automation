import logging

from selenium import webdriver

from Utilities.utils import Utils
from Base.BaseTest import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class SearchItems(BaseClass):
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Order_module", logLevel=logging.WARNING)

    # Locators
    SEARCH_BAR = (By.XPATH, '//span[@class="ant-input-affix-wrapper search-field"]/input[@class="ant-input"]')


    # Methods
    def click_on_search(self, search_item):
        try:
            print(f"Search Item Input value : {search_item}")
            return self.wait.until(EC.visibility_of_element_located(self.SEARCH_BAR)).send_keys(search_item)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Search Bar : \n {str(e)}")



