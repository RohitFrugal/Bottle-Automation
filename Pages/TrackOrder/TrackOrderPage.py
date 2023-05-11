import logging

from selenium import webdriver

from Utilities.utils import Utils
from Base.BaseTest import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TrackOrderPage(BaseClass):

    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.log = Utils.custom_logger(logLevel=logging.DEBUG)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)


    # Locator

    TrackOrderTab = (By.XPATH, "(//a[@id ='TrackOrderMenu'])[1]")
    InputBox = (By.XPATH, "//input[@class='ant-input order-option__button_1 btn track_order-btn']")
    NextButton = (By.XPATH, "//div[@class='ant-row']/button[@class='ant-btn ant-btn-default']")
    Factory_Title = (By.XPATH, "//span [contains(text(), 'Factory')]")

    # Methods
    def click_on_TrackOrder(self):
        return self.wait.until(EC.visibility_of_element_located(self.TrackOrderTab)).click()


    def sendOrderID(self, orderID):
        return self.wait.until(EC.visibility_of_element_located(self.InputBox)).send_keys(orderID)

    def clickOnNext(self):
        return self.wait.until(EC.visibility_of_element_located(self.NextButton)).click()

    def getFactoryTitle(self):
        return self.wait.until(EC.visibility_of_element_located(self.Factory_Title)).text

