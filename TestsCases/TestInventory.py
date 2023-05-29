import allure
import logging
import unittest


from Utilities.utils import Utils
from ddt import ddt, data, unpack

from Base.BaseTest import BaseClass
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType

from executions.InventoryExecutions.InventoryMethods import InventoryMethods
from executions.LoginExecutions.LoginMethods import LoginMethod



@ddt
@allure.feature('Inventory')
@allure.title('Testing Inventory Tab')
class TestInventory(unittest.TestCase, BaseClass):
    # Calling Logger.
    log = Utils.custom_logger(logLevel=logging.WARNING)

    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.Inventory = InventoryMethods(self.driver)
        self.LoginMethod = LoginMethod(self.driver)

    # Test Cases


    @allure.title(f"Create a new Category")
    @allure.story("Create a new Category from Add button ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/InventoryData/InventoryTestCase.xlsx", "TestInventory"))
    @unpack
    def test_Add_newCategory(self, username, password, ImagePath, name, code, desc, leather_flag, unit):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(self.Inventory.AddInventory_Items(ImagePath, name, code, desc, leather_flag, unit), True, msg="Adding a New Category Failed ")
        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_for_customer", attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e


    @allure.title(f"Selecting  a new Category")
    @allure.story("Selecting a new Category from Category Carousel ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/InventoryData/InventoryTestCase.xlsx", "ItemCarousel"))
    @unpack
    def test_Add_newCategory_item(self, username, password, ItemName, name, code, sku, tags, color, description, l_quantity, h_quantity, imgPath, brand, weight):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(self.Inventory.selectCarouselItems(ItemName, name, code, sku, tags, color, description, l_quantity, h_quantity, imgPath, brand, weight),
                             True, msg="Adding a New Category Failed ")
        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_for_customer", attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e



    @allure.title(f"Restocking the Items ")
    @allure.story("Selecting a new Category and restocking the Items ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/InventoryData/InventoryTestCase.xlsx", "restocking"))
    @unpack
    def test_restocking_item(self, username, password, ItmeName, vendor_name, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(self.Inventory.stockItem_for_normal_item(ItmeName, vendor_name, price, date, quantity, quality, transport_mode, Pay_mode, receiver_name, imgPath),
                             True, msg="Adding a New Stock Failed ")
        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_Restocking_Items", attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e


    @allure.title(f"Searching the Items ")
    @allure.story("Searching the Items from the search and adding a new Item to it")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/InventoryData/InventoryTestCase.xlsx", "searchItem"))
    @unpack
    def test_search_item(self, username, password, ItmeName):
        self.LoginMethod.nativelogin(self.driver, username, password)
        try:
            self.assertEqual(self.Inventory.search_item(ItmeName),
                             True, msg="Searching a New Stock Item Failed")
        # Checking if assertion failed
        except AssertionError as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_Restocking_Items", attachment_type=AttachmentType.PNG)
            self.log.error(f"Assertion failed here while finding element. {str(e)}")
            raise e


    # Closing Method.
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            self.log.error(f"Failed to close driver. {str(e)}")
            raise e
