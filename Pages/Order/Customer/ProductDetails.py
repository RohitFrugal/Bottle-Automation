import logging
import time

from Utilities.utils import Utils
from selenium.webdriver import Keys
from Pages.Order.OrderPage import OrderPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class ProductDetails(OrderPage):
    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(logLevel=logging.DEBUG)

    PRODUCT_NAME = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div/span[1]')
    LEATHER_PROFILE = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/span[1]')
    LEATHER_SIZE = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[3]/div/div[2]/div/div/div/div/span[1]')
    HARDWARE = (By.XPATH, "//*[@class='ant-select-selection-search']/input[contains(@id, 'rc_select_3') or contains(@id, 'rc_select_13')]")
    LINING = (By.XPATH, '//*[@class="ant-select-selection-search"]//input[contains(@id, "rc_select_4") or contains(@id, "rc_select_14")]')
    POLYFILL = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[2]/div[2]/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div/div/div')
    RIB = (By.ID, 'rib')
    ITEMSNAEM = (By.XPATH, '//*[@class="ant-select-item-option-content"]')

    # Fill Product details
    def selectProductName(self, productname):
        self.log.info(f"I'm in Select Product")
        return self.HandleDropdown(self.PRODUCT_NAME, self.ITEMSNAEM, productname)

    def selectLeatherProfile(self, leatherProfile):
        self.log.info(f"I'm in select Leather Profile")
        return self.HandleDropdown(self.LEATHER_PROFILE, self.ITEMSNAEM, leatherProfile)

    def selectLeatherSize(self, leatherSize):
        print(f"I'm in select Leather Size")
        return self.HandleDropdown(self.LEATHER_SIZE, self.ITEMSNAEM, leatherSize)

    def selectHardware(self, hardware):
        self.log.info(f"I'm in select Hardware")
        self.wait.until(EC.visibility_of_element_located(self.HARDWARE)).send_keys(hardware)
        return self.wait.until(EC.visibility_of_element_located(self.HARDWARE)).send_keys(Keys.ENTER)


    def selectLining(self, lining):
        self.log.info(f"I'm in select Lining")
        self.wait.until(EC.visibility_of_element_located(self.LINING)).send_keys(lining)
        return self.wait.until(EC.visibility_of_element_located(self.LINING)).send_keys(Keys.ENTER)

    def selectPolyfill(self, polyfill):
        self.log.info(f"I'm in select Polyfill")
        return self.HandleDropdown(self.POLYFILL, self.ITEMSNAEM, polyfill)
