import time
import logging
from selenium import webdriver
from Utilities.utils import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait



class DashboardPage:
    wait: WebDriverWait
    driver: webdriver

    # Locators
    # Top tile
    Total_User = (By.XPATH, "(//h1[@class='ant-typography'])[1]")
    Total_Order = (By.XPATH, "(//h1[@class='ant-typography'])[2]")
    Total_Sales = (By.XPATH, "(//h1[@class='ant-typography'])[3]")
    Total_Pending = (By.XPATH, "(//h1[@class='ant-typography'])[4]")

    # Mid-Sections
    Active_User = (By.XPATH, "(//h5[@class='ant-typography'])[1]")
    Inactive_User = (By.XPATH, "(//h5[@class='ant-typography'])[2]")

    # Verification Methods
    TOP_RECENT_ORDER = (By.XPATH, "(//a[@class='ant-typography'])[1]")

    # Initializing driver and logger.
    def __init__(self, driver):
        self.log = Utils.custom_logger(logLevel=logging.WARNING)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Top Tile
    def verify_total_user(self):
        time.sleep(5)
        total_user = self.driver.find_element(*self.Total_User).text
        return total_user

    # TODO --- Get the Real time data for the testing

    def verify_total_order(self):
        time.sleep(5)
        total_order = self.driver.find_element(*self.Total_Order).text
        return total_order

    def verify_total_sales(self):
        time.sleep(5)
        total_sales = self.driver.find_element(*self.Total_Sales).text
        return total_sales

    def verify_pending(self):
        time.sleep(5)
        total_pending = self.driver.find_element(*self.Total_Pending).text
        return total_pending



    # Mid-Sections
    def active_user(self):
        time.sleep(5)
        active_user = self.driver.find_element(*self.Active_User).text
        return active_user

    def inactive_user(self):
        time.sleep(5)
        inactive_user = self.driver.find_element(*self.Inactive_User).text
        return inactive_user

    def verify_sum_of_total_user(self):
        time.sleep(5)
        SumOfTotalUser = int(self.active_user()) + int(self.inactive_user())
        return str(SumOfTotalUser)

    def recent_top_order(self):
        time.sleep(5)
        top_recent_Order = self.driver.find_element(*self.TOP_RECENT_ORDER).text
        return top_recent_Order.strip("#")

    def total_user(self):
        time.sleep(2)
        return str(int(self.active_user()) + int(self.inactive_user()))
