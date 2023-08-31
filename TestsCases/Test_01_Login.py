import os

import allure
import unittest
from ddt import ddt, data, unpack
from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType
from executions.LoginExecutions.LoginMethods import LoginMethod
from selenium.common.exceptions import NoSuchElementException, TimeoutException


@ddt
@allure.feature('Login Page')
@allure.title('Login Test')
class TestLogin(unittest.TestCase, BaseClass):

    # SetUp Method.
    def setUp(self):
        # browser = self.get_browser_from_command_line()  # Implement the logic to retrieve the browser name
        # browser = os.environ.get()
        super().initialize_driver("chrome")
        self.Login = LoginMethod(self.driver)


    # Test Cases.
    # Login Successful
    @allure.story("Login Successfully")
    @allure.description("Login Successfully")
    @allure.severity(allure.severity_level.NORMAL)
    # "*" must be used to indicate all the items from the list
    @data(*Utils.read_xlsx("../TestData/LoginTestData/login.xlsx", "login"))
    @unpack
    def test_LoginSuccessful(self, username, password):
        self.Login.nativelogin(username, password)
        try:
            self.assertEqual(self.Login.verify_correct_login(), True, msg="Login verification failed.")
        # Check if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_LoginSuccessful",
                attachment_type=AttachmentType.PNG)
            raise e

    # Login with Incorrect Cred
    @allure.story("Login Unsuccessfully")
    @allure.description("Login Unsuccessfully")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/LoginTestData/login.xlsx", "incorrect_cred"))
    @unpack
    def test_LoginUnsuccessful(self, username, password):
        self.Login.nativelogin(username, password)
        try:
            self.assertEqual(self.Login.verify_invalid_login(), True, msg="Error message verification failed.")
        # Check if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_LoginUnsuccessful",
                attachment_type=AttachmentType.PNG)
            raise e

    # Login with invalid Email
    # @allure.title("Login With Invalid Username")
    @allure.description("Login With Invalid Username")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/LoginTestData/login.xlsx", "invalid_email"))
    @unpack
    def test_login_Unsuccessful_with_invalid_username(self, username, password):
        self.Login.nativelogin(username, password)
        try:
            self.assertEqual(self.Login.verify_login_with_invalid_mail(), True, msg="Error message verification failed.")
        # Check if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_Unsuccessful_with_invalid_username",
                attachment_type=AttachmentType.PNG)
            raise e

    # Login with empty user ID fields
    # @allure.title("Login With Incorrect Username")
    @allure.description("Login With Incorrect Username")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/LoginTestData/login.xlsx", "empty_email"))
    @unpack
    def test_login_with_empty_userid_fields(self, username, password):
        self.Login.nativelogin("", password)
        try:
            self.assertEqual(self.Login.verify_empty_email_field(), True,
                             msg="Error message verification failed.")
        # Check if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_with_empty_userid_fields",
                attachment_type=AttachmentType.PNG)
            raise e

    # Login with empty Password ID fields
    @allure.description("Login With Incorrect Username")
    # @allure.title("Login With Incorrect Username")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/LoginTestData/login.xlsx", "empty_password"))
    @unpack
    def test_login_with_empty_password_fields(self, username, password):
        self.Login.nativelogin(username, "")
        try:
            self.assertEqual(self.Login.verify_empty_password_field(), True,
                             msg="Error message verification failed.")
        # Check if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="test_login_with_empty_password_fields",
                attachment_type=AttachmentType.PNG)
            raise e

    # Closing Method.
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            raise e
