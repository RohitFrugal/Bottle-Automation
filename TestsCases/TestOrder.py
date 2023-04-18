import logging
import allure
import unittest
from ddt import ddt, data, unpack
from selenium.common import WebDriverException

from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from executions.OrderMethod import OrderMethod
from allure_commons.types import AttachmentType
from executions.LoginMethod import LoginMethod

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
    @allure.story("Verify Order list")
    @allure.severity(allure.severity_level.NORMAL)
    def test_order_list(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Order.verify_navigateToOrder(), "ORDER LISTS", msg="Verification of Order list tile failed.")
        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    @allure.story("Create a Order for Customer ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_order_customer(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Order.createOrder_Customer("9860838858"), "Create Order", msg="Verification of Order list tile failed.")
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    @allure.story("Create a New Customer ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_create_order_new_customer(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Order.create_new_user("9887339699", "Test2 ", "text2@example.com", "2001-12-12", "Siliguri"), "Create Order",
                         msg="Verification Failed to Create a new user.")
        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Test Create new User.",
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
