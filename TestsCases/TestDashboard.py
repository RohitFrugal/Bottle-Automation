import allure
import logging
import unittest
from ddt import ddt, data, unpack
from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from Pages.DashboardPage import DashboardPage
from allure_commons.types import AttachmentType
from executions.LoginMethod import LoginMethod
from selenium.common import WebDriverException



@ddt
@allure.feature('Dashboard')
@allure.title('Testing Dashboard Elements')
class TestDashboard(unittest.TestCase, BaseClass):

    # Calling Logger.
    log = Utils.custom_logger(logLevel=logging.WARNING)

    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.Dashboard = DashboardPage(self.driver)
        self.LoginMethod = LoginMethod(self.driver)


    # Test Cases.
    @allure.story("Checking Total User Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_totalUser(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.verify_total_user(), "32", msg="Verification of total user tile failed.")

        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e


    @allure.story("Checking Total Order Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_totalOrder(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.verify_total_order(), "82", msg="Verification of total order tile failed.")

        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e


    @allure.story("Checking Total Sales Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_totalSales(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.verify_total_sales(), "32", msg="Verification of total sales tile failed.")

        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    @allure.story("Checking Total Pending Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_totalPending(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.verify_pending(), "0", msg="Verification of total Pending tile failed.")

        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    @allure.story("Checking Active User Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_active_user(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.active_user(), "27", msg="Verification of Active user tile failed.")

        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    @allure.story("Checking Inactive User Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_inactive_user(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.inactive_user(), "5", msg="Verification of Inactive User tile failed.")

        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e

    @allure.story("Checking Total user Active User Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_sumoftotal_user(self):
        self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.verify_sum_of_total_user(), self.Dashboard.verify_total_user(), msg="Checking sum of total user tile failed.")

        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
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

