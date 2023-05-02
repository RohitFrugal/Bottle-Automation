import logging
import allure
import unittest
from ddt import ddt, data, unpack
from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from Pages.Login.LoginPage import LoginPage
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType
from executions.LoginExecutions.LoginMethod import LoginMethod


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
    @allure.title("Login Successfully")
    @allure.severity(allure.severity_level.NORMAL)
    # "*" must be used to indicate all the items from the list
    @data(*Utils.read_xlsx("../TestData/LoginTestData/login.xlsx", "login"))
    @unpack
    def test_LoginSuccessful(self, username, password, output):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(self.Login.verify_login(), output, msg="Login verification failed.")

        # Check if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_LoginSuccessful",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    # Login with Incorrect Cred
    @allure.story("Login Unsuccessfully")
    @allure.title("Login Unsuccessfully")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/LoginTestData/login.xlsx", "incorrect_cred"))
    @unpack
    def test_LoginUnsuccessful(self, username, password, output):
        self.LoginMethod.nativeloginforWrongCred(self.driver, username, password)
        try:
            self.assertEqual(self.Login.verify_login_error_message(), output,
                             msg="Error message verification failed.")
        # Check if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_LoginUnsuccessful",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    # Login with invalid Email
    @allure.title("Login With Invalid Username")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/LoginTestData/login.xlsx", "invalid_email"))
    @unpack
    def test_login_Unsuccessful_with_invalid_username(self, username, password, output):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(self.Login.verify_login_error_message_for_invalid_email(), output,
                             msg="Error message verification failed.")
        # Check if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_Unsuccessful_with_invalid_username",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    # Login with empty user ID fields
    @allure.story("Login With Incorrect Username")
    @allure.title("Login With Incorrect Username")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/LoginTestData/login.xlsx", "empty_email"))
    @unpack
    def test_login_with_empty_userid_fields(self, username, password, output):
        self.LoginMethod.nativelogin(self.driver, "", password)
        try:
            self.assertEqual(self.Login.verify_login_error_message_with_noEmail(), output,
                             msg="Error message verification failed.")
        # Check if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_with_empty_userid_fields",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    # Login with empty Password ID fields
    @allure.story("Login With Incorrect Username")
    @allure.title("Login With Incorrect Username")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/LoginTestData/login.xlsx", "empty_password"))
    @unpack
    def test_login_with_empty_password_fields(self, username, password, output):
        self.LoginMethod.nativelogin(self.driver, username, "")
        try:
            self.assertEqual(self.Login.verify_login_error_message_with_noPassword(), output,
                             msg="Error message verification failed.")
        # Check if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_with_empty_password_fields",
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
