import logging
import unittest

import allure
from ddt import ddt, data, unpack
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType

from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from executions.LoginExecutions.LoginMethods import LoginMethod
from executions.VendorExecutions.VendorMethod import VendorMethod


@ddt
@allure.feature('Inventory Dashboard')
@allure.title('Fetch Item Status')
class TestVendors(unittest.TestCase, BaseClass):
    log = Utils.custom_logger(logLevel=logging.WARNING)

    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.LoginMethod = LoginMethod(self.driver)
        self.vendor = VendorMethod(self.driver)

    # @allure.title(f"Verifying landing on Vendor Page")
    # @allure.severity(allure.severity_level.NORMAL)
    # def test_landing(self):
    #     self.LoginMethod.nativelogin(self.driver, "frugal@latido.com.np", "Test@123")
    #     try:
    #         self.assertEqual(self.vendor.gettingStarted(), True,
    #                          msg="Assertion failed due to missmatch of Vendor Landing Page")
    #     except AssertionError as e:
    #         allure.attach(self.driver.get_screenshot_as_png(), name="Verification of landing Page",
    #                       attachment_type=AttachmentType.PNG)
    #         self.log.error(f"Assertion failed here while finding element.\n {str(e)}")
    #         raise e

    @allure.title(f"Verifying landing on Vendor Page")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/Vendor/VendorData.xlsx", "addVendor"))
    @unpack
    def test_vendor_creation(self, username, password, IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions,
                  contact_name, contact_location, contact_number, contact_email):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(self.vendor.addVendor(IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions,
                  contact_name, contact_location, contact_number, contact_email), True, msg="Adding of Vendor failed!")
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Adding of New Vendor Failed",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element.\n {str(e)}")
            raise e




    # Closing Method
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            self.log.error(f"Failed to close driver. {str(e)}")
            raise e
