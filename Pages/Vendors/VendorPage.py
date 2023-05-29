import logging
import time

from selenium import webdriver

from Utilities.utils import Utils
from Base.BaseTest import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class VendorPage:
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.log = Utils.custom_logger(logLevel=logging.DEBUG)
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





    # Methods

    # Starter Methods
    def clickOnVendor(self):
        return self.wait.until(EC.visibility_of_element_located(self.VENDOR_TAB)).click()

    def getPageTitle(self):
        print(self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE)).text)
        return self.wait.until(EC.visibility_of_element_located(self.PAGE_TITLE)).text

    # Adding new vendor
    def click_on_Add(self):
        return self.wait.until(EC.visibility_of_element_located(self.ADD_VENDOR)).click()

    def get_title_text(self):
        return self.wait.until(EC.visibility_of_element_located(self.ADD_VENDOR_LANDING)).text


    # Filling Vendor Details
    def upload_vendor_Icon(self, IconPath):
        time.sleep(2)
        return self.driver.find_element(*self.UPLOAD_ICON).send_keys(IconPath)

    def enterVendor_id(self, vendor_id):
        return self.wait.until(EC.visibility_of_element_located(self.VENDOR_ID)).send_keys(vendor_id)

    def enterVendor_name(self, vendor_name):
        return self.wait.until(EC.visibility_of_element_located(self.VENDOR_NAME)).send_keys(vendor_name)

    def enterVendor_phone(self, vendor_phone):
        return self.wait.until(EC.visibility_of_element_located(self.VENDOR_PHONE)).send_keys(vendor_phone)

    def enterVendor_email(self, vendor_email):
        return self.wait.until(EC.visibility_of_element_located(self.VENDOR_EMAIL)).send_keys(vendor_email)

    def enterSupplier_type(self, supplier_type):
        return self.wait.until(EC.visibility_of_element_located(self.SUPPLIER_TYPE)).send_keys(supplier_type)

    def enterLocation(self, location):
        return self.wait.until(EC.visibility_of_element_located(self.VENDOR_LOCATION)).send_keys(location)

    def enterDescriptions(self, descriptions):
        return self.wait.until(EC.visibility_of_element_located(self.DESCRIPTIONS)).send_keys(descriptions)


    # Filling Contacting Person Info
    def enterContactPersonName(self, contact_name):
        return self.wait.until(EC.visibility_of_element_located(self.CONTACT_NAME)).send_keys(contact_name)

    def enterContactPersonLocation(self, contact_location):
        return self.wait.until(EC.visibility_of_element_located(self.PERSON_LOCATION)).send_keys(contact_location)

    def enterContactPersonNumber(self, contact_number):
        return self.wait.until(EC.visibility_of_element_located(self.PERSON_PHONE)).send_keys(contact_number)

    def enterContactPersonEmail(self, contact_email):
        return self.wait.until(EC.visibility_of_element_located(self.PERSON_EMAIL)).send_keys(contact_email)

    # Button
    def click_on_submit(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BTN)).click()

    def click_on_cancel(self):
        return self.wait.until(EC.visibility_of_element_located(self.CANCLE_BTN)).click()
