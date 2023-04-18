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
    Total_User = (By.XPATH, "//*[@id='root']/section/main/div/div/div[2]/div/div[1]/div/div/div/div[1]/h1")
    Total_Order = (By.XPATH, '//*[@id="root"]/section/main/div/div/div[2]/div/div[2]/div/div/div/div[1]/h1')
    Total_Sales = (By.XPATH, '//*[@id="root"]/section/main/div/div/div[2]/div/div[3]/div/div/div/div[1]/h1')
    Total_Pending = (By.XPATH, '//*[@id="root"]/section/main/div/div/div[2]/div/div[4]/div/div/div/div[1]/h1')

    # Mid-Sections
    Active_User = (By.XPATH, '//*[@id="root"]/section/main/div/div/div[3]/div/div[2]/div[1]/div/div/div[1]/div[2]/h5')
    Inactive_User = (By.XPATH, '//*[@id="root"]/section/main/div/div/div[3]/div/div[2]/div[1]/div/div/div[2]/div[2]/h5')

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
