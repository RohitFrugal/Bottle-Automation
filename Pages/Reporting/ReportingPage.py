import time
import logging
from selenium import webdriver

from Utilities.utils import Utils
from Base.BaseTest import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class ReportingPage(BaseClass):
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Report_module", logLevel=logging.DEBUG)

    # Locators

    REPORTING_TAB = (By.ID, "ReportingMenu")
    LANDING_PAGE_HEADER = (By.XPATH, "//h1[@class='ant-typography product-name']")
    SORT_SELECTOR = (By.XPATH, "(//div[@class='ant-select-selector'])[1]")
    DESCENDING_SELECTOR = (By.XPATH, "//div[@class='ant-select-item-option-content'][contains(text(), 'descending ')]")
    SEARCH_BAR = (By.XPATH, "//input[@class='ant-input']")

    PRODUCT_NAME = (By.XPATH, "//h4[@class='ant-typography']")
    RECEIVED_DATE = (By.XPATH, "//h5[@class='ant-typography']")
    VENDOR_NAME = (By.XPATH, "(//h5[@class='ant-typography'])[2]")

    VIEW_MORE = (By.XPATH, "//span[@class='anticon anticon-eye']")

    PRODUCT_TYPE_VIEW_MORE = (By.XPATH, "//div[@class='report-detail__title']/p")
    PRODUCT_NAME_VIEW_MORE = (By.XPATH, "//div[@class='report-detail__title']/h4")
    VENDOR_NAME_VIEW_MORE = (By.XPATH, "(//h4[@class='report-detail__content-value'])[1]")
    RECEIVED_DATE_VIEW_MORE = (By.XPATH, "(//h4[@class='report-detail__content-value'])[2]")
    COLOR_VIEW_MORE = (By.XPATH, "(//h4[@class='report-detail__content-value'])[3]")
    QUANTITY_VIEW_MORE = (By.XPATH, "(//h4[@class='report-detail__content-value'])[5]")
    PRICE_VIEW_MORE = (By.XPATH, "(//h4[@class='report-detail__content-value'])[6]")
    QUALITY_VIEW_MORE = (By.XPATH, "(//h4[@class='report-detail__content-value'])[7]")
    TRANSPORT_BY_VIEW_MORE = (By.XPATH, "(//h4[@class='report-detail__content-value'])[9]")
    PAYMENT_MODE_VIEW_MORE = (By.XPATH, "(//h4[@class='report-detail__content-value'])[10]")
    RECEIVED_BY_VIEW_MORE = (By.XPATH, "(//h4[@class='report-detail__content-value'])[11]")

    # Executions Methods
    def navigate(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.REPORTING_TAB)).click()
        except NoSuchElementException as e:
            self.log.error(f"Unable to find navigation menu for Report :\n {str(e)}")

    def getTitle(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.LANDING_PAGE_HEADER)).text
        except NoSuchElementException as e:
            self.log.error(f"Unable to find Header Title for Report :\n {str(e)}")

    def sort_vendor(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SORT_SELECTOR)).click()
            return self.wait.until(EC.visibility_of_element_located(self.DESCENDING_SELECTOR)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to sort the report : \n {str(e)}")

    def search_bar(self, searchItem):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SEARCH_BAR)).send_keys(searchItem)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Search Bar input : \n {str(e)}")

    # Validations outer List
    def get_reporting_name(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Validate Product Name: \n {str(e)}")

    def get_received_date(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.RECEIVED_DATE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Validate Received Date : \n {str(e)}")

    def get_vendor_name(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.VENDOR_NAME)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Validate Vendor Name : \n {str(e)}")

    def view_more(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.VIEW_MORE)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Click on view more : \n {str(e)}")

    # Validating view more

    def get_product_type_view_more(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_TYPE_VIEW_MORE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Product Type : \n {str(e)}")

    def get_product_Name_view_more(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_NAME_VIEW_MORE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Product Name : \n {str(e)}")

    def get_vendor_Name_view_more(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.VENDOR_NAME_VIEW_MORE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Product Name : \n {str(e)}")

    def get_received_date_view_more(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.RECEIVED_DATE_VIEW_MORE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Received Date : \n {str(e)}")

    def get_color_view_more(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.COLOR_VIEW_MORE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Color Data : \n {str(e)}")

    def get_quantity_view_more(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.QUANTITY_VIEW_MORE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Quantity Data : \n {str(e)}")

    def get_price_view_more(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PRICE_VIEW_MORE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Quantity Data : \n {str(e)}")

    def get_quality_view_more(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.QUALITY_VIEW_MORE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Quality Data : \n {str(e)}")

    def get_transportation_mode_view_more(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.TRANSPORT_BY_VIEW_MORE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Transportation  Data : \n {str(e)}")

    def get_payment_mode_view_more(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PAYMENT_MODE_VIEW_MORE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Payment Data : \n {str(e)}")

    def get_received_by_view_more(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.RECEIVED_BY_VIEW_MORE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Received By Data : \n {str(e)}")
