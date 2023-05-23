import logging
import unittest

import allure
from ddt import ddt, data, unpack
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType

from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from executions.LoginExecutions.LoginMethods import LoginMethod
from executions.InventDashboardExecutions.InventDashboardMethods import InventDashboardMethod


@ddt
@allure.feature('Inventory Dashboard')
@allure.title('Fetch Item Status')
class TestInventDashboard(unittest.TestCase, BaseClass):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.InventDash = InventDashboardMethod(self.driver)
        self.LoginMethod = LoginMethod(self.driver)

    # Test Case

    @allure.title(f"Checking Dashboard data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_inventDash_details(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.InventDash.execute_info_gather(), True, msg="Verification Failed to mismatch title.")
        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_for_customer", attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    @allure.title(f"Comparing Dashboard data with List data for Category")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_inventDash_rp(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.InventDash.get_full_inventory_rpt(), True, msg="Verification Failed to mismatch title.")
        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_for_customer", attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    @allure.title(f"Comparing Dashboard data with List data for Vendors")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_vendor_rpt(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.InventDash.get_full_vendor_rpt(), True, msg="Verification Failed to mismatch title.")
        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_for_customer", attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    # Closing Method

    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            self.log.error(f"Failed to close driver. {str(e)}")
            raise e
