import logging
import allure
import unittest
from ddt import ddt, data, unpack
from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from Pages.LoginPage import LoginPage
from selenium.common import WebDriverException
from executions.LoginMethod import LoginMethod
from allure_commons.types import AttachmentType


@ddt
@allure.feature('Login Page')
@allure.title('Login Test')
class TestLogin(unittest.TestCase, BaseClass):
    # Calling Logger.
    log = Utils.custom_logger(logLevel=logging.WARNING)

    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.Login = LoginPage(self.driver)
        self.LoginMethod = LoginMethod(self.driver)

    # Test Cases.
    # Login Successful
    @allure.story("Login Successfully")
    @allure.severity(allure.severity_level.NORMAL)
    @data(("frugal@latido.com.np", "Test@123"), ("rohit12@latido.com.np", "Test@123"))
    @unpack
    def test_LoginSuccessful(self, username, password):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(self.Login.verify_login(), "OVERVIEW", msg="Login verification failed.")

        # Check if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    # Login with Incorrect Cred
    @allure.story("Login Unsuccessfully")
    @allure.severity(allure.severity_level.NORMAL)
    @data(("frugal@latido.com.np", "Test@1as23"), ("rohitw1@latido.com.np", "Tesdt@23"))
    @unpack
    def test_LoginUnsuccessful(self, username, password):
        self.LoginMethod.nativeloginforWrongCred(self.driver, username, password)
        try:
            self.assertEqual(self.Login.verify_login_error_message(), "Incorrect username or password.",
                             msg="Error message verification failed.")
        # Check if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    # Login with invalid Email
    @allure.story("Login With Invalid Username")
    @allure.severity(allure.severity_level.NORMAL)
    @data(("frugal@-latido.com.np", "Test@123"), ("rohit12#4@ latido.co.np", "Test@123"))
    @unpack
    def test_login_unsuccessful_with_invalid_username(self, username, password):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(self.Login.verify_login_error_message_for_invalid_email(),
                             "Incorrect username or password.",
                             msg="Error message verification failed.")
        # Check if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    # Login with empty user ID fields
    @allure.story("Login With Incorrect Username")
    @allure.severity(allure.severity_level.NORMAL)
    @data(("", "Test@123"), ("", "Test@123"))
    @unpack
    def test_login_with_empty_userid_fields(self, username, password):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(self.Login.verify_login_error_message_with_noEmail(), "Please input your Email!",
                             msg="Error message verification failed.")
        # Check if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    # Login with empty Password ID fields
    @allure.story("Login With Incorrect Username")
    @allure.severity(allure.severity_level.NORMAL)
    @data(("frugal@latido.com.np", ""), ("rohit12@latido.com.np", ""))
    @unpack
    def test_login_with_empty_password_fields(self, username, password):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(self.Login.verify_login_error_message_with_noPassword(), "Please input your password!",
                             msg="Error message verification failed.")
        # Check if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestLoginScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    # Closing Method.
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            self.log.error(f"Failed to close driver. {str(e)}")
            raise e
