import logging
import time

from selenium import webdriver
from Utilities.utils import Utils
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException

class MemberPage:
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Member_management_module", logLevel=logging.WARNING)



    # Locators
    MemberTab = (By.ID, "MemberManagementMenu")
    HeaderText = (By.XPATH, "//h1[@class='ant-typography product-name']")

    # Add new user
    ADD_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-round ant-btn-primary']")
    NAME = (By.XPATH, "(//input[@id='name'])[2]")
    click_search = (By.XPATH, "//div[@class='ant-select-selection-search']")
    DESIGNATION = (By.XPATH, "//input[@id='role']")
    EMAIL = (By.XPATH, "//input[@id='email']")
    PHONE_NUMBER = (By.XPATH, "//input[@id='phone_number']")
    ADDRESS = (By.XPATH, "//input[@id='address']")
    TEMP_PASSWORD = (By.XPATH, "//input[@id='temporaryPassword']")
    INPUT_IMG = (By.XPATH, "//input[@type='file']")
    OKAY_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
    SAVE_BUTTON = (By.XPATH, "(//button[@class='ant-btn ant-btn-round ant-btn-primary'])[2]")

    CONFIRM_MSG = (By.XPATH, "//div[@class='ant-notification-notice-message']")

    # Edit & Delete
    EDIT_BTN = (By.XPATH, "(//span[@class='ant-avatar ant-avatar-circle ant-avatar-icon'][1])[1]")
    REMOVE_ROLE = (By.XPATH, "//span[@class='anticon anticon-close']")
    DELETE_BTN = (By.XPATH, "(//span[@class='ant-avatar ant-avatar-circle ant-avatar-icon'][2])[1]")
    OK_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary ant-btn-sm']")

    # Reset Password
    RESET_PASSWORD = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
    ENTER_PASSWORD = (By.XPATH, "//input[@id='password']")
    RESET_PASSWORD_BUTTON = (By.XPATH, "(//button[@class='ant-btn ant-btn-primary'])[2]")
    RESET_PASSWORD_VERIFY = (By.XPATH, "//div[@class='ant-message-custom-content ant-message-success']")

    # Helper Methods
    def BackSpace(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).send_keys(Keys.CONTROL + 'a')
            self.wait.until(EC.element_to_be_clickable(locator)).send_keys(Keys.BACKSPACE)
        except NoSuchElementException as e:
            self.log.error(f"Exception occurred while clearing email address: {e}")

    # Locator Function
    def navigate_to_member(self):
        try:
            return self.wait.until(EC.element_to_be_clickable(self.MemberTab)).click()
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to locate Member Management Menu : {str(e)}")

    def get_Header_Text(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.HeaderText)).text
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to Locate the Header Text for Member Management: {str(e)}")

    def click_on_add(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ADD_BTN)).click()
        except(TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to Locate Add Button : {str(e)}")

    # Fill_new_user_form
    def enter_name(self, name):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.NAME)).send_keys(name)
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to locate the element to input name : {str(e)}")

    def enter_designation(self, designation):
        try:
            self.wait.until(EC.visibility_of_element_located(self.click_search)).click()
            search_list = (By.XPATH, f"//div[@class='ant-select-item-option-content'][contains(text(), '{designation}')]")
            return self.wait.until(EC.visibility_of_element_located(search_list)).click()
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to locate the element to input designation : {str(e)}")

    def enter_edit_designation(self, designation):
        try:
            search_list = (By.XPATH, "//input[@class='ant-select-selection-search-input']")
            self.wait.until(EC.visibility_of_element_located(self.REMOVE_ROLE)).click()
            self.wait.until(EC.visibility_of_element_located(self.click_search)).click()
            self.wait.until(EC.visibility_of_element_located(search_list)).send_keys(designation)
            return self.wait.until(EC.visibility_of_element_located(search_list)).send_keys(Keys.ENTER)
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to locate the element to input designation : {str(e)}")

    def enter_email(self, email):
        try:
            self.BackSpace(self.EMAIL)
            return self.wait.until(EC.visibility_of_element_located(self.EMAIL)).send_keys(email)
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to locate the element to input email : {str(e)}")

    def enter_phone_number(self, phone_number):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PHONE_NUMBER)).send_keys(phone_number)
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to locate the element to input phone_number : {str(e)}")

    def enter_address(self, address):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ADDRESS)).send_keys(address)
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to locate the element to input Address : {str(e)}")

    def enter_password(self, password):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.TEMP_PASSWORD)).send_keys(password)
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to locate the element to input password : {str(e)}")


    def get_Image(self, ImgPath):
        try:
            self.wait.until(EC.visibility_of_element_located(self.INPUT_IMG)).send_keys(ImgPath)
            return self.wait.until(EC.visibility_of_element_located(self.OKAY_BUTTON)).click()
        except(TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to locate the element to upload the image : {str(e)}")

    def save(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SAVE_BUTTON)).click()
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to locate save button : {str(e)}")

    def validating_string(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CONFIRM_MSG)).text
        except(TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Something went wrong while creating an User : {str(e)}")

    # TODO -- Add a new function for Deletions.
    def edit(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.EDIT_BTN)).click()
        except (TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Something went wrong while finding edit button : {str(e)}")

    def delete(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.DELETE_BTN)).click()
            return self.wait.until(EC.visibility_of_element_located(self.OK_BUTTON)).click()
        except(TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Somthing went wrong while deleting the member : {str(e)}")
    def get_username(self):
        userName = (By.XPATH, "(//h4[@class='ant-typography'])[1]")
        return self.wait.until(EC.visibility_of_element_located(userName)).text

    def get_designated_role(self):
        designated_role = (By.XPATH, "(//div[@class='ant-typography'])[1]")
        return self.wait.until(EC.visibility_of_element_located(designated_role)).text

    def resetPassword(self, password):
        try:
            self.wait.until(EC.visibility_of_element_located(self.RESET_PASSWORD)).click()
            self.wait.until(EC.visibility_of_element_located(self.ENTER_PASSWORD)).send_keys(password)
            self.wait.until(EC.visibility_of_element_located(self.RESET_PASSWORD_BUTTON)).click()
        except(TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f" Unable to locate reset password button : {str(e)}")


    def get_password_verify(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.RESET_PASSWORD_VERIFY)).text
        except(TimeoutException, NoSuchElementException, Exception) as e:
            self.log.error(f"Unable to fetch the verification message for reset password : {str(e)}")
