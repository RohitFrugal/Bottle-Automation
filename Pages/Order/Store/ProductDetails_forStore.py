import logging

from Utilities.utils import Utils
from selenium.webdriver import Keys
from Pages.Order.OrderPage import OrderPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class ProductDetailsForStore(OrderPage):
    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__(driver)
        self.log = Utils.custom_logger(logLevel=logging.DEBUG)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    PRODUCT_NAME = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div/span[1]')
    LEATHER_PROFILE = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/span[1]')
    LEATHER_SIZE = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div/div[2]/div/div/div/div/span[1]')
    HARDWARE = (By.XPATH, "//*[@class='ant-select-selection-search']/input[contains(@id, 'rc_select_3') or contains(@id, 'rc_select_13')]")
    LINING = (By.XPATH, '//*[@class="ant-select-selection-search"]//input[contains(@id, "rc_select_4") or contains(@id, "rc_select_14")]')
    POLYFILL = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div/div/div')
    ITEMSNAME = (By.XPATH, '//*[@class="ant-select-item-option-content"]')


    # Fill Product details
    def selectProductName(self, productname):
        print(f"I'm in Select Product for Store")
        return self.HandleDropdown(self.PRODUCT_NAME, self.ITEMSNAME, productname)

    def selectLeatherProfile(self, leatherProfile):
        print(f"I'm in select Leather Profile for Store")
        return self.HandleDropdown(self.LEATHER_PROFILE, self.ITEMSNAME, leatherProfile)

    def selectLeatherSize(self, leatherSize):
        print(f"I'm in select Leather Size for Store")
        return self.HandleDropdown(self.LEATHER_SIZE, self.ITEMSNAME, leatherSize)

    def selectHardware(self, hardware):
        print(f"I'm in select Hardware for Store")
        self.wait.until(EC.visibility_of_element_located(self.HARDWARE)).send_keys(hardware)
        return self.wait.until(EC.visibility_of_element_located(self.HARDWARE)).send_keys(Keys.ENTER)


    def selectLining(self, lining):
        print(f"I'm in select Lining")
        self.wait.until(EC.visibility_of_element_located(self.LINING)).send_keys(lining)
        return self.wait.until(EC.visibility_of_element_located(self.LINING)).send_keys(Keys.ENTER)

    def selectPolyfill(self, polyfill):
        print(f"I'm in selectPolyfill")
        return self.HandleDropdown(self.POLYFILL, self.ITEMSNAME, polyfill)
