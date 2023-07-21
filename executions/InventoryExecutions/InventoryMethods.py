import time
import logging

from Utilities.utils import Utils
from Pages.Inventory.InventoryPage import InventoryPage
from selenium.common.exceptions import NoSuchElementException


def compare(Actual_response, Expected_response):
    print(f"Actual_response : {Actual_response}   --- Expected_response : {Expected_response} ")
    if Actual_response == Expected_response:
        return True
    else:
        return False


class InventoryMethods:
    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.  Inventory = InventoryPage(driver)
        self.log = Utils.custom_logger(module_name='InventoryExecutions', logLevel=logging.INFO)


    # Helper Methods
    def navigate_to_Inventory(self):
        self.Inventory.click_on_inventoryTab()

    def verify_navigate_to_Inventory(self):
        self.Inventory.click_on_inventoryTab()
        return compare(self.Inventory.check_title(), "INVENTORY")

    def check_flag(self, leather_flag, unit):
        if leather_flag == 0:
            self.Inventory.select_unit(unit)
        elif leather_flag == 1:
            self.Inventory.click_leather()

    def fill_category_form(self, ImagePath, name, code, desc, leather_flag, unit):
        self.Inventory.upload_image(ImagePath)
        self.Inventory.enter_name(name)
        self.Inventory.enter_code(code)
        self.Inventory.enter_desc(desc)
        self.check_flag(leather_flag, unit)

    def handle_submission(self):
        try:
            already_present = self.driver.find_element(*self.Inventory.ALREADY_PRESENT)
            if already_present.is_displayed:
                self.log.error(f"Inventory Item already Present in the DB")
                return False
        except NoSuchElementException:
            if "INVENTORY" == self.Inventory.check_title():
                return True



    # Executions Methods
    def AddInventory_Items(self, ImagePath, name, code, desc, leather_flag, unit):
        self.navigate_to_Inventory()
        self.Inventory.click_on_add()
        self.fill_category_form(ImagePath, name, code, desc, leather_flag, unit)
        self.Inventory.click_submit()
        time.sleep(2)
        if self.Inventory.check_submit().is_displayed:
            return True
        else:
            return False

    def selectCarouselItems(self, ItmeName, name, code, sku, tags, color, description, l_quantity, h_quantity, imgPath, brand, weight):
        self.navigate_to_Inventory()
        time.sleep(5)
        self.Inventory.input_search(ItmeName)
        time.sleep(2)
        self.Inventory.selectCategoryItem()
        self.Inventory.click_add_Items()
        self.Inventory.input_item_name(name)
        self.Inventory.input_code(code)
        self.Inventory.input_sku(sku)
        self.Inventory.input_Tags(tags)
        self.Inventory.input_color(color)
        self.Inventory.input_description(description)
        self.Inventory.input_least_quantity(l_quantity)
        self.Inventory.input_high_quantity(h_quantity)
        self.Inventory.upload_primary_img(imgPath)
        time.sleep(5)
        self.Inventory.input_brand(brand)
        self.Inventory.input_weight(weight)
        self.Inventory.item_submit()
        time.sleep(2)
        result = self.handle_submission()
        print(f"Results : {result}")
        return result


    def stockItem_for_normal_item(self, ItemName, productName, vendor_name, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath):
        self.navigate_to_Inventory()
        time.sleep(5)
        print("In Inventory tab now start searching")
        self.Inventory.input_search(ItemName)
        time.sleep(2)
        self.Inventory.selectCategoryItem()
        self.Inventory.getProduct_name(productName)
        self.Inventory.click_on_add_inventory()
        time.sleep(2)
        self.Inventory.select_vendor_name(vendor_name)
        time.sleep(2)
        self.Inventory.enterPrice(price)
        self.Inventory.enter_date(date)
        time.sleep(2)
        self.Inventory.enterQuantity(quantity)
        self.Inventory.selectQuality(quality)
        self.Inventory.selectTransportation_mode(transport_mode)
        self.Inventory.selectPaymentMethod(Pay_mode)
        self.Inventory.enter_received_by(receiver_name)
        self.Inventory.upload_bill(imgPath)
        self.Inventory.click_next()
        self.Inventory.final_submit()
        time.sleep(10)
        return True


    def search_item(self, itemName):
        self.navigate_to_Inventory()
        time.sleep(5)
        self.Inventory.input_search(itemName)
        time.sleep(5)
        return self.Inventory.select_Searched_item(itemName)



