import time
from datetime import datetime
from Pages.Reporting.ReportingPage import ReportingPage
from executions.InventoryExecutions.InventoryMethods import InventoryMethods


# from selenium.common.exceptions import NoSuchElementException, TimeoutException





class ReportMethods:
    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.report = ReportingPage(self.driver)
        self.Inventory = InventoryMethods(self.driver)

    # Helper Methods
    def compare(self, actual_title, expected_title):
        print(f"Actual Title : {actual_title} -- Expected Title : {expected_title}")
        if actual_title == expected_title:
            return True
        else:
            return False

    def convertDate(self, og_date):
        return datetime.strptime(og_date, '%Y-%m-%d').strftime('%b %d, %Y')


    def getResults(self, result):
        if result.__contains__(False):
            return False
        else:
            return True


    # Methods
    def verify_landing(self):
        self.report.navigate()
        # self.report.sort_vendor()
        time.sleep(5)
        return self.compare(self.report.getTitle(), 'REPORTING')

    def check_search(self, searchItem):
        self.report.search_bar(searchItem)


    def create_inventory_check(self, ItemName, productName, vendor_name, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath):
        result = []
        self.Inventory.stockItem_for_normal_item(ItemName, productName, vendor_name, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath)
        self.report.navigate()
        # self.report.sort_vendor()
        time.sleep(5)
        self.driver.refresh()
        updated_date = self.convertDate(date)
        result.append(self.compare(self.report.get_reporting_name(), productName))
        result.append(self.compare(self.report.get_received_date(), updated_date))
        result.append(self.compare(self.report.get_vendor_name(), vendor_name))
        return self.getResults(result)

    def check_details(self, ItemName, productName, vendor_name, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath):
        self.Inventory.stockItem_for_normal_item(ItemName, productName, vendor_name, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath)
        result = []
        self.report.navigate()
        # self.report.sort_vendor()
        time.sleep(3)
        self.driver.refresh()
        self.report.view_more()
        result.append(self.compare(self.report.get_product_type_view_more(), ItemName))
        result.append(self.compare(self.report.get_product_Name_view_more(), productName))
        result.append(self.compare(self.report.get_vendor_Name_view_more(), vendor_name))
        result.append(self.compare(self.report.get_received_date_view_more(), self.convertDate(date)))
        # result.append(self.compare(self.report.get_color_view_more(), 'Black'))
        print(f" {type(self.report.get_quantity_view_more())}  -- {type(quantity)}")
        result.append(self.compare(int(self.report.get_quantity_view_more()), quantity))

        print(f" {type(self.report.get_price_view_more())}  -- {type(price)}")
        result.append(self.compare(int(self.report.get_price_view_more()), price))

        result.append(self.compare((self.report.get_quality_view_more()).capitalize(), quality))

        result.append(self.compare(self.report.get_transportation_mode_view_more(), transport_mode))
        result.append(self.compare(self.report.get_payment_mode_view_more(), Pay_mode))
        result.append(self.compare(self.report.get_received_by_view_more(), receiver_name))

        print(f"Result : {result}")
        return self.getResults(result)






