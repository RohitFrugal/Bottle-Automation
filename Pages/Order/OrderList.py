import logging

from selenium import webdriver

from Utilities.utils import Utils
from Base.BaseTest import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException



class OrderList(BaseClass):
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.log = Utils.custom_logger(module_name="Order_module", logLevel=logging.WARNING)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    LATEST_CUSTOMER_ITEM = (By.XPATH, "//div[@class='ant-row customer-order__value']/div[@class='ant-col ant-col-sm-3']/h5")

    LATEST_STORE_ITEM = (By.XPATH, "//div[contains(@id, 'rc-tabs-0-panel-2') or contains(@id, 'rc-tabs-1-panel-2')]/div/div/div/div[@class='ant-col ant-col-sm-4']/h5")

    GOTO_ORDER_LIST = (By.XPATH, '//button[@class="ant-btn ant-btn-default cancel-btn btn"]/span')

    CUSTOMER_TAB = (By.XPATH, "//div[@class='ant-tabs-tab'] //div[contains(@id, 'rc-tabs-0-tab-1') or contains(@id, 'rc-tabs-1-tab-1') or contains(@id, 'rc-tabs-2-tab-1')]")
    STORE_TAB = (By.XPATH, "//div[@class='ant-tabs-tab'] //div[contains(@id, 'rc-tabs-0-tab-2') or contains(@id, 'rc-tabs-1-tab-2') or contains(@id, 'rc-tabs-2-tab-2')]")

    HEADER_TEXT = (By.XPATH, '//h2[contains(text(), "ORDER DETAILS")]')

    USER_INFO = (By.XPATH, '//div[@class="ant-tabs-tab"]/div[contains(@id, "rc-tabs-0-tab-user-info")]')
    SIZE = (By.XPATH, '//div[@class="ant-tabs-tab"]/div[contains(@id, "rc-tabs-0-tab-sizing")]')
    PAYMENT = (By.XPATH, '//div[@class="ant-tabs-tab"]/div[contains(@id, "rc-tabs-0-tab-payment")]')
    REMARKS = (By.XPATH, '//div[@class="ant-tabs-tab"]/div[contains(@id, "rc-tabs-0-tab-remarks")]')

    # Order Card Detail
    ORDER_ID = (By.XPATH, "//div[@class='ant-row']/div[@class='ant-col']/h3")

    PRODUCT_NAME = (By.XPATH, "//div[@class='ant-card-body']/div[3]/div[1]/h3")
    LEATHER_PROFILE = (By.XPATH, "//div[@class='ant-card-body']/div[3]/div[2]/h3")
    HARDWARE = (By.XPATH, "//div[@class='ant-card-body']/div[4]/div[1]/h3")
    LINING = (By.XPATH, "//div[@class='ant-card-body']/div[4]/div[2]/h3")
    POLYFILL = (By.XPATH, "//div[@class='ant-card-body']/div[5]/div[1]/h3")

    # Methods
    def click_on_goto_order(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.GOTO_ORDER_LIST)).click()
        except (NoSuchElementException, TimeoutException, Exception)as e:
            self.log.error(f"Couldn't find the Element for Navigation to Order List : \n {str(e)}")

    def get_latest_customer_orderID(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.LATEST_CUSTOMER_ITEM))
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Latest Customer ID : \n {str(e)}")

    def click_on_store(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.STORE_TAB)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Navigation to Store : \n {str(e)}")

    def click_on_customer(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CUSTOMER_TAB)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Navigation to Customer  : \n {str(e)}")

    def get_latest_store_orderID(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.LATEST_STORE_ITEM))
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Latest Store ID : \n {str(e)}")

    def header_text_verification(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.HEADER_TEXT)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Header Text : \n {str(e)}")

    def get_order_id(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ORDER_ID)).text
        except Exception as e:
            self.log.error(f"Failed to locate the Order Id {str(e)}")

    def get_product_name(self):
        try:
            productname = self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME)).text
            return productname
        except Exception as e:
            self.log.error(f"Failed to locate Product name {str(e)}")

    def get_leather_profile(self):
        try:
            leatherProfile = self.wait.until(EC.visibility_of_element_located(self.LEATHER_PROFILE)).text
            return leatherProfile
        except Exception as e:
            self.log.error(f"Failed to locate Leather Profile {str(e)}")

    def get_hardware(self):
        try:
            hardware = self.wait.until(EC.visibility_of_element_located(self.HARDWARE)).text
            return hardware
        except Exception as e:
            self.log.error(f"Failed to locate Hardware {str(e)}")

    def get_lining(self):
        try:
            lining = self.wait.until(EC.visibility_of_element_located(self.LINING)).text
            return lining
        except Exception as e:
            self.log.error(f"Failed to locate Lining {str(e)}")

    def get_polyfill(self):
        try:
            polyfill = self.wait.until(EC.visibility_of_element_located(self.POLYFILL)).text
            return polyfill
        except Exception as e:
            self.log.error(f"Failed to locate polyfill {str(e)}")
