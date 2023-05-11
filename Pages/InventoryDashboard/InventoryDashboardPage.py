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

    IN_STOCK = (By.XPATH, "//div/div[2]/div[1]/div/div/div/div[1]/h3")
    ALARMING_STOCK = (By.XPATH, "//div/div[2]/div[2]/div/div/div/div[1]/h3")
    OUT_OF_STOCK = (By.XPATH, "//div/div[2]/div[3]/div/div/div/div[1]/h3")

    OUT_OF_STOCK_LIST = (By.XPATH, "(//div[@class='ant-col']/h5[@class='ant-typography dashboard-list-more'])[2]")
    OUT_OF_STOCK_LIST_SHOW_MORE = (By.XPATH, "(//div[@class='showmore'])[1]/a[@class='ant-typography']")
    OUT_OF_STOCK_LIST_ITEMS = (By.XPATH, "((//div[@class='ant-row'])[2] /div[2]/div/div/div[2]/div[@class='innerList']/div)")

    ALARMING_STOCK_LIST = (By.XPATH, "(//div[@class='ant-col']/h5[@class='ant-typography dashboard-list-more'])[4]")
    ALARMING_STOCK_LIST_SHOW_MORE = (By.XPATH, "(//div[@class='showmore'])[2]/a[@class='ant-typography']")
    ALARMING_STOCK_LIST_ITEMS = (By.XPATH, "(//div[@class='ant-row'])[3]//div[2]/div/div/div[2]/div[@class='innerList']/div")

    CATEGORY_LIST_VIEWMORE = (By.XPATH, "(//h5[@class='ant-typography dashboard-list-more'][contains(text(), 'View Full Report')])[1]")
    CATEGORY_LIST_ITEM_NAME = (By.XPATH, "(//div[@class='ant-row dashboard-list-body'])[1]/div[2]/h5/a")
    CATEGORY_LIST_ITEM_QUANTITY = (By.XPATH, "(//div[@class='ant-row dashboard-list-body'])[1]/div[3]/h5")

    VENDOR_LIST_VIEWMORE = (By.XPATH, "(//h5[@class='ant-typography dashboard-list-more'][contains(text(), 'View Full Report')])[2]")
    VENDOR_LIST_NAME = (By.XPATH, "(//div[@class='ant-row dashboard-list-body'])[4]/div[2]/h5/a")
    VENDOR_LIST_NUMBER = (By.XPATH, "(//div[@class='ant-row dashboard-list-body'])[4]/div[3]/h5")

    INVENTORY_ITEM_NAME = (By.XPATH, "//div[@class='ant-space-item']/h5")
    INVENTORY_ITEM_QUANTITY = (By.XPATH, "//span[@class='material_item_quantity material_item_quantity__color_green']/div/div/span")

    # VENDOR_SEARCH_BAR = (By.XPATH, "//span[@class='ant-input-wrapper ant-input-group']/input")
    VENDOR_NAME = (By.XPATH, "//h5[@class='ant-typography']")
    VENDOR_NUMBER = (By.XPATH, "//td[@class='ant-table-cell'][3]")

    # Methods
    def click_on_inventDashboard(self):
        return self.wait.until(EC.visibility_of_element_located(self.INVENT_DASHBOARD_TAB)).click()

    def getTitle(self):
        return self.wait.until(EC.visibility_of_element_located(self.TITLE)).text

    def fetch_InStock(self):
        return self.wait.until(EC.visibility_of_element_located(self.IN_STOCK)).text

    def fetch_AlarmingStock(self):
        return self.wait.until(EC.visibility_of_element_located(self.ALARMING_STOCK)).text

    def fetch_OutOfStock(self):
        return self.wait.until(EC.visibility_of_element_located(self.OUT_OF_STOCK)).text

    def fetch_OutOfStock_list(self):
        ItemList = self.wait.until(EC.visibility_of_element_located(self.OUT_OF_STOCK_LIST)).text
        return ItemList.split(": ")[-1]

    def fetch_AlarmingStock_list(self):
        ItemList = self.wait.until(EC.visibility_of_element_located(self.ALARMING_STOCK_LIST)).text
        return ItemList.split(": ")[-1]

    def click_on_showMore_OutOfStock(self):
        return self.wait.until(EC.visibility_of_element_located(self.OUT_OF_STOCK_LIST_SHOW_MORE)).click()

    def click_on_showMore_AlarmingStock(self):
        return self.wait.until(EC.visibility_of_element_located(self.ALARMING_STOCK_LIST_SHOW_MORE)).click()

    def check_outOfStockList(self):
        list_of_items = self.driver.find_elements(*self.OUT_OF_STOCK_LIST_ITEMS)
        count = len(list_of_items)
        print(f"Count of OUT OF STOCK Items  : {count}")

    def check_alarmingStock(self):
        list_of_items = self.driver.find_elements(*self.ALARMING_STOCK_LIST_ITEMS)
        count = len(list_of_items)
        print(f"Count of ALARMING STOCK Items  : {count}")

    def get_category_details(self):
        categoryDetails = []
        categoryDetails.append(self.wait.until(EC.visibility_of_element_located(self.CATEGORY_LIST_ITEM_NAME)).text)
        categoryDetails.append(self.wait.until(EC.visibility_of_element_located(self.CATEGORY_LIST_ITEM_QUANTITY)).text)
        return categoryDetails

    def click_on_Category_viewmore(self):
        return self.wait.until(EC.visibility_of_element_located(self.CATEGORY_LIST_VIEWMORE)).click()

    def get_vendor_details(self):
        vendorDetails = []
        vendorDetails.append(self.wait.until(EC.visibility_of_element_located(self.VENDOR_LIST_NAME)).text)
        vendorDetails.append(self.wait.until(EC.visibility_of_element_located(self.VENDOR_LIST_NUMBER)).text)
        return vendorDetails

    def click_on_Vendor_viewmore(self):
        return self.wait.until(EC.visibility_of_element_located(self.VENDOR_LIST_VIEWMORE)).click()

    def get_inventory_item_details(self):
        inventory_detail = []
        inventory_detail.append(self.wait.until(EC.visibility_of_element_located(self.INVENTORY_ITEM_NAME)).text)
        inventory_detail.append(self.wait.until(EC.visibility_of_element_located(self.INVENTORY_ITEM_QUANTITY)).text)
        return inventory_detail

    def get_vendorTab_details(self):
        vendor_details = []

        vendor_details.append(self.wait.until(EC.visibility_of_element_located(self.VENDOR_NAME)).text)
        vendor_details.append(self.wait.until(EC.visibility_of_element_located(self.VENDOR_NUMBER)).text)
        return vendor_details
