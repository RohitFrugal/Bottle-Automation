import time
import logging
from selenium import webdriver
from Utilities.utils import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException



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
    # TODO - Check the total number of order made by navigating to Order section
    #  and getting the number fo Items from the list of order and pages,

    GET_LAST_PAGE_TEXT_CUSTOMER = (By.XPATH, "(//ul[@class='ant-pagination']/li[8])[1]")
    GET_LAST_PAGE_TEXT_STORE = (By.XPATH, "(//ul[@class='ant-pagination']/li[8])[2]")

    NUMBER_OF_ELEMENTS_PER_PAGE_CUSTOMER = (By.XPATH, "(//div[@class='ant-card-body'])[3]//div[@class='ant-row customer-order__value']")
    NUMBER_OF_ELEMENTS_PER_PAGE_STORE = (By.XPATH, "(//div[@class='ant-card-body'])[4]//div[@class='ant-row customer-order__value']")


    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Dashboard_module", logLevel=logging.WARNING)

    # Top Tile
    def verify_total_user(self):
        try:
            time.sleep(5)
            total_user = self.driver.find_element(*self.Total_User).text
            print(total_user)
            return total_user
        except (NoSuchElementException, TimeoutException, Exception, AssertionError)as e:
            self.log.error(f"Couldn't find the Element for Total User : \n {str(e)}")

    def verify_total_order(self):
        try:
            time.sleep(5)
            total_order = self.driver.find_element(*self.Total_Order).text
            return total_order
        except (NoSuchElementException, TimeoutException, Exception, AssertionError)as e:
            self.log.error(f"Couldn't find the Element for Total Order : \n {str(e)}")

    def verify_total_sales(self):
        try:
            time.sleep(5)
            total_sales = self.driver.find_element(*self.Total_Sales).text
            return total_sales
        except (NoSuchElementException, TimeoutException, Exception, AssertionError)as e:
            self.log.error(f"Couldn't find the Element for Total Sales : \n {str(e)}")

    def verify_pending(self):
        try:
            time.sleep(5)
            total_pending = self.driver.find_element(*self.Total_Pending).text
            return total_pending
        except (NoSuchElementException, TimeoutException, Exception, AssertionError)as e:
            self.log.error(f"Couldn't find the Element for Total Pending Orders  : \n {str(e)}")


    # Mid-Sections
    def active_user(self):
        try:
            time.sleep(5)
            active_user = self.driver.find_element(*self.Active_User).text
            return active_user
        except (NoSuchElementException, TimeoutException, Exception, AssertionError)as e:
            self.log.error(f"Couldn't find the Element for Active User : \n {str(e)}")

    def inactive_user(self):
        try:
            time.sleep(5)
            inactive_user = self.driver.find_element(*self.Inactive_User).text
            return inactive_user
        except (NoSuchElementException, TimeoutException, Exception, AssertionError)as e:
            self.log.error(f"Couldn't find the Element for Inactive User : \n {str(e)}")

    def verify_sum_of_total_user(self):
        try:
            time.sleep(5)
            SumOfTotalUser = int(self.active_user()) + int(self.inactive_user())
            return str(SumOfTotalUser)
        except (NoSuchElementException, TimeoutException, Exception, AssertionError)as e:
            self.log.error(f"Couldn't fetch Data from the DOM for Sum of Total User : \n {str(e)}")

    def total_user(self):
        try:
            time.sleep(5)
            return str(int(self.active_user()) + int(self.inactive_user()))
        except (NoSuchElementException, TimeoutException, Exception, AssertionError)as e:
            self.log.error(f"Couldn't find the Element for List of user's : \n {str(e)}")

    def get_elements_perPage_Customer(self):
        try:
            # print("I'm here to get the elements present in each page for customer.")
            get_list_of_element = self.wait.until(EC.visibility_of_all_elements_located(self.NUMBER_OF_ELEMENTS_PER_PAGE_CUSTOMER))
            No_elements = len(get_list_of_element)
            # print(f"Number of Element in Page for customer : {No_elements}")
            return No_elements
        except (NoSuchElementException, TimeoutException, Exception, AssertionError)as e:
            self.log.error(f"Couldn't find the Element for  Recent Order : \n {str(e)}")

    def get_elements_perPage_Store(self):
        try:
            # print("I'm here to get the elements present in each page for store.")
            get_list_of_element = self.wait.until(EC.visibility_of_all_elements_located(self.NUMBER_OF_ELEMENTS_PER_PAGE_STORE))
            No_elements = len(get_list_of_element)
            # print(f"Number of Element in Page for Store : {No_elements}")
            return No_elements
        except (NoSuchElementException, TimeoutException, Exception, AssertionError)as e:
            self.log.error(f"Couldn't find the Element for  Recent Order : \n {str(e)}")

    def get_lastPage_customer(self):
        try:
            time.sleep(5)
            last_page_no = self.driver.find_element(*self.GET_LAST_PAGE_TEXT_CUSTOMER)
            last_page_number_text = last_page_no.text
            print(f"Number of Pages : {last_page_number_text}")
            last_page_no.click()
            return last_page_number_text
        except (NoSuchElementException, TimeoutException, Exception, AssertionError)as e:
            self.log.error(f"Couldn't find the Element for  Recent Order : \n {str(e)}")


    def get_lastPage_store(self):
        try:
            time.sleep(5)
            last_page_no = self.driver.find_element(*self.GET_LAST_PAGE_TEXT_STORE)
            last_page_number_text = last_page_no.text
            print(f"Number of Pages : {last_page_number_text}")
            last_page_no.click()
            return last_page_number_text
        except (NoSuchElementException, TimeoutException, Exception, AssertionError)as e:
            self.log.error(f"Couldn't find the Element for  Recent Order : \n {str(e)}")
