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
from selenium.common.exceptions import NoSuchElementException, TimeoutException

@ddt
@allure.feature('Inventory Dashboard')
@allure.title('Fetch Item Status')
class TestVendors(unittest.TestCase, BaseClass):

    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.LoginMethod = LoginMethod(self.driver)
        self.vendor = VendorMethod(self.driver)


    # Verifying landing on Vendor Page
    # @allure.title(f"Verifying landing on Vendor Page")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_landing(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.vendor.gettingStarted(), True,
                             msg="Assertion failed due to missmatch of Vendor Landing Page")
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Verification of landing Page",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element.\n {str(e)}")
            raise e


    # Adding a new Vendor
    # @allure.title(f"Adding a new Vendor")
    @allure.description(f"Adding a new Vendor")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/Vendor/VendorData.xlsx", "addVendor"))
    @unpack
    def test_02_vendor_creation(self, username, password, IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions,
                  contact_name, contact_location, contact_number, contact_email):
        self.LoginMethod.nativelogin(username, password)
        try:
            self.assertEqual(self.vendor.addVendor(IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions,
                  contact_name, contact_location, contact_number, contact_email), True, msg="Adding of Vendor failed!")
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Adding of New Vendor Failed",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element.\n {str(e)}")
            raise e


    # Editing a Vendor details
    # @allure.title(f"Editing a Vendor details")
    @allure.description(f"Editing a Vendor details")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/Vendor/VendorData.xlsx", "editVendor"))
    @unpack
    def test_03_edit_vendor(self, username, password,  IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions,
                         contact_name, contact_location, contact_number, contact_email, edit_vendor_name, edit_vendor_email, edit_vendor_phone):
        self.LoginMethod.nativelogin(username, password)
        try:
            self.assertEqual(self.vendor.edit_vendor(IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions,
                            contact_name, contact_location, contact_number, contact_email, edit_vendor_name, edit_vendor_email, edit_vendor_phone),
                            True, msg="Editing a vendor details failed!")
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Editing a Vendor details Failed",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element.\n {str(e)}")
            raise e



    # Deleting a Vendor
    # @allure.title(f"Deleting a Vendor ")
    @allure.description(f"Deleting a Vendor")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/Vendor/VendorData.xlsx", "deleteVendor"))
    @unpack
    def test_04_delete_vendor(self, username, password, IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location,
                         descriptions, contact_name, contact_location, contact_number, contact_email):
        self.LoginMethod.nativelogin(username, password)
        try:
            self.assertEqual(self.vendor.delete_vendor(IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type,
                            location, descriptions, contact_name, contact_location, contact_number, contact_email),
                             True, msg="Deleting a vendor failed!")
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Deleting a Vendor Failed",
                          attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element.\n {str(e)}")
            raise e



    # # Testing synchronization of a Vendor
    # # TODO
    # """Create a new Vendor and Goto Inventory and re-stock some item with the newly create vendor"""

    # @allure.title(f"Synchronization a Vendor ")
    @allure.description(f"Checking Synchronization of a Vendor after creating a new one ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/Vendor/VendorData.xlsx", "syncVendor"))
    @unpack
    def test_05_sync_vendor(self, username, password, IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type,
                         location, descriptions, contact_name, contact_location, contact_number, contact_email,
                         ItmeName, productName, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath):
        self.LoginMethod.nativelogin(username, password)
        try:
            self.assertEqual(self.vendor.add_stock(IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type,
                            location, descriptions, contact_name, contact_location, contact_number, contact_email,
                            ItmeName, productName, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath),
                             True, msg="Deleting a vendor failed!")
        except (NoSuchElementException, AssertionError, TimeoutException) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Deleting a Vendor Failed",
                          attachment_type=AttachmentType.PNG)
            raise e




    # Closing Method
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            raise e
