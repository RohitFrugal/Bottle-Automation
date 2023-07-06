import logging

from selenium import webdriver

from Utilities.utils import Utils
from Base.BaseTest import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class TrackOrderPage(BaseClass):

    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="TrackOrder_module", logLevel=logging.WARNING)


    # Locator

    TrackOrderTab = (By.XPATH, "(//a[@id ='TrackOrderMenu'])[1]")
    InputBox = (By.XPATH, "//input[@class='ant-input order-option__button_1 btn track_order-btn']")
    NextButton = (By.XPATH, "//div[@class='ant-row']/button[@class='ant-btn ant-btn-default']")
    Factory_Title = (By.XPATH, "//span [contains(text(), 'Factory')]")
    checkFactory = (By.XPATH, "//div[@class='ant-col table-content ant-col-sm-6']/div[contains(@class, 'unActive')]")


    # Methods
    def click_on_TrackOrder(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.TrackOrderTab)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Navigation to Track Order  : \n {str(e)}")


    def sendOrderID(self, orderID):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.InputBox)).send_keys(orderID)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Input Order ID : \n {str(e)}")

    def clickOnNext(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.NextButton)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Search Order ID : \n {str(e)}")

    def getFactoryTitle(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.Factory_Title)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to get Factory Title : \n {str(e)}")

    def getCheckFactory(self):
        try:
            self.driver.find_element(*self.checkFactory)
            return True
        except NoSuchElementException as e:
            self.log.error(f"Couldn't find the Element to Check Factory Check: \n {str(e)}")
            return False
