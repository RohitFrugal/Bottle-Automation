import time
import logging

from Pages.InventoryDashboard.InventoryDashboard import InventoryDashboard
from Utilities.utils import Utils


class InventDashboardMethod:
    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver

        self.inventDashboard = InventoryDashboard(driver)
        self.log = Utils.custom_logger(logLevel=logging.INFO)

    # Helper Methods

    # Test Methods

    # Execution Functions
    def execute_info_gather(self):
        self.inventDashboard.click_on_inventDashboard()
        return self.inventDashboard.getTitle()
