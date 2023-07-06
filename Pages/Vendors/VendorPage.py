import time
import logging
from selenium import webdriver
from Utilities.utils import Utils
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException



class VendorPage:
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.log = Utils.custom_logger(module_name="Vendor_module", logLevel=logging.DEBUG)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators

    # Starter
    VENDOR_TAB = (By.ID, "VendorsMenu")
    PAGE_TITLE = (By.XPATH, "//h1[@class='ant-typography product-name']")

    # Adding new Vendor
    ADD_VENDOR = (By.XPATH, "//button[@class='ant-btn ant-btn-round ant-btn-primary']")
    ADD_VENDOR_LANDING = (By.XPATH, "(//h4)[1]")

    # Filling Vendor Details
    UPLOAD_ICON = (By.XPATH, "//input[@type='file']")
    VENDOR_ID = (By.ID, "vendor_id")
    VENDOR_NAME = (By.ID, "vendor_name")
    VENDOR_PHONE = (By.ID, "phone_no")
    VENDOR_EMAIL = (By.ID, "email")
    SUPPLIER_TYPE = (By.ID, "supplies_type")
    VENDOR_LOCATION = (By.ID, "location")
    DESCRIPTIONS = (By.ID, "description")

    # Filling contacting Person info
    CONTACT_NAME = (By.ID, "contact_person_contact_name")
    PERSON_LOCATION = (By.ID, "contact_person_location")
    PERSON_PHONE = (By.ID, "contact_person_phone_no")
    PERSON_EMAIL = (By.ID, "contact_person_email")

    # Buttons
    SUBMIT_BTN = (By.XPATH, "//button[@type='submit']")
    CANCLE_BTN = (By.XPATH, "//button[@type='button']")

    # Validating Text
    VALIDATION_MSG = (By.XPATH, "//div[@class='ant-notification-notice-message']")

    # Searching Item
    SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search vendor']")

    # Editing Vendor Details
    SORT_SELECTOR = (By.XPATH, "//div[@class='ant-select-selector']")
    DESCENDING_SELECTOR = (By.XPATH, "//div[@class='ant-select-item-option-content'][contains(text(), 'Descending ')]")
    EDIT_BTN = (By.XPATH, "((//div[@class='ant-space-item'])/span)")
    DELETE_BTN = (By.XPATH, "(//span[@class='anticon anticon-delete action-icon'])[1]")
    OK_DELETE_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
    CANCLE_DELETE_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-default']")

    # Comparing values
    cp_vendor_name = (By.XPATH, "//h2[contains(text(), '')]")
    cp_vendor_phone = (By.XPATH, "(//span[@class='ant-descriptions-item-content'])[1]")
    cp_vendor_email = (By.XPATH, "(//span[@class='ant-descriptions-item-content'])[3]")

    # Methods

    # Helper Methods
    def BackSpace(self, selector):
        try:
            self.wait.until(EC.visibility_of_element_located(selector)).send_keys(Keys.CONTROL + 'a')
            self.wait.until(EC.visibility_of_element_located(selector)).send_keys(Keys.BACKSPACE)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Clear \n {str(e)}")

    # Starter Methods
    def clickOnVendor(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.VENDOR_TAB)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Navigate to Vendor : \n {str(e)}")

    def getPageTitle(self):
        try:
            print(self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE)).text)
            return self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to find the Page Title : \n {str(e)}")

    # Adding new vendor
    def click_on_Add(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ADD_VENDOR)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to add new Vendor: \n {str(e)}")

    def get_title_text(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ADD_VENDOR_LANDING)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to get the Title text : \n {str(e)}")

    # Filling Vendor Details
    def upload_vendor_Icon(self, IconPath):
        try:
            time.sleep(2)
            return self.driver.find_element(*self.UPLOAD_ICON).send_keys(IconPath)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Upload Vendor ICON : \n {str(e)}")

    def enterVendor_id(self, vendor_id):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.VENDOR_ID)).send_keys(vendor_id)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Input vendor ID : \n {str(e)}")

    def enterVendor_name(self, vendor_name):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.VENDOR_NAME)).send_keys(vendor_name)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input vendor Name : \n {str(e)}")

    def enterVendor_phone(self, vendor_phone):
        try:
            # print(f"Phone number type: {type(vendor_phone)}")
            return self.wait.until(EC.visibility_of_element_located(self.VENDOR_PHONE)).send_keys(vendor_phone)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input vendor Phone : \n {str(e)}")

    def enterVendor_email(self, vendor_email):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.VENDOR_EMAIL)).send_keys(vendor_email)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input Vendor Mail: \n {str(e)}")

    def enterSupplier_type(self, supplier_type):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SUPPLIER_TYPE)).send_keys(supplier_type)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input supplier Type : \n {str(e)}")

    def enterLocation(self, location):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.VENDOR_LOCATION)).send_keys(location)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input Location : \n {str(e)}")

    def enterDescriptions(self, descriptions):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.DESCRIPTIONS)).send_keys(descriptions)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input descriptions : \n {str(e)}")

    # Filling Contacting Person Info
    def enterContactPersonName(self, contact_name):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CONTACT_NAME)).send_keys(contact_name)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input contact Person name  : \n {str(e)}")

    def enterContactPersonLocation(self, contact_location):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PERSON_LOCATION)).send_keys(contact_location)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input contact Person Location : \n {str(e)}")

    def enterContactPersonNumber(self, contact_number):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PERSON_PHONE)).send_keys(contact_number)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input contact Person number  : \n {str(e)}")

    def enterContactPersonEmail(self, contact_email):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PERSON_EMAIL)).send_keys(contact_email)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input contact Person Email  : \n {str(e)}")

    # Button
    def click_on_submit(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BTN)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Submit button : \n {str(e)}")

    def click_on_cancel(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CANCLE_BTN)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Cancel button  : \n {str(e)}")

    def click_on_edit(self):
        try:
            time.sleep(2)
            return self.wait.until(EC.visibility_of_element_located(self.EDIT_BTN)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Edit button  : \n {str(e)}")

    # Validating create new Vendor
    def get_validation_msg(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.VALIDATION_MSG)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to fetch Validation msg : \n {str(e)}")

    # Sorting Vendor
    def sort_vendor(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.SORT_SELECTOR)).click()
            return self.wait.until(EC.visibility_of_element_located(self.DESCENDING_SELECTOR)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to sort the vendors : \n {str(e)}")

    # Editing Vendor Value
    def get_edit_values(self):
        try:
            comparison_values = [self.wait.until(EC.visibility_of_element_located(self.cp_vendor_name)).text,
                             int(self.wait.until(EC.visibility_of_element_located(self.cp_vendor_phone)).text),
                             self.wait.until(EC.visibility_of_element_located(self.cp_vendor_email)).text]
            return comparison_values
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to get the updated values of Vendor : \n {str(e)}")

    def search(self, search_item):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SEARCH_BAR)).send_keys(search_item)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Search Element : \n {str(e)}")

    def delete_vendor(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.DELETE_BTN)).click()
            time.sleep(2)
            return self.wait.until(EC.visibility_of_element_located(self.OK_DELETE_BTN)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Delete the Vendor : \n {str(e)}")