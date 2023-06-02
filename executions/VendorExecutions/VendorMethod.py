import time
import logging

from Pages.Vendors.VendorPage import VendorPage
from Utilities.utils import Utils
from executions.InventoryExecutions.InventoryMethods import InventoryMethods


class VendorMethod:

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.Vendor = VendorPage(driver)
        self.Inventory = InventoryMethods(self.driver)
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

    def validate_create(self):
        if self.Vendor.get_validation_msg() == "Vendor created successfully":
            return True
        elif self.Vendor.get_validation_msg() == "Request failed with status code 409":
            self.log.error("Add Vendor Title missmatch!")
            return False

    def compare(self, compare_list, Org_values_list):
        print(compare_list)

        print(Org_values_list)

        if compare_list == Org_values_list:
            return True
        else:
            return False

    def delete(self, search_item):
        self.Vendor.search(search_item)
        time.sleep(5)
        self.Vendor.delete_vendor()
        if self.Vendor.get_validation_msg() == "Vendor deleted successfully":
            return True


    # Filling Vendor Details
    def fill_Vendor_details(self, IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location,
                            descriptions):
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

    # Editing Vendor details
    def edit_vendor_details(self, vendor_name, vendor_email, vendor_phone):
        self.Vendor.BackSpace(self.Vendor.VENDOR_NAME)
        self.Vendor.enterVendor_name(vendor_name)
        self.Vendor.BackSpace(self.Vendor.VENDOR_PHONE)
        self.Vendor.enterVendor_phone(vendor_phone)
        self.Vendor.BackSpace(self.Vendor.VENDOR_EMAIL)
        self.Vendor.enterVendor_email(vendor_email)
        self.Vendor.click_on_submit()
        time.sleep(2)
        if self.Vendor.get_validation_msg() == "Vendor created successfully":
            self.driver.refresh()
            return True
        else:
            return False



    # Execution Methods
    def gettingStarted(self):
        return self.verify_landing()

    def addVendor(self, IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions, contact_name, contact_location, contact_number, contact_email):
        self.Vendor.clickOnVendor()
        self.Vendor.click_on_Add()
        self.fill_Vendor_details(IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions)
        self.fill_contact_person_details(contact_name, contact_location, contact_number, contact_email)
        self.Vendor.click_on_submit()
        time.sleep(2)
        if self.validate_create():
            self.Vendor.clickOnVendor()
            return self.delete(vendor_name)
        else:
            return False

    def edit_vendor(self, IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions,
                contact_name, contact_location, contact_number, contact_email, edit_vendor_name, edit_vendor_email, edit_vendor_phone):
        self.Vendor.clickOnVendor()
        self.Vendor.click_on_Add()
        self.fill_Vendor_details(IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions)
        self.fill_contact_person_details(contact_name, contact_location, contact_number, contact_email)
        self.Vendor.click_on_submit()
        time.sleep(2)
        if self.validate_create():
            self.Vendor.clickOnVendor()
            self.Vendor.search(vendor_name)
            time.sleep(2)
            self.Vendor.click_on_edit()
            time.sleep(2)
            if self.edit_vendor_details(edit_vendor_name, edit_vendor_email, edit_vendor_phone):
                """ Raise a bug here the success message is wrong """
                edited_values = [edit_vendor_name, edit_vendor_phone, edit_vendor_email]
                if self.compare(edited_values, self.Vendor.get_edit_values()):
                    self.Vendor.clickOnVendor()
                    return self.delete(edit_vendor_name)
                else:
                    return False
            else:
                return False
        else:
            return False

    def delete_vendor(self, IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location,
                    descriptions, contact_name, contact_location, contact_number, contact_email):
        self.Vendor.clickOnVendor()
        self.Vendor.click_on_Add()
        self.fill_Vendor_details(IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions)
        self.fill_contact_person_details(contact_name, contact_location, contact_number, contact_email)
        self.Vendor.click_on_submit()
        time.sleep(2)
        if self.validate_create():
            self.Vendor.clickOnVendor()
            self.Vendor.search(vendor_name)
            time.sleep(2)
            self.Vendor.delete_vendor()
            if self.Vendor.get_validation_msg() == "Vendor deleted successfully":
                return True
            else:
                return False
        else:
            return False

    def add_stock(self, IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions,
                contact_name, contact_location, contact_number, contact_email,
                ItmeName, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath):
        self.Vendor.clickOnVendor()
        self.Vendor.click_on_Add()
        self.fill_Vendor_details(IconPath, vendor_id, vendor_name, vendor_email, vendor_phone, supply_type, location, descriptions)
        self.fill_contact_person_details(contact_name, contact_location, contact_number, contact_email)
        self.Vendor.click_on_submit()
        time.sleep(2)
        if self.validate_create():
            return self.Inventory.stockItem_for_normal_item(ItmeName, vendor_name, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath)
        else:
            return False