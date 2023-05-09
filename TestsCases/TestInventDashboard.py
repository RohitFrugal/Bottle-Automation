import logging
import unittest

import allure
from ddt import ddt, data, unpack
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType

from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from executions.LoginExecutions.LoginMethod import LoginMethod
from executions.InventDashboard.InventDashboardMethods import InventDashboardMethod


@ddt
@allure.feature('Inventory Dashboard')
@allure.title('Fetch Item Status')
class TestInventDashboard(unittest.TestCase, BaseClass):
    og = Utils.custom_logger(logLevel=logging.WARNING)

    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.InventDash = InventDashboardMethod(self.driver)
        self.LoginMethod = LoginMethod(self.driver)

    # Test Case



# *********************************************************************** ONLY FOR Testing the SCRIPT ************************************************************************
    @allure.title(f"Create a new Order for existing Customer")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(*Utils.read_xlsx("../TestData/InventDashboard/InventoryDashboard.xlsx", "Test"))
    # @unpack
    def test_create_order_customer(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.InventDash.execute_info_gather(), "DASHBOARD", msg="Verification Failed to mismatch title.")
        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_for_customer", attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e
# *********************************************************************** ONLY FOR Testing the SCRIPT ************************************************************************



    # Closing Method

    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            self.log.error(f"Failed to close driver. {str(e)}")
            raise e
