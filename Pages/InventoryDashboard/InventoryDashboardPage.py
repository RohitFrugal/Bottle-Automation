import time
import logging
from selenium import webdriver
from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException




class InventoryDashboard(BaseClass):

    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Invent_Dashboard_module", logLevel=logging.DEBUG)

    # Locators

    INVENT_DASHBOARD_TAB = (By.XPATH, "//div[@class='menus']/div//a[contains(@id, 'InventoryDashboardMenu')]")
    TITLE = (By.XPATH, "//h1[contains(text(), 'DASHBOARD')]")

    IN_STOCK = (By.XPATH, "//div/div[2]/div[1]/div/div/div/div[1]/h3")
    ALARMING_STOCK = (By.XPATH, "//div/div[2]/div[2]/div/div/div/div[1]/h3")
    OUT_OF_STOCK = (By.XPATH, "//div/div[2]/div[3]/div/div/div/div[1]/h3")

    OUT_OF_STOCK_LIST = (By.XPATH, "(//div[@class='ant-col']/h5[@class='ant-typography dashboard-list-more'])[2]")
    OUT_OF_STOCK_LIST_SHOW_MORE = (By.XPATH, "(//div[@class='showmore'])[1]/a[@class='ant-typography']")
    OUT_OF_STOCK_LIST_ITEMS = (By.XPATH, "((//div[@class='ant-row'])[2] /div[2]/div/div/div[2]/div[@class='innerList']/div)")

    ALARMING_STOCK_LIST = (By.XPATH, "(//div[@class='ant-col']/h5[@class='ant-typography dashboard-list-more'])[4]")
    ALARMING_STOCK_LIST_SHOW_MORE = (By.XPATH, "(//div[@class='showmore'])[2]/a[@class='ant-typography']")
    ALARMING_STOCK_LIST_ITEMS = (By.XPATH, "(//div[@class='ant-row'])[3]//div[2]/div/div/div[2]/div[@class='innerList']/div")

    # CATEGORY_LIST_VIEWMORE = (By.XPATH, "(//h5[@class='ant-typography dashboard-list-more'][contains(text(), 'View Full Report')])[1]")
    CATEGORY_LIST_ITEM_NAME = (By.XPATH, "(//div[@class='ant-row dashboard-list-body'])[1]/div[2]/h5/a")
    CATEGORY_LIST_ITEM_QUANTITY = (By.XPATH, "(//div[@class='ant-row dashboard-list-body'])[1]/div[3]/h5")

    VENDOR_LIST_VIEWMORE = (By.XPATH, "(//h5[@class='ant-typography dashboard-list-more'][contains(text(), 'View Full Report')])[2]")
    VENDOR_LIST_NAME = (By.XPATH, "(//div[@class='ant-row dashboard-list-body'])[4]/div[2]/h5/a")
    VENDOR_LIST_NUMBER = (By.XPATH, "(//div[@class='ant-row dashboard-list-body'])[4]/div[3]/h5")

    INVENTORY_ITEM_NAME = (By.XPATH, "//div[@class='ant-space-item']/h5")
    INVENTORY_ITEM_QUANTITY = (By.XPATH, "//span[@class='material_item_quantity material_item_quantity__color_green']/div/div/span")

    # VENDOR_SEARCH_BAR = (By.XPATH, "//span[@class='ant-input-wrapper ant-input-group']/input")

    VENDOR_NAME = (By.XPATH, "(//div[@class='ant-row'])[3]/h2")
    VENDOR_NUMBER = (By.XPATH, "(//span[@class='ant-descriptions-item-content'])[1]")

    # Methods
    def click_on_inventDashboard(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.INVENT_DASHBOARD_TAB)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Navigation to Inventory Dashboard : \n {str(e)}")

    def getTitle(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.TITLE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to get Inventory Title : \n {str(e)}")

    def fetch_InStock(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.IN_STOCK)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Inventory In stock Items : \n {str(e)}")

    def fetch_AlarmingStock(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ALARMING_STOCK)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch alarming Stock Items : \n {str(e)}")

    def fetch_OutOfStock(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.OUT_OF_STOCK)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Out of Stock Items : \n {str(e)}")

    def fetch_OutOfStock_list(self):
        try:
            ItemList = self.wait.until(EC.visibility_of_element_located(self.OUT_OF_STOCK_LIST)).text
            return ItemList.split(": ")[-1]
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch out of Stock List : \n {str(e)}")

    def fetch_AlarmingStock_list(self):
        try:
            ItemList = self.wait.until(EC.visibility_of_element_located(self.ALARMING_STOCK_LIST)).text
            return ItemList.split(": ")[-1]
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch alarming Stock List : \n {str(e)}")

    def click_on_showMore_OutOfStock(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.OUT_OF_STOCK_LIST_SHOW_MORE)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Click on Show more : \n {str(e)}")

    def click_on_showMore_AlarmingStock(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ALARMING_STOCK_LIST_SHOW_MORE)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Click on Show more : \n {str(e)}")

    def check_outOfStockList(self):
        try:
            list_of_items = self.driver.find_elements(*self.OUT_OF_STOCK_LIST_ITEMS)
            count = len(list_of_items)
            print(f"Count of OUT OF STOCK Items  : {count}")
            return str(count)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to check Out of Stock List  : \n {str(e)}")

    def check_alarmingStock(self):
        try:
            list_of_items = self.driver.find_elements(*self.ALARMING_STOCK_LIST_ITEMS)
            count = len(list_of_items)
            print(f"Count of ALARMING STOCK Items  : {count}")
            return str(count)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to check Alarming Stock List : \n {str(e)}")



    def get_category_details(self):
        try:
            categoryDetails = []
            categoryDetails.append(self.wait.until(EC.visibility_of_element_located(self.CATEGORY_LIST_ITEM_NAME)).text)
            categoryDetails.append(self.wait.until(EC.visibility_of_element_located(self.CATEGORY_LIST_ITEM_QUANTITY)).text)
            print(f"These are Category Details : {categoryDetails}")
            return categoryDetails
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to check Category Details : \n {str(e)}")

    def click_on_Category_viewmore(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CATEGORY_LIST_ITEM_NAME)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to click on Category Viewmore : \n {str(e)}")

    def get_vendor_details(self):
        try:
            vendorDetails = []
            vendorDetails.append(self.wait.until(EC.visibility_of_element_located(self.VENDOR_LIST_NAME)).text)
            vendorDetails.append(self.wait.until(EC.visibility_of_element_located(self.VENDOR_LIST_NUMBER)).text)
            return vendorDetails
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to check vendor details : \n {str(e)}")

    def click_on_Vendor_viewmore(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.VENDOR_LIST_NAME)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to click on Vendor Viewmore : \n {str(e)}")

    def get_inventory_item_details(self):
        try:
            inventory_detail = []
            time.sleep(2)
            inventory_detail.append(self.wait.until(EC.visibility_of_element_located(self.INVENTORY_ITEM_NAME)).text)
            inventory_detail.append(self.wait.until(EC.visibility_of_element_located(self.INVENTORY_ITEM_QUANTITY)).text)
            print(f"These are the Inventory details : {inventory_detail}")
            return inventory_detail
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to get Inventory item Details: \n {str(e)}")

    def get_vendorTab_details(self):
        try:
            vendor_details = []
            vendor_details.append(self.wait.until(EC.visibility_of_element_located(self.VENDOR_NAME)).text)
            vendor_details.append(self.wait.until(EC.visibility_of_element_located(self.VENDOR_NUMBER)).text)
            return vendor_details
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to get Vendor Tab Details : \n {str(e)}")
