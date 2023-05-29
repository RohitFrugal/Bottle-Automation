import logging
import unittest

import allure
from ddt import ddt, data, unpack
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType

from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from executions.LoginExecutions.LoginMethods import LoginMethod
from executions.OrdersExecutions.OrderMethods import OrderMethod
from selenium.common.exceptions import NoSuchElementException, TimeoutException



@ddt
@allure.feature('Order List')
@allure.title('Order Section Testing')
class TestOrder(unittest.TestCase, BaseClass):
    # Calling Logger.
    log = Utils.custom_logger(logLevel=logging.WARNING)

    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.Order = OrderMethod(self.driver)
        self.LoginMethod = LoginMethod(self.driver)

    # Test Cases
    # Verify Order List.

    @allure.title(f"Create a new Order for existing Customer")
    @allure.story("Create an Order for existing Customer ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/OrderTestData/orderTestCase.xlsx", "forCustomer"))
    @unpack
    def test_create_order_customer(self, username, password, contactNo, gender, productname, leatherProfile,
                                   leatherSize, hardware, lining, polyfill, size, armhole, height, shoulder, weight,
                                   length, arms, hips, chest, waist, sleeves, bodytype, remark, date, OTP):
        self.LoginMethod.nativelogin(self.driver, username, password)
        test_case_name = f"Create a new Order for existing Customer : {contactNo} "
        try:
            self.assertEqual(
                self.Order.createOrder_Customer(contactNo, gender, productname, leatherProfile, leatherSize, hardware,
                                                lining, polyfill, size, armhole, height, shoulder, weight, length, arms,
                                                hips, chest, waist, sleeves, bodytype, remark, date, OTP),
                "Order Succesfully Created", msg="Verification Failed to Create a new Order.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_for_customer",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e
        else:
            allure.attach(self.driver.get_screenshot_as_png(), name=test_case_name,
                          attachment_type=allure.attachment_type.PNG)

    @allure.title(f"Create a new Order for new Customer")
    @allure.story("Create an Order for new Customer ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/OrderTestData/orderTestCase.xlsx", "forNewCustomer"))
    @unpack
    def test_create_new_user_order(self, username, password, contactNo, name, email, dob, address, gender, productname,
                                   leatherProfile, leatherSize, hardware, lining, polyfill, size, armhole, height, shoulder, weight,
                                   length, arms, hips, chest, waist, sleeves, bodytype, remark, date, OTP):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(
                self.Order.create_new_user_order(contactNo, name, email, dob, address, gender, productname,
                                                 leatherProfile, leatherSize, hardware, lining, polyfill, size, armhole, height,
                                                 shoulder, weight, length, arms, hips, chest, waist, sleeves, bodytype, remark,
                                                 date, OTP),
                "Order Succesfully Created", msg="Verification Failed to Create a new Order.")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Creating new Order for new customer.",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    @allure.title("Create a New Order for store")
    @allure.story("Create a New Order for store")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/OrderTestData/orderTestCase.xlsx", "forStore"))
    @unpack
    def test_create_order_store(self, username, password, productname, leatherProfile, leatherSize, hardware, lining,
                                polyfill, size, bodytype, length, chest, waist, hips, shoulder, sleeves, arms, weight, front,
                                armhole, remarks, price, discount, OTP):
        # Login with Admin
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(
                self.Order.createOrder_Store(productname, leatherProfile, leatherSize, hardware, lining, polyfill,
                                             size, bodytype, length, chest, waist, hips, shoulder, sleeves, arms,
                                             weight, front, armhole, remarks, price, discount, OTP),
                "Order Succesfully Created",
                msg="Verification Failed to Create a new user.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Creating order for Store.",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    @allure.title("Checking Order synchronization after creating a new customer order ")
    @allure.story("Checking Order synchronization  ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/OrderTestData/orderTestCase.xlsx", "forSync"))
    @unpack
    def test_check_order_synchronization_for_Customer(self, username, password, contactNo, gender, productname, leatherProfile,
                                   leatherSize, hardware, lining, polyfill, size, armhole, height, shoulder, weight,
                                   length, arms, hips, chest, waist, sleeves, bodytype, remark, date, OTP):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(
                self.Order.navigate_to_customer_order_list(contactNo, gender, productname, leatherProfile, leatherSize, hardware,
                                                lining, polyfill, size, armhole, height, shoulder, weight, length, arms,
                                                hips, chest, waist, sleeves, bodytype, remark, date, OTP), True,
                msg="Verification Failed to Create a new user.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Creating order for Store.",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    @allure.title("Checking Order synchronization after creating a New Order for store")
    @allure.story("Checking Order synchronization  ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/OrderTestData/orderTestCase.xlsx", "forStore"))
    @unpack
    def test_check_order_synchronization_for_Store(self, username, password, productname, leatherProfile, leatherSize, hardware, lining,
                                polyfill, size, bodytype, length, chest, waist, hips, shoulder, sleeves, arms, weight, front,
                                armhole, remarks, price, discount, OTP):
        # Login with Admin
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(
                self.Order.navigate_to_store_order_list(productname, leatherProfile, leatherSize, hardware, lining, polyfill,
                                             size, bodytype, length, chest, waist, hips, shoulder, sleeves, arms,
                                             weight, front, armhole, remarks, price, discount, OTP), True,
                msg="Verification Failed to Create a new user.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Creating order for Store.",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    @allure.title("Search Functionality")
    @allure.story("Search and verify item")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/OrderTestData/orderTestCase.xlsx", "searchInput"))
    @unpack
    def test_Search_functionality(self, username, password, searchValue, productname, leatherProfile, hardware, lining, polyfill):
        # Login with Admin
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:

            # TODO --- Resolve wrong Search Item issue.
            self.assertEqual(
                self.Order.searchBar(searchValue, productname, leatherProfile, hardware, lining, polyfill), True,
                msg="Verification Failed to Create a new user.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Creating order for Store.",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e















    # *********************************************************************** ONLY FOR Testing the SCRIPT ************************************************************************
    # @allure.story("Create a New Customer and Customer Order ")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_create_order_new_customer(self):
    #     self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
    #     try:
    #         self.assertEqual(
    #             self.Order.verify_create_new_user("9907360699", "Test2 ", "test043@example.com", "2001-12-12",
    #                                               "Siliguri"),
    #             "Create Order",
    #             msg="Verification Failed to Create a new user.")
    #     # Checking if assertion failed
    #     except AssertionError as e:
    #         allure.attach(self.driver.get_screenshot_as_png(), name="Test Create new User.",
    #                       attachment_type=AttachmentType.PNG)
    #         self.log.error(f"Assertion failed here while finding element. {str(e)}")
    #         raise e
    #
    #
    # @allure.title("Checking Synchronization for Order List")
    # @allure.story("Create an Order for  Customer ")
    # @allure.severity(allure.severity_level.NORMAL)
    # @data(*Utils.read_xlsx("../TestData/OrderTestData/orderTestCase.xlsx", "forCustomer"))
    # @unpack
    # def test_create_order_customer(self):
    #     self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
    #     test_case_name = f"Create a new Order for existing Customer and checking the Synchronization with Order List"
    #     try:
    #         self.assertEqual(
    #             self.Order.navigate_to_order_list("9860838858", "male", 'Ek (male)', 'Black Sheep', '40', 'Silver',
    #                                               'Black', 'Yes', "32", "6", "6.1", "32", "70", "6.1", "23", "42", "42",
    #                                               "32", "16",
    #                                               "Fit", "Test with Manual Input", "2023-05-26", "0000011"),
    #             True, msg=" Failed to Synchronization with Create List .")
    #     # Checking if assertion failed
    #     except AssertionError as e:
    #         allure.attach(self.driver.get_screenshot_as_png(), name="Creating Order.",
    #                       attachment_type=AttachmentType.PNG)
    #         self.log.error(f"Assertion failed here while finding element. {str(e)}")
    #         raise e
    #     else:
    #         allure.attach(self.driver.get_screenshot_as_png(), name=test_case_name,
    #                       attachment_type=allure.attachment_type.PNG)
    #
    #
    # @allure.title("Create a New Order for store")
    # @allure.story("Create a New Order for store")
    # @allure.severity(allure.severity_level.NORMAL)
    # @data(*Utils.read_xlsx("../TestData/OrderTestData/orderTestCase.xlsx", "forStore"))
    # @unpack
    # def test_create_order_store(self, username, password, productname, leatherProfile, leatherSize, hardware, lining,
    #                             polyfill, size, bodytype, length, chest, waist, hips, shoulder, sleeves, arms, weight, front,
    #                             armhole, remarks, price, discount, OTP):
    #     # Login with Admin
    #     self.LoginMethod.nativelogin(self.driver, username, password)
    #     try:
    #         self.assertEqual(
    #             self.Order.navigate_to_store_order_list(productname, leatherProfile, leatherSize, hardware, lining, polyfill,
    #                                          size, bodytype, length, chest, waist, hips, shoulder, sleeves, arms,
    #                                          weight, front, armhole, remarks, price, discount, OTP), True,
    #             msg="Verification Failed to Create a new user.")
    #
    #     # Checking if assertion failed
    #     except AssertionError as e:
    #         allure.attach(self.driver.get_screenshot_as_png(), name="Creating order for Store.",
    #                       attachment_type=AttachmentType.PNG)
    #         self.log.error(f"Assertion failed here while finding element. {str(e)}")
    #         raise e
    # *********************************************************************** ONLY FOR Testing the SCRIPT ************************************************************************





    # Closing Method.
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            self.log.error(f"Failed to close driver. {str(e)}")
            raise e
