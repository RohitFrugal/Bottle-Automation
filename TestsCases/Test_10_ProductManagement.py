import allure
import unittest
from Utilities.utils import Utils
from ddt import ddt, data, unpack
from Base.BaseTest import BaseClass
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType
from executions.ProductExecutions.ProductMethods import ProductMethod
from executions.LoginExecutions.LoginMethods import LoginMethod
from selenium.common.exceptions import NoSuchElementException, TimeoutException



@ddt
@allure.feature('Order List')
@allure.title('Order Section Testing')
class TestProductManagement(unittest.TestCase, BaseClass):

    # SetUp Method.
    def setUp(self):
        super().initialize_driver("chrome")
        self.Product = ProductMethod(self.driver)
        self.LoginMethod = LoginMethod(self.driver)

    # Test Cases

    @allure.title(f"Verify Product Management Page")
    @allure.description("To verify Product management page. ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_verify_productManagement_page(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Product.verify_navigate_to_productManagement(), True, msg="Verify Product management landing page")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_Product_management", attachment_type=AttachmentType.PNG)

            raise e

    # @allure.title(f"Add a new Product")
    @allure.description("Adding a new product into the List. ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/ProductManagement/ProductTestData.xlsx", "ProductSheet"))
    @unpack
    def test_02_add_new_product(self, imgPath, name, category, gender, rank, tag, hardware, lining, polyfill_flag, rib_flag, description, sizes,
                        leatherType, sizes_list, price_list, duplicate_leather_list):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(
                self.Product.add_new_product(imgPath, name, category, gender, rank, tag, hardware, lining, polyfill_flag, rib_flag, description, sizes,
                        leatherType, sizes_list, price_list, duplicate_leather_list),
                True, msg="Verify add new Product")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_Product_management", attachment_type=AttachmentType.PNG)
            raise e


    # @allure.title(f"Edit a new Product with Secondary Images ")
    @allure.description("Adding a new product into the List. ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/ProductManagement/ProductTestData.xlsx", "editSheet"))
    @unpack
    def test_03_edit_new_product(self, name, tags, hardware, lining, polyfill_flag, description, secondaryImg):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(
                self.Product.edit_product(name, tags, hardware, lining, polyfill_flag, description, secondaryImg),
                True, msg="Verify add new Product")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_Product_management", attachment_type=AttachmentType.PNG)
            raise e


    # @allure.title(f"Checking the synchronization between the system ")
    @allure.description("Adding a new product into the List. ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/ProductManagement/ProductTestData.xlsx", "synchronization_sheet"))
    @unpack
    def test_04_check_synchronization(self, imgPath, name, category, gender, rank, tag, hardware, lining, polyfill_flag, rib_flag, description, sizes,
                        leatherType, sizes_list, price_list, duplicate_leather_list):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(
                self.Product.check_synchronization(imgPath, name, category, gender, rank, tag, hardware, lining, polyfill_flag, rib_flag, description, sizes,
                        leatherType, sizes_list, price_list, duplicate_leather_list),
                True, msg="Verify add new Product")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_Product_management", attachment_type=AttachmentType.PNG)
            raise e



    # Closing Method.
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            raise e
