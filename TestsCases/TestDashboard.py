import allure
import unittest
from ddt import ddt
from Base.BaseTest import BaseClass
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType
from executions.LoginExecutions.LoginMethods import LoginMethod
from executions.DashboardExecutions.DashboardMethods import DashboardMethod
from selenium.common.exceptions import NoSuchElementException, TimeoutException



@ddt
@allure.feature('DashboardExecutions')
@allure.title('Testing DashboardExecutions Elements')
class TestDashboard(unittest.TestCase, BaseClass):

    # Calling Logger.

    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.Dashboard = DashboardMethod(self.driver)
        self.LoginMethod = LoginMethod(self.driver)


    # Test Cases.
    @allure.description("Checking Total User Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_01_totalUser(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.verify_total_user(),  self.Dashboard.total_user(), msg="Verification of total user tile failed.")
        # Checking if assertion failed

        except (NoSuchElementException, AssertionError, TimeoutException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                attachment_type=AttachmentType.PNG)
            raise e


    @allure.description("Checking Total Order Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_02_totalOrder(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.verify_total_order(), self.Dashboard.get_number_of_orders(), msg="Verification of total order tile failed.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            raise e


    @allure.description("Checking Total Sales Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_03_totalSales(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.verify_total_sales(), "130", msg="Verification of total sales tile failed.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("Checking Total Pending Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_04_totalPending(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.verify_pending(), "0", msg="Verification of total Pending tile failed.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("Checking Active User Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_05_active_user(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.active_user(), "116", msg="Verification of Active user tile failed.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("Checking Inactive User Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_06_inactive_user(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.inactive_user(), "14", msg="Verification of Inactive User tile failed.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("Checking Total user Active User Tiles")
    @allure.severity(allure.severity_level.NORMAL)
    # @data(("frugal@latido.com.np", "Test@123"))
    def test_dashboard_07_sumoftotal_user(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Dashboard.verify_sum_of_total_user(), self.Dashboard.verify_total_user(), msg="Checking sum of total user tile failed.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, Exception) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="TestDashboardScreen",
                          attachment_type=AttachmentType.PNG)
            raise e



    # Closing Method.
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            raise e

