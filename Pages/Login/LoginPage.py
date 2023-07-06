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





class LoginPage:
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Login_module", logLevel=logging.WARNING)


    # Login.
    userIdField = (By.ID, "basic_email")
    PasswordField = (By.ID, "basic_password")

    SubmitButton = (By.XPATH, "//*[@id='basic']/div[2]/div/div/div/div/button")
    WelcomeMsg = (By.XPATH, "//*[@id='root']/section/main/div/div/div[1]/h2")

    # Login Error Messages

    errorTile = (By.XPATH, "/html/body/div[3]/div/div/div/div/div/span[1]")
    ErrorMsg = (By.XPATH, "//html/body/div[3]/div/div/div/div/div/span[2]")
    invalid_email_err_msg = (By.XPATH, "//div[@class='ant-form-item-explain-error']")
    NoEmailErrorMsg = (By.XPATH, '//*[@id="basic"]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div')
    NoPasswordErrorMsg = (By.XPATH, "//*[@id='basic']/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div")

    # Logout.
    svg_element = (By.XPATH, "(//div[@class='menu']/span[@role='img'])[1]")
    logout = (By.XPATH, "//div[@id='LogoutButton']")
    logoutScreen = (By.XPATH, "//button[@id='LogoutConfirmButton']")


    # Login Methods
    def enter_user_id(self, username):
        try:
            self.BackSpaceUsername()
            self.wait.until(EC.element_to_be_clickable(self.userIdField)).send_keys(username)
        except (NoSuchElementException, Exception) as e:
            self.log.error(f"Exception occurred while entering user ID: {e}")

    def enter_password(self, password):
        try:
            self.BackSpacePassword()
            self.wait.until(EC.element_to_be_clickable(self.PasswordField)).send_keys(password)
        except NoSuchElementException as e:
            self.log.error(f"Exception occurred while entering password: {e}")

    def click_on_submit_button(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.SubmitButton)).click()
        except (NoSuchElementException, TimeoutException, Exception)as e:
            self.log.error(f"Exception occurred while clicking on submit button: {e}")

    def click_on_logOut_button(self):
        try:
            action_chains = ActionChains(self.driver)
            svg_element = self.wait.until(EC.presence_of_element_located(self.svg_element))
            action_chains.move_to_element(svg_element).perform()
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable(self.logout)).click()
            time.sleep(2)
            self.wait.until(EC.element_to_be_clickable(self.logoutScreen)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Exception occurred while clicking on logout button: {e}")

    # Login Methods end's here.

    # Verification Methods
    def verify_login(self):
        try:
            text = self.wait.until(EC.visibility_of_element_located(self.WelcomeMsg)).text
            return text
        except (NoSuchElementException, Exception) as e:
            self.log.error(f"Exception occurred while verifying login: {e}")

    def verify_login_error_message(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.invalid_email_err_msg)).text
        except (NoSuchElementException, Exception) as e:
            self.log.error(f"Exception occurred while verifying login: {e}")

    def verify_login_error_message_for_invalid_email(self):
        try:
            invalid_email = self.wait.until(EC.visibility_of_element_located(self.invalid_email_err_msg)).text
            return invalid_email
        except (NoSuchElementException, Exception) as e:
            self.log.error(f"Exception occurred while verifying login: {e}")

    def verify_login_error_message_with_noEmail(self):
        try:
            no_email = self.wait.until(EC.visibility_of_element_located(self.NoEmailErrorMsg)).text
            return no_email
        except (NoSuchElementException, Exception) as e:
            self.log.error(f"Exception occurred while verifying login: {e}")

    def verify_login_error_message_with_noPassword(self):
        try:
            no_password = self.wait.until(EC.visibility_of_element_located(self.NoPasswordErrorMsg)).text
            return no_password
        except (NoSuchElementException, Exception) as e:
            self.log.error(f"Exception occurred while verifying login: {e}")

    # Verification Methods end's here



    # Clearing the Fields
    def BackSpaceUsername(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.userIdField)).send_keys(Keys.CONTROL + 'a')
            self.wait.until(EC.element_to_be_clickable(self.userIdField)).send_keys(Keys.BACKSPACE)
        except NoSuchElementException as e:
            self.log.error(f"Exception occurred while verifying login: {e}")
    def BackSpacePassword(self):
        try:
            self.wait.until(EC.element_to_be_clickable(self.PasswordField)).send_keys(Keys.CONTROL + 'a')
            self.wait.until(EC.element_to_be_clickable(self.PasswordField)).send_keys(Keys.BACKSPACE)
        except NoSuchElementException as e:
            self.log.error(f"Exception occurred while verifying login: {e}")
