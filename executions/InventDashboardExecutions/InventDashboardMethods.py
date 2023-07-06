import time
import logging

from Pages.InventoryDashboard.InventoryDashboardPage import InventoryDashboard
from Utilities.utils import Utils


class InventDashboardMethod:
    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver

        self.inventDashboard = InventoryDashboard(driver)

    # Helper Methods
    def navigate_toDashboard(self):
        return self.inventDashboard.click_on_inventDashboard()


    def compare(self, cardValue, listValue):
        print(f"Card Value : {type(cardValue)} :: List Value : {type(listValue)} ")
        print(f"Card Value : {cardValue} :: List Value : {listValue} ")
        if cardValue == listValue:
            return True
        else:
            return False

    # Test Methods
    def compare_result(self, result):
        if result.__contains__(False):
            return False
        else:
            return True

    # Execution Functions
    def execute_info_gather(self):
        self.navigate_toDashboard()
        print("============================= In-Stock Items list ==============================")
        print(f"In-Stock Items : {self.inventDashboard.fetch_InStock()}")

        print("============================= Alarming Stock list ==============================")
        print(f"Alarming Stock : {self.inventDashboard.fetch_AlarmingStock()}")

        print("============================= Out of Stock list ==============================")
        print(f"Out of Stock : {self.inventDashboard.fetch_OutOfStock()}")

        print("============================= Compare list ==============================")
        print(f"Out of Stock Item List : {self.inventDashboard.fetch_OutOfStock_list()}")


        print(f"Alarming Stock Item List : {self.inventDashboard.fetch_AlarmingStock_list()}")

        result = []

        alarmingStock = self.inventDashboard.fetch_AlarmingStock()
        alarmingStockList = self.inventDashboard.fetch_AlarmingStock_list()
        result.append(self.compare(alarmingStock, alarmingStockList))
        print(f"Result for alarming Stock : {result}")

        outOfStock = self.inventDashboard.fetch_OutOfStock()
        outOfStockList = self.inventDashboard.fetch_OutOfStock_list()
        result.append(self.compare(outOfStock, outOfStockList))
        print(f"Result for Out of Stock : {result}")


        self.inventDashboard.click_on_showMore_OutOfStock()
        OutofStock_ItemCount = self.inventDashboard.check_outOfStockList()
        result.append(self.compare(outOfStockList, OutofStock_ItemCount))
        print(f"Result for Show More Out Of Stock : {result}")


        self.inventDashboard.click_on_showMore_AlarmingStock()
        AlarmingStock_ItemCount = self.inventDashboard.check_alarmingStock()
        result.append(self.compare(alarmingStockList, AlarmingStock_ItemCount))
        print(f"Result for Show More Alarming Stock : {result}")



        # print(f"Items is Result List: {result}")
        return self.compare_result(result)

    def get_full_inventory_rpt(self):
        self.navigate_toDashboard()
        invent_dashboard = self.inventDashboard.get_category_details()
        self.inventDashboard.click_on_Category_viewmore()
        inventory_tab = self.inventDashboard.get_inventory_item_details()
        return self.compare(invent_dashboard, inventory_tab)

    def get_full_vendor_rpt(self):
        self.navigate_toDashboard()
        vendor_dashboard = self.inventDashboard.get_vendor_details()
        self.inventDashboard.click_on_Vendor_viewmore()
        vendor_tab = self.inventDashboard.get_vendorTab_details()
        return self.compare(vendor_dashboard, vendor_tab)






