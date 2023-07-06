import logging
import time

from selenium import webdriver

from Utilities.utils import Utils
from Base.BaseTest import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException



class OrderPage(BaseClass):
    wait: WebDriverWait
    driver: webdriver

    # Locators
    OrderTab = (By.XPATH, "(//div[@class='menu']/a[@id='OrderListMenu'])[1]")
    HeaderText = (By.XPATH, '//*[@id="root"]/section/main/div/div[1]/div[1]/h1')

    # Create Order
    AddOrderbtn = (By.XPATH, '//*[@id="root"]/section/main/div/div[1]/div[2]/div/div[3]/div/span')
    ForCustomer = (By.XPATH, '//*[@id="root"]/section/main/div/div/div/div[2]/button')
    ForStore = (By.XPATH, '//*[@id="root"]/section/main/div/div/div/div[3]/button')
    InputContact = (By.ID, 'contact')

    # For existing user.
    ClickOnCustomer = (By.XPATH, '//*[@id="root"]/section/main/div/div/div/form/div/div[2]/div/div/div[2]/h4')
    ClickOnNext = (By.XPATH, '//*[@id="root"]/section/main/div/div/div/div/button')


    # Fill Customer Details.
    FULLNAME = (By.ID, 'userName')
    GENDER_MAlE = (By.XPATH, '//label[@class="ant-radio-button-wrapper ant-radio-button-wrapper-in-form-item"][1]/span[2]/div/img')
    GENDER_FEMAlE = (By.XPATH, '//label[@class="ant-radio-button-wrapper ant-radio-button-wrapper-in-form-item"][2]/span[2]/div/img')
    GENDER_OTHER = (By.XPATH, '//label[@class="ant-radio-button-wrapper ant-radio-button-wrapper-in-form-item"][3]/span[2]/div/img')
    EMAIL = (By.ID, 'email')

    # Successful Message.
    CONFIRM_MSG = (By.XPATH, "//div[@class='ant-notification-notice-message']")

    # Navigate to Store
    STORE_PAGE = (By.XPATH, "//div[@class='ant-tabs-nav-list']/div[@class='ant-tabs-tab']")


    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Order_module", logLevel=logging.WARNING)

    # Methods

    # Move to Create Order Page.
    def clickOnOrderTab(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.OrderTab)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't Locate Order Tab : \n {str(e)}")

    def move_to_store(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.STORE_PAGE)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't Locate Store Tab : \n {str(e)}")


    def verify_header(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.HeaderText)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't Locate element for Header Text : \n {str(e)}")

    def click_on_add(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.AddOrderbtn)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Add  : \n {str(e)}")

    def click_on_forCustomer(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.ForCustomer)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Customer Button : \n {str(e)}")

    def click_on_forStore(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.ForStore)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Store Button : \n {str(e)}")

    def enter_contact(self, contactNo):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.InputContact)).send_keys(contactNo)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Input Contact : \n {str(e)}")

    def click_on_customer(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.ClickOnCustomer)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Customer Order: \n {str(e)}")

    def move_next(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.ClickOnNext)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for moving Next : \n {str(e)}")


    # Fill customer details
    def inputCustomer_name(self, name):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.FULLNAME)).send_keys(name)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input Customer Name : \n {str(e)}")

    def click_gender(self, gender):
        try:
            self.selectGender(gender)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Selecting Customer Gender : \n {str(e)}")

    def enterEmail(self, email):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input Customer email: \n {str(e)}")

    # Handle DropDown
    def HandleDropdown(self, dropDownLocator, itemsLocator, valueName):
        self.wait.until(EC.visibility_of_element_located(dropDownLocator)).click()
        all_items = self.wait.until(EC.presence_of_all_elements_located(itemsLocator))
        print(f"This is total length of : {len(all_items)}")
        for item in all_items:
            print(item.text)
            if item.text == valueName:
                self.log.info(f"This items got clicked {item.text}")
                item.click()
                break


    def searchDropdown(self, selectInputLocator, itemsLocator, valueName):
        self.wait.until(EC.visibility_of_element_located(selectInputLocator)).send_keys(valueName)
        all_items = self.wait.until(EC.presence_of_all_elements_located(itemsLocator))
        for item in all_items:
            if item.text != valueName:
                self.page_scroll()
            if item.text == valueName:
                self.log.info(f"This items got clicked {item.text}")
                item.click()
                break



    # Handle Gender Selections
    def selectGender(self, gender):
        # Selecting Male
        if gender.lower() == 'male':
            try:
                return self.wait.until(EC.visibility_of_element_located(self.GENDER_MAlE)).click()
            except Exception as e:
                self.log.error(f"Occurred in Male selections {str(e)}")

        # Selecting Female
        elif gender.lower() == 'female':
            try:
                return self.wait.until(EC.visibility_of_element_located(self.GENDER_FEMAlE)).click()
            except Exception as e:
                self.log.error(f"Occurred in Female selections {str(e)}")

        # Selecting Others
        elif gender.lower() == 'other':
            try:
                return self.wait.until(EC.visibility_of_element_located(self.GENDER_OTHER)).click()
            except Exception as e:
                self.log.error(f"Occurred in Others selections {str(e)}")

