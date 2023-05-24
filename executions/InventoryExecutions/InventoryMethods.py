import time
import logging
from Utilities.utils import Utils
from Pages.Inventory.InventoryPage import InventoryPage
from selenium.common.exceptions import NoSuchElementException

class InventoryMethods:
    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.  Inventory = InventoryPage(driver)
        self.log = Utils.custom_logger(logLevel=logging.INFO)

    # Helper Methods
    def navigate_to_Inventory(self):
        self.Inventory.click_on_inventoryTab()

    def fill_category_form(self, ImagePath, name, code, desc, unit):
        self.Inventory.upload_image(ImagePath)
        self.Inventory.enter_name(name)
        self.Inventory.enter_code(code)
        self.Inventory.enter_desc(desc)
        self.Inventory.select_unit(unit)

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
    def AddInventory_Items(self, ImagePath, name, code, desc, unit):
        self.navigate_to_Inventory()
        self.Inventory.click_on_add()
        self.fill_category_form(ImagePath, name, code, desc, unit)
        self.Inventory.click_submit()
        time.sleep(50)



    def selectCarouselItems(self, ItmeName, name, code, sku, tags, color, description, l_quantity, h_quantity, imgPath, brand, weight):
        self.navigate_to_Inventory()
        self.Inventory.selectCategoryItem(ItmeName)
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


    def stockItem_for_normal_item(self, ItemName, vendor_name, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath):
        self.navigate_to_Inventory()
        self.Inventory.selectCategoryItem(ItemName)
        self.Inventory.click_on_Product_image()
        self.Inventory.click_on_add_inventory()
        self.Inventory.select_vendor_name(vendor_name)
        self.Inventory.enterPrice(price)
        self.Inventory.enter_date(date)
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
