import logging
import time

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
    ITEMSNAEM = (By.XPATH, '//*[@class="ant-select-item-option-content"]')
    LEATHER_PROFILE = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[2]/div/div[2]/div/div/div/div/span[1]')

    LEATHER_SIZE = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[1]/div[2]/div/div/div/div/div[1]/div[3]/div/div[2]/div/div/div/div/span[1]')

    HARDWARE_SELECTOR = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[1]/div[2]'
                                   '/div/div/div/div/div[1]/div[4]/div/div[2]/div/div/div/div/div/span[2]')
    HARDWARE = (By.XPATH, '//*[@id="rc_select_3"]')
    LINING = (By.XPATH, '//*[@id="rc_select_4"]')
    POLYFILL = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[1]/div[2]'
                          '/div/div/div/div/div[1]/div[6]/div/div[2]/div/div/div/div')

    # Fill Product details
    def selectProductName(self, productname):
        print(f"I'm in SelectProduct for Store")
        return self.HandleDropdown(self.PRODUCT_NAME, self.ITEMSNAEM, productname)

    def selectLeatherProfile(self, leatherProfile):
        print(f"I'm in selectLeatherProfile for Store")
        return self.HandleDropdown(self.LEATHER_PROFILE, self.ITEMSNAEM, leatherProfile)

    def selectLeatherSize(self, leatherSize):
        print(f"I'm in selectLeatherSize for Store")
        return self.HandleDropdown(self.LEATHER_SIZE, self.ITEMSNAEM, leatherSize)

    def selectHardware(self, hardware):
        print(f"I'm in selectHardware for Store")
        try:
            # self.wait.until(EC.visibility_of_element_located(self.HARDWARE_SELECTOR)).click()
            # time.sleep(4)
            # self.wait.until(EC.visibility_of_element_located(self.HARDWARE)).send_keys(hardware)
            # time.sleep(4)
            # return self.wait.until(EC.visibility_of_element_located(self.HARDWARE)).send_keys(Keys.ENTER)
            
            return self.searchDropdown(self.HARDWARE, self.ITEMSNAEM, hardware)
        except Exception as e:
            self.log.error(f"{str(e)} \n Error because of this. ")


    def selectLining(self, lining):
        print(f"I'm in selectLining")
        return self.searchDropdown(self.LINING, self.ITEMSNAEM, lining)

    def selectPolyfill(self, polyfill):
        print(f"I'm in selectPolyfill")
        return self.HandleDropdown(self.POLYFILL, self.ITEMSNAEM, polyfill)
