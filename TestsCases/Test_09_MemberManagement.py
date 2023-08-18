
import allure
import unittest
from ddt import ddt, unpack, data
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType

from Base.BaseTest import BaseClass
from Utilities.utils import Utils
from executions.LoginExecutions.LoginMethods import LoginMethod
from executions.MemberExecutions.MemberMethods import MemberMethods
from selenium.common.exceptions import NoSuchElementException, TimeoutException


@ddt
@allure.feature('Member Management')
@allure.title('Creating new Member Management')
class TestMemberManagement(unittest.TestCase, BaseClass):
    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.LoginMethod = LoginMethod(self.driver)
        self.Member = MemberMethods(self.driver)

    # Test Cases


    @allure.description("Verify Landing Page.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_Landing_memberManagement(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Member.verify_landing(), True, msg="Assertion Failed for Validating Landing Page for Member Management")
        except (TimeoutException, NoSuchElementException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="", attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("Verify Create New User.")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/MemberManagement/TestMemberManagement.xlsx", "createUser"))
    @unpack
    def test_02_create_new_member(self, name, role, email, phone_number, address, password):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Member.create_new_member(name, role, email, phone_number, address, password), True,
                             msg="Assertion Failed for Validating Landing Page for Member Management")
        except (TimeoutException, NoSuchElementException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error_Creating_user", attachment_type=AttachmentType.PNG)
            raise e

    # TODO --- Add new Test case for Editing and Deleting the user

    @allure.description("Verify the edits are reflecting correctly after editing.")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/MemberManagement/TestMemberManagement.xlsx", "editUser"))
    @unpack
    def test_03_edit_member(self, name, role, email, phone_number, address, password, edit_name, edit_role, edit_phone_number):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Member.edit_user_details(name, role, email, phone_number, address, password,
                    edit_name, edit_role, edit_phone_number), True,
                    msg="Assertion Failed for Validating Landing Page for Member Management")
        except (TimeoutException, NoSuchElementException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error_Creating_user", attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("Reset Password a user password after creation.")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/MemberManagement/TestMemberManagement.xlsx", "resetPassword"))
    @unpack
    def test_04_reset_password(self, name, role, email, phone_number, address, password, reset_password):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Member.reset_password(name, role, email, phone_number, address, password, reset_password), True,
                    msg="Assertion Failed for Validating Landing Page for Member Management")
        except (TimeoutException, NoSuchElementException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error_Creating_user", attachment_type=AttachmentType.PNG)
            raise e


    @allure.description("Check Loging after creating an user.")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/MemberManagement/TestMemberManagement.xlsx", "checkLogin"))
    @unpack
    def test_05_login_newMember(self, name, role, email, phone_number, address, password):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Member.checkLogin(name, role, email, phone_number, address, password), True,
                    msg="Assertion Failed for Validating Landing Page for member Roles")
        except (TimeoutException, NoSuchElementException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Error_Creating_user", attachment_type=AttachmentType.PNG)
            raise e

     



    # Closing Method
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            raise e
