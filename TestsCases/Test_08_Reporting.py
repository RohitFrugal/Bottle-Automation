import allure
import unittest
from ddt import ddt, data, unpack
from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType
from executions.LoginExecutions.LoginMethods import LoginMethod
from executions.ReportingExecutions.ReportingMethods import ReportMethods
from selenium.common.exceptions import NoSuchElementException, TimeoutException



@ddt
@allure.feature('Reporting Module Test Cases')
@allure.title('Testing Reporting Elements')
class TestReporting(unittest.TestCase, BaseClass):


    # SetUp Method.
    def setUp(self):

        super().initialize_driver("chrome")
        self.LoginMethod = LoginMethod(self.driver)
        self.Report = ReportMethods(self.driver)



    # Test Cases.
    @allure.description("Verify Landing on Reporting Page.")
    @allure.severity(allure.severity_level.NORMAL)
    def test_landing(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Report.verify_landing(), True, msg="Verification failed! for Report Landing.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify Report Landing ", attachment_type=AttachmentType.PNG)
            raise e


    @allure.description("Check for new Entry")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/ReportData/Report.xlsx", "checkReport"))
    @unpack
    def test_01_new_entry_list(self, ItemName, productName, vendor_name, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Report.create_inventory_check(ItemName, productName, vendor_name, price, date, quantity, quality,
                    transport_mode, Pay_mode, receiver_name, imgPath),
                    True, msg="Verification failed! for Report List.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify Report Landing ", attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("Check for View more Details")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/ReportData/Report.xlsx", "viewMore"))
    @unpack
    def test_02_new_entry(self, ItemName, productName, vendor_name, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Report.check_details(ItemName, productName, vendor_name, price, date, quantity, quality,
                    transport_mode, Pay_mode, receiver_name, imgPath),
                    True, msg="Verification failed! for Details Page.")

        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify Report Landing ", attachment_type=AttachmentType.PNG)
            raise e


    # Closing Method.
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            raise e
