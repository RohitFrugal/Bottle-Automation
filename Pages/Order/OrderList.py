import logging

from selenium import webdriver

from Utilities.utils import Utils
from Base.BaseTest import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class OrderList(BaseClass):
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.log = Utils.custom_logger(logLevel=logging.DEBUG)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    LATEST_CUSTOMER_ITEM = (By.XPATH, "//div[@class='ant-row customer-order__value']/div[@class='ant-col ant-col-sm-3']/h5")

    LATEST_STORE_ITEM = (By.XPATH, "//div[contains(@id, 'rc-tabs-0-panel-2') or contains(@id, 'rc-tabs-1-panel-2')]/div/div/div/div[@class='ant-col ant-col-sm-4']/h5")

    GOTO_ORDER_LIST = (By.XPATH, '//button[@class="ant-btn ant-btn-default cancel-btn btn"]/span')

    CUSTOMER_TAB = (By.XPATH, "//div[@class='ant-tabs-tab'] //div[contains(@id, 'rc-tabs-1-tab-1') or contains(@id, 'rc-tabs-2-tab-1')]")
    STORE_TAB = (By.XPATH, "//div[@class='ant-tabs-tab'] //div[contains(@id, 'rc-tabs-0-tab-2') or contains(@id, 'rc-tabs-1-tab-2') or contains(@id, 'rc-tabs-2-tab-2')]")
    def click_on_goto_order(self):
        return self.wait.until(EC.visibility_of_element_located(self.GOTO_ORDER_LIST)).click()

    def get_latest_customer_orderID(self):
        return self.wait.until(EC.visibility_of_element_located(self.LATEST_CUSTOMER_ITEM))

    def click_on_store(self):
        return self.wait.until(EC.visibility_of_element_located(self.STORE_TAB)).click()

    def click_on_customer(self):
        return self.wait.until(EC.visibility_of_element_located(self.CUSTOMER_TAB)).click()

    def get_latest_store_orderID(self):
        return self.wait.until(EC.visibility_of_element_located(self.LATEST_STORE_ITEM))
