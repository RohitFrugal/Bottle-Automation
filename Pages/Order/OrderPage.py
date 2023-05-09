import logging
import time

from selenium import webdriver

from Utilities.utils import Utils
from Base.BaseTest import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC



class OrderPage(BaseClass):
    wait: WebDriverWait
    driver: webdriver

    # Locators
    OrderTab = (By.ID, 'OrderListMenu')
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





    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.log = Utils.custom_logger(logLevel=logging.DEBUG)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Methods

    # Move to Create Order Page.
    def clickOnOrderTab(self):
        self.wait.until(EC.element_to_be_clickable(self.OrderTab)).click()
    def verify_header(self):
        return self.wait.until(EC.visibility_of_element_located(self.HeaderText)).text
    def click_on_add(self):
        return self.wait.until(EC.element_to_be_clickable(self.AddOrderbtn)).click()
    def click_on_forCustomer(self):
        return self.wait.until(EC.element_to_be_clickable(self.ForCustomer)).click()
    def click_on_forStore(self):
        return self.wait.until(EC.element_to_be_clickable(self.ForStore)).click()
    def enter_contact(self, contactNo):
        return self.wait.until(EC.visibility_of_element_located(self.InputContact)).send_keys(contactNo)
    def click_on_customer(self):
        return self.wait.until(EC.element_to_be_clickable(self.ClickOnCustomer)).click()
    def move_next(self):
        return self.wait.until(EC.element_to_be_clickable(self.ClickOnNext)).click()



    # Fill customer details
    def inputCustomer_name(self, name):
        return self.wait.until(EC.visibility_of_element_located(self.FULLNAME)).send_keys(name)
    def click_gender(self, gender):
        self.selectGender(gender)
    def enterEmail(self, email):
        return self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)


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

