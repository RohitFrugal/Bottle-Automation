import allure
import unittest
from Utilities.utils import Utils
from ddt import ddt, data, unpack
from Base.BaseTest import BaseClass
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType
from executions.LeatherExecutions.LeatherMethods import LeatherMethod
from executions.LoginExecutions.LoginMethods import LoginMethod
from executions.InventoryExecutions.InventoryMethods import InventoryMethods
from selenium.common.exceptions import NoSuchElementException, TimeoutException


@ddt
@allure.feature('Leather Management')
class TestLeatherManagement(unittest.TestCase, BaseClass):

    # SetUp Method.
    def __init__(self, methodName: str = ...):
        super().__init__(methodName)

    def setUp(self):
        super().initialize_driver()
        self.Leather = LeatherMethod(self.driver)
        self.LoginMethod = LoginMethod(self.driver)
        self.Inventory = InventoryMethods(self.driver)

    # Test Cases

    @allure.description("To verify Leather Management page. ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_verify_leatherManagement_page(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Leather.verify_navigate_to_leatherManagement(), True,
                             msg="Verify Leather management landing page")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_Leather_management",
                          attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("Adding a new Leather into the List. ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/LeatherManagement/LeatherTestData.xlsx", "addLeather"))
    @unpack
    def test_02_add_new_Leather(self, ImagePath, ItemCategoryName, codeName, desc, leather_flag, unit, code,  sku, tags, color, description, l_quantity, h_quantity, leather_flg, imgPath, leather_ball_imgPath, brand, weight,
                                finish, texture, aging, hide, touch,):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.Inventory.AddInventory_Items(ImagePath, ItemCategoryName, codeName, desc, leather_flag, unit)
            self.Inventory.selectCarouselItems(ItemCategoryName, codeName, code, sku, tags, color, description,
                                               l_quantity, h_quantity, leather_flg, imgPath, leather_ball_imgPath, brand, weight),

            self.assertEqual(self.Leather.add_new_Leather(codeName, finish, texture, aging, hide, touch),
                             True, msg="Verify add new Leather")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_Leather_management",
                          attachment_type=AttachmentType.PNG)
            raise e

    @allure.description("verification of newly created Leather into the List. ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/LeatherManagement/LeatherTestData.xlsx", "synchronization"))
    @unpack
    def test_03_check_synchronization(self, leather_name, finish, texture, aging_process, hide_type, touch):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Leather.check_synchronization(leather_name, finish, texture, aging_process, hide_type, touch),
                             True, msg="Verify add new Leather")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_Leather_management", attachment_type=AttachmentType.PNG)
            raise e


    # Closing Method.
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            raise e
