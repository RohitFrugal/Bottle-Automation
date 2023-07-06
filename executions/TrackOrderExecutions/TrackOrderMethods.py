import time
import logging

from Utilities.utils import Utils
from Pages.TrackOrder.TrackOrderPage import TrackOrderPage
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class TrackOrderMethods:
    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.Track = TrackOrderPage(driver)


    def InputOrderID(self, orderID):
        self.Track.click_on_TrackOrder()
        self.Track.sendOrderID(orderID)
        self.Track.clickOnNext()
        time.sleep(5)
        self.Track.getFactoryTitle()
        return self.Track.getCheckFactory()
