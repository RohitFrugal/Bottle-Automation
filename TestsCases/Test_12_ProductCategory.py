import allure
import unittest
from Utilities.utils import Utils
from ddt import ddt, data, unpack
from Base.BaseTest import BaseClass
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType
from executions.ProductCategoryExecutions.ProductCategoryMethod import ProductCategoryMethod
from executions.LoginExecutions.LoginMethods import LoginMethod
from selenium.common.exceptions import NoSuchElementException, TimeoutException


@ddt
@allure.feature('Product Category')
class TestProductCategory(unittest.TestCase, BaseClass):

    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.LoginMethod = LoginMethod(self.driver)
        self.category = ProductCategoryMethod(self.driver)

    # Test Cases

    @allure.description("To verify Product Category page. ")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_verify_landingProduct_Category_page(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.category.test_navigation(), True,
                             msg="Verify Product Category landing page")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_Product_Category",
                          attachment_type=AttachmentType.PNG)
            raise e


    @allure.description("To verify Add new Product Category. ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/ProductCategory/TestProductCategory.xlsx", "add_category"))
    @unpack
    def test_02_add_new_product_category(self, imgPath, name):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.category.test_add_new_category(imgPath, name), True,
                             msg="Verify Failed to Add new Product Category")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_Product_Category",
                          attachment_type=AttachmentType.PNG)
            raise e


    # TODO -- Add a scroll when not able to find an Item category.


    @allure.description("To verify edit Product Category. ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/ProductCategory/TestProductCategory.xlsx", "edit_category"))
    @unpack
    def test_03_edit_product_category(self, name, edit_name):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.category.test_edit_category(name, edit_name), True,
                             msg="Verify Failed to edit Product Category page")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_Product_Category",
                          attachment_type=AttachmentType.PNG)
            raise e


    @allure.description("To verify Add new Product Sub-Category. ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/ProductCategory/TestProductCategory.xlsx", "add_subCategory"))
    @unpack
    def test_04_add_product_subcategory(self, main_category, imgPath, sub_Category_name):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.category.test_add_Subcategory(main_category, imgPath, sub_Category_name), True,
                             msg="Verify Failed to add new sub-category page")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_Product_Category",
                          attachment_type=AttachmentType.PNG)
            raise e


    @allure.description("To verify edit Product Sub-category. ")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/ProductCategory/TestProductCategory.xlsx", "edit_subCategory"))
    @unpack
    def test_05_edit_product_subcategory(self, main_category, sub_category, edit_name):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.category.test_edit_Subcategory(main_category, sub_category, edit_name), True,
                             msg="Verify Failed to edit Product SUb-category page")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="verify_Product_Category",
                          attachment_type=AttachmentType.PNG)
            raise e


    # Closing Method.
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            raise e
