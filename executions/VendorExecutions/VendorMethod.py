import time
import logging

from Pages.Vendors.VendorPage import VendorPage
from Utilities.utils import Utils

class VendorMethod:

# Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.Vendor = VendorPage(driver)
        self.log = Utils.custom_logger(logLevel=logging.INFO)


# Helper Method

    # Verify Methods
    def verify_landing(self):
        self.Vendor.clickOnVendor()
        if self.Vendor.getPageTitle() == "VENDORS":
            return True
        else:
            self.log.error("Vendor Title Page missmatch!")
            return False

    def verify_add_vendor_landing(self):
        if self.Vendor.get_title_text() == "Add  Vendor information":
            return True
        else:
            self.log.error("Add Vendor Title missmatch!")
            return False

    # Filling Vendor Details
    def fill_Vendor_details(self, IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions):
        self.Vendor.upload_vendor_Icon(IconPath)
        self.Vendor.enterVendor_id(vendor_id)
        self.Vendor.enterVendor_name(vendor_name)
        self.Vendor.enterVendor_phone(vendor_phone)
        self.Vendor.enterVendor_email(vendor_email)
        self.Vendor.enterSupplier_type(supply_type)
        self.Vendor.enterLocation(location)
        self.Vendor.enterDescriptions(descriptions)

    def fill_contact_person_details(self, contact_name, contact_location, contact_number, contact_email):
        self.Vendor.enterContactPersonName(contact_name)
        self.Vendor.enterContactPersonLocation(contact_location)
        self.Vendor.enterContactPersonNumber(contact_number)
        self.Vendor.enterContactPersonEmail(contact_email)



    # Execution Methods
    def gettingStarted(self):
        return self.verify_landing()

    def addVendor(self, IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions,
                  contact_name, contact_location, contact_number, contact_email):
        self.Vendor.clickOnVendor()
        self.Vendor.click_on_Add()
        self.fill_Vendor_details(IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions)
        self.fill_contact_person_details(contact_name, contact_location, contact_number, contact_email)
        time.sleep(10)
        self.Vendor.click_on_cancel()
        return self.verify_landing()


