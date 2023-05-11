import time
import logging

from Utilities.utils import Utils
from Pages.TrackOrder.TrackOrderPage import TrackOrderPage


class TrackOrderMethods:
    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver

        self.Track = TrackOrderPage(driver)
        self.log = Utils.custom_logger(logLevel=logging.INFO)

    def InputOrderID(self, orderID):
        self.Track.click_on_TrackOrder()
        self.Track.sendOrderID(orderID)
        self.Track.clickOnNext()
        time.sleep(5)
        return self.Track.getFactoryTitle()
