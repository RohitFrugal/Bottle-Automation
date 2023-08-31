import logging
import unittest

import allure
from ddt import ddt
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType

from Base.BaseTest import BaseClass
from executions.LoginExecutions.LoginMethods import LoginMethod
from executions.InventDashboardExecutions.InventDashboardMethods import InventDashboardMethod
from selenium.common.exceptions import NoSuchElementException, TimeoutException

@ddt
@allure.feature('Inventory Dashboard')
@allure.title('Fetch Item Status')
class TestInventDashboard(unittest.TestCase, BaseClass):

    # SetUp Method.
    def setUp(self):
        super().initialize_driver("chrome")
        self.InventDash = InventDashboardMethod(self.driver)
        self.LoginMethod = LoginMethod(self.driver)

    # Test Case

    # @allure.title(f"Checking Dashboard data")
    @allure.description(f"Checking Dashboard data")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_inventDash_details(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.InventDash.execute_info_gather(), True, msg="Verification Failed to mismatch data.")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_for_customer", attachment_type=AttachmentType.PNG)
            raise e

    # @allure.title(f"Comparing Dashboard data with List data for Category")
    @allure.description(f"Comparing Dashboard data with List data for Category")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_inventDash_rp(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.InventDash.get_full_inventory_rpt(), True, msg="Verification Failed to mismatch title.")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_for_customer", attachment_type=AttachmentType.PNG)
            raise e

    # @allure.title(f"Comparing Dashboard data with List data for Vendors")
    @allure.description(f"Comparing Dashboard data with List data for Vendors")
    @allure.severity(allure.severity_level.NORMAL)
    def test_get_vendor_rpt(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.InventDash.get_full_vendor_rpt(), True, msg="Verification Failed to mismatch title.")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_for_customer", attachment_type=AttachmentType.PNG)
            raise e

    # Closing Method

    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            raise e
