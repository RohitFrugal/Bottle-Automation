import logging
import time

from selenium import webdriver
from selenium.webdriver import Keys

from Utilities.utils import Utils
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class OrderPage:
    wait: WebDriverWait
    driver: webdriver

    # Locators
    OrderTab = (By.ID, 'OrderListMenu')
    HeaderText = (By.XPATH, '//*[@id="root"]/section/main/div/div[1]/div[1]/h1')

    # Create Order -
    AddOrderbtn = (By.XPATH, '//*[@id="root"]/section/main/div/div[1]/div[2]/div/div[3]/div/span')
    ForCustomer = (By.XPATH, '//*[@id="root"]/section/main/div/div/div/div[2]/button')
    ForStore = (By.XPATH, '//*[@id="root"]/section/main/div/div/div/div[3]/button')
    InputContact = (By.ID, 'contact')

    # For existing user.

    ClickOnCustomer = (By.XPATH, '//*[@id="root"]/section/main/div/div/div/form/div/div[2]/div/div/div[2]/h4')
    ClickOnNext = (By.XPATH, '//*[@id="root"]/section/main/div/div/div/div/button')

    # For new user.
    InputName = (By.ID, 'name')
    InputEmail = (By.ID, 'email')
    InputDob = (By.ID, 'dob')  # Format - 2022-12-12
    InputAddress = (By.XPATH,
                    '//*[@id="root"]/section/main/div/div/form/div/div/div/div[5]/div[2]/div/div/div/div/div/div/div[2]/div[1]/div/input')
    SuggestedAddress = (By.XPATH, '/html/body/div[5]')

    SubmitUser = (
    By.XPATH, '//*[@id="root"]/section/main/div/div/form/div/div/div/div[6]/div/div/div/div/div/button/span')

    # Verify Create User
    PageHeader = (By.XPATH, '//*[@id="root"]/section/main/div/div/h2')

    # Initializing driver and logger.
    def __init__(self, driver):
        self.log = Utils.custom_logger(logLevel=logging.DEBUG)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Methods
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

    # Filling user details form.
    def input_name(self, name):
        return self.wait.until(EC.visibility_of_element_located(self.InputName)).send_keys(name)

    def input_email(self, email):
        return self.wait.until(EC.visibility_of_element_located(self.InputEmail)).send_keys(email)

    def input_dob(self, dob):
        return self.wait.until(EC.visibility_of_element_located(self.InputDob)).send_keys(dob)

    def input_address(self, address):
        user_address = self.wait.until(EC.visibility_of_element_located(self.InputAddress))
        user_address.send_keys(address)
        time.sleep(1)
        user_address.send_keys(Keys.SPACE)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pac-container")))
        time.sleep(1)
        user_address.send_keys(Keys.DOWN)
        time.sleep(1)
        self.wait.until(EC.presence_of_element_located((By.CLASS_NAME, "pac-item"))).click()
        time.sleep(1)

    def submit_new_user(self):
        return self.wait.until(EC.element_to_be_clickable(self.SubmitUser)).click()

    def verify_Create_user(self):
        print(self.wait.until(EC.visibility_of_element_located(self.PageHeader)).text)
        return self.wait.until(EC.visibility_of_element_located(self.PageHeader)).text
