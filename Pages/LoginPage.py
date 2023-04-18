import time
import logging
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains

from Utilities.utils import Utils


class LoginPage:
    wait: WebDriverWait
    driver: webdriver

    # Login.
    userIdField = (By.ID, "basic_email")
    PasswordField = (By.ID, "basic_password")
    SubmitButton = (By.XPATH, "//*[@id='basic']/div[2]/div/div/div/div/button")
    WelcomeMsg = (By.XPATH, "//*[@id='root']/section/main/div/div/div[1]/h2")

    # Login Error Messages

    errorTile = (By.XPATH, "/html/body/div[3]/div/div/div/div/div/span[1]")
    ErrorMsg = (By.XPATH, "//html/body/div[3]/div/div/div/div/div/span[2]")
    invalid_email_err_msg = (By.XPATH, "/html/body/div[3]/div/div/div/div/div/span[2]")
    NoEmailErrorMsg = (By.XPATH, '//*[@id="basic"]/div[1]/div[1]/div/div[1]/div[2]/div[2]/div[1]/div')
    NoPasswordErrorMsg = (By.XPATH, "//*[@id='basic']/div[1]/div[2]/div/div[1]/div[2]/div[2]/div[1]/div")



    # Logout.
    svg_element = (By.XPATH, "//*[@id='root']/section/div/div/header/div[2]/div[12]/span")
    logout = (By.XPATH, "/html/body/div[3]/div/div/div/div[2]/div/div[2]")
    logoutScreen = (By.XPATH, "/html/body/div[4]/div/div[2]/div/div[2]/div[2]/button[2]/span")

    # Initializing driver and logger.
    def __init__(self, driver):
        self.log = Utils.custom_logger(logLevel=logging.WARNING)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Login Methods
    def enter_user_id(self, username):
        self.BackSpaceUsername()
        self.wait.until(EC.element_to_be_clickable(self.userIdField)).send_keys(username)

    def enter_password(self, password):
        self.BackSpacePassword()
        self.wait.until(EC.element_to_be_clickable(self.PasswordField)).send_keys(password)

    def click_on_submit_button(self):
        self.wait.until(EC.element_to_be_clickable(self.SubmitButton)).click()

    def click_on_logOut_button(self):
        action_chains = ActionChains(self.driver)
        svg_element = self.wait.until(EC.presence_of_element_located(self.svg_element))
        action_chains.move_to_element(svg_element).perform()
        self.wait.until(EC.element_to_be_clickable(self.logout)).click()
        logout_btn = self.wait.until(EC.element_to_be_clickable(self.logoutScreen))
        logout_btn.click()

    # Login Methods end's here.

    # Verification Methods
    def verify_login(self):
        text = self.wait.until(EC.visibility_of_element_located(self.WelcomeMsg)).text
        return text

    def verify_login_error_message(self):
        error_msg_tooltip = self.wait.until(EC.visibility_of_element_located(self.errorTile))
        hover = ActionChains(self.driver).move_to_element(error_msg_tooltip)
        hover.perform()
        error_msg = self.wait.until(EC.visibility_of_element_located(self.ErrorMsg)).text
        self.log.warning(f"Unable to find the given element present on this XPath : '{self.ErrorMsg}'")
        return error_msg

    def verify_login_error_message_for_invalid_email(self):
        invalid_email = self.wait.until(EC.visibility_of_element_located(self.invalid_email_err_msg)).text
        return invalid_email

    def verify_login_error_message_with_noEmail(self):
        no_email = self.wait.until(EC.visibility_of_element_located(self.NoEmailErrorMsg)).text
        return no_email

    def verify_login_error_message_with_noPassword(self):
        no_password = self.wait.until(EC.visibility_of_element_located(self.NoPasswordErrorMsg)).text
        return no_password

    # Verification Methods end's here

    # Clearing the Fields
    def BackSpaceUsername(self):
        self.wait.until(EC.element_to_be_clickable(self.userIdField)).send_keys(Keys.CONTROL + 'a')
        self.wait.until(EC.element_to_be_clickable(self.userIdField)).send_keys(Keys.BACKSPACE)

    def BackSpacePassword(self):
        self.wait.until(EC.element_to_be_clickable(self.PasswordField)).send_keys(Keys.CONTROL + 'a')
        self.wait.until(EC.element_to_be_clickable(self.PasswordField)).send_keys(Keys.BACKSPACE)