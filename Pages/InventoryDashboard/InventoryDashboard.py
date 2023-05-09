import logging

from selenium import webdriver

from Utilities.utils import Utils
from Base.BaseTest import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class InventoryDashboard(BaseClass):

    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.log = Utils.custom_logger(logLevel=logging.DEBUG)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators

    INVENT_DASHBOARD_TAB = (By.XPATH, "//div[@class='menus']/div//a[contains(@id, 'InventoryDashboardMenu')]")
    TITLE = (By.XPATH, "//h1[contains(text(), 'DASHBOARD')]")

    # Methods
    def click_on_inventDashboard(self):
        return self.wait.until(EC.visibility_of_element_located(self.INVENT_DASHBOARD_TAB)).click()

    def getTitle(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITLE)).text
