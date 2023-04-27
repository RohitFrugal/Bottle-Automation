import logging
import unittest

import allure
from ddt import ddt, data, unpack
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType

from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from executions.LoginExecutions.LoginMethod import LoginMethod
from executions.OrdersExecutions.OrderMethods import OrderMethod


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
    # @allure.story("Verify Order list")
    # @allure.severity(allure.severity_level.NORMAL)
    # @data(*Utils.read_xlsx("../TestData/OrderTestData/forCustomer.xlsx", "login"))
    # @unpack
    # def test_order_list(self):
    #     self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
    #     try:
    #         self.assertEqual(self.Order.verify_navigateToOrder(), "ORDER LISTS",
    #                          msg="Verification of Order list tile failed.")
    #     # Checking if assertion failed
    #     except AssertionError as e:
    #         allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
    #                       attachment_type=AttachmentType.PNG)
    #         self.log.error(f"Assertion failed here while finding element. {str(e)}")
    #         raise e
    #
    # @allure.story("Verify Create an Order for Customer ")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_create_order_customer(self):
    #     self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
    #     try:
    #         self.assertEqual(self.Order.verify_createOrder_Customer("9860838858"), "Create Order",
    #                          msg="Verification of Order list tile failed.")
    #     except AssertionError as e:
    #         allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
    #                       attachment_type=AttachmentType.PNG)
    #         self.log.error(f"Assertion failed here while finding element. {str(e)}")
    #         raise e

    # @allure.story("Create a Order for  Customer ")
    # @allure.severity(allure.severity_level.NORMAL)
    # @data(*Utils.read_xlsx("../TestData/OrderTestData/orderTestCase.xlsx", "forCustomer"))
    # @unpack
    # def test_create_order_customer(self, username, password, contactNo, gender, productname, leatherProfile,
    #                                leatherSize, hardware, lining, polyfill, size, armhole, height, shoulder, weight,
    #                                length, arms, hips, chest, waist, sleeves, bodytype, remark, date, OTP):
    #     self.LoginMethod.nativelogin(self.driver, username, password)
    #     try:
    #         self.assertEqual(
    #             self.Order.createOrder_Customer(contactNo, gender, productname, leatherProfile, leatherSize, hardware,
    #                                             lining, polyfill, size, armhole, height, shoulder, weight, length, arms,
    #                                             hips, chest, waist, sleeves, bodytype, remark, date, OTP),
    #             "Order Succesfully Created", msg="Verification Failed to Create a new Order.")
    #     # Checking if assertion failed
    #     except AssertionError as e:
    #         allure.attach(self.driver.get_screenshot_as_png(), name="Creating Order.",
    #                       attachment_type=AttachmentType.PNG)
    #         self.log.error(f"Assertion failed here while finding element. {str(e)}")
    #         raise e

    # @allure.story("Create a Order for  Customer ")
    # @allure.severity(allure.severity_level.NORMAL)
    # # @data(*Utils.read_xlsx("../TestData/OrderTestData/orderTestCase.xlsx", "forCustomer"))
    # # @unpack
    # def test_create_order_customer(self):
    #     self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
    #     try:
    #         self.assertEqual(
    #             self.Order.createOrder_Customer("9860838858", "male", 'Ek (male)', 'Black Sheep', '40', 'Silver', 'Black', 'Yes',
    #                                             "32", "6", "6.1", "32", "70", "6.1", "23", "42", "42", "32", "16", "Fit",
    #                                             "Test with Manual Input", "2023-04-26", "0000011"),
    #             "Order Succesfully Created", msg="Verification Failed to Create a new Order.")
    #     # Checking if assertion failed
    #     except AssertionError as e:
    #         allure.attach(self.driver.get_screenshot_as_png(), name="Creating Order.",
    #                       attachment_type=AttachmentType.PNG)
    #         self.log.error(f"Assertion failed here while finding element. {str(e)}")
    #         raise e


    @allure.story("Create a New Order for store  ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/OrderTestData/orderTestCase.xlsx", "forStore"))
    @unpack
    def test_create_order_store(self, username, password, productname, leatherProfile, leatherSize,	hardware, lining, polyfill,
                                size, bodytype, length,	chest, waist, hips, shoulder, sleeves, arms, weight, front, armhole,
                                remarks, price, discount, OTP):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(
                self.Order.createOrder_Store(productname, leatherProfile, leatherSize,	hardware, lining, polyfill,
                                             size, bodytype, length, chest, waist, hips, shoulder, sleeves, arms, weight, front, armhole,
                                             remarks, price, discount, OTP),
                "Order Succesfully Created", msg="Verification Failed to Create a new user.")

        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Test Create new User.",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    # @allure.story("Create a New Customer ")
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

    # Closing Method.
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            self.log.error(f"Failed to close driver. {str(e)}")
            raise e
