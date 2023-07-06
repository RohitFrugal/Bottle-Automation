import logging

from Utilities.utils import Utils
from selenium.webdriver import Keys
from Pages.Order.OrderPage import OrderPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class ProductDetailsForStore(OrderPage):
    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Order_module", logLevel=logging.WARNING)

    PRODUCT_NAME = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[1]/div/div[2]/div/div/div/div/span[1]')
    LEATHER_PROFILE = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/span[1]')
    LEATHER_SIZE = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div/div[2]/div/div/div/div/span[1]')
    HARDWARE = (By.XPATH, "//*[@class='ant-select-selection-search']/input[contains(@id, 'rc_select_3') or contains(@id, 'rc_select_13')]")
    LINING = (By.XPATH, '//*[@class="ant-select-selection-search"]//input[contains(@id, "rc_select_4") or contains(@id, "rc_select_14")]')
    POLYFILL = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[6]/div/div[2]/div/div/div/div')
    ITEMSNAME = (By.XPATH, '//*[@class="ant-select-item-option-content"]')


    # Fill Product details
    def selectProductName(self, productname):
        try:
            print(f"I'm in Select Product for Store")
            return self.HandleDropdown(self.PRODUCT_NAME, self.ITEMSNAME, productname)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Selecting the Product : \n {str(e)}")


    def selectLeatherProfile(self, leatherProfile):
        try:
            print(f"I'm in select Leather Profile for Store")
            return self.HandleDropdown(self.LEATHER_PROFILE, self.ITEMSNAME, leatherProfile)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Selecting Leather Profile : \n {str(e)}")

    def selectLeatherSize(self, leatherSize):
        try:
            print(f"I'm in select Leather Size for Store")
            return self.HandleDropdown(self.LEATHER_SIZE, self.ITEMSNAME, leatherSize)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Selecting Leather Size : \n {str(e)}")


    def selectHardware(self, hardware):
        try:
            print(f"I'm in select Hardware for Store")
            self.wait.until(EC.visibility_of_element_located(self.HARDWARE)).send_keys(hardware)
            return self.wait.until(EC.visibility_of_element_located(self.HARDWARE)).send_keys(Keys.ENTER)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Selecting Hardware : \n {str(e)}")



    def selectLining(self, lining):
        try:
            print(f"I'm in select Lining")
            self.wait.until(EC.visibility_of_element_located(self.LINING)).send_keys(lining)
            return self.wait.until(EC.visibility_of_element_located(self.LINING)).send_keys(Keys.ENTER)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Selecting Lining : \n {str(e)}")


    def selectPolyfill(self, polyfill):
        try:
            print(f"I'm in selectPolyfill")
            return self.HandleDropdown(self.POLYFILL, self.ITEMSNAME, polyfill)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Selecting Polyfill : \n {str(e)}")

