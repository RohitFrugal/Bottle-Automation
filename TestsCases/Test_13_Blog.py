import allure
import unittest
from Utilities.utils import Utils
from ddt import ddt, data, unpack
from Base.BaseTest import BaseClass
from allure_commons.types import AttachmentType
from executions.BlogExecutions.BlogMethods import BlogMethods
from executions.LoginExecutions.LoginMethods import LoginMethod
from selenium.common.exceptions import NoSuchElementException, TimeoutException, WebDriverException


@ddt
@allure.feature('Blog')
@allure.title('Testing Blog Module')
class TestBlog(unittest.TestCase, BaseClass):

    # SetUp Method.
    def setUp(self):
        super().initialize_driver()
        self.Blog = BlogMethods(self.driver)
        self.LoginMethod = LoginMethod(self.driver)

    # Test Cases
    # Verify BLog List.

    @allure.description("Verify Navigation on Blog")
    @allure.severity(allure.severity_level.NORMAL)
    def test_01_verify_bolg_page(self):
        self.LoginMethod.nativelogin("frugal@latido.com.np", "Test@123")
        try:
            self.assertEqual(self.Blog.test_landing(), True, msg="Verification Failed for Blog Page.")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Failed_for_Blog", attachment_type=AttachmentType.PNG)
            raise e


    @allure.description("Create a new Blog")
    @allure.severity(allure.severity_level.NORMAL)
    @data(*Utils.read_xlsx("../TestData/BlogTestData/blogTestCase.xlsx", "new_blog"))
    @unpack
    def test_02_create_new_blog(self, username, password, shortDescriptions, blog_type, tags, title, style_types, text_contents, list_items, imgPath, imgBlogLayout, imageArrays,  audiClip, caption):
        self.LoginMethod.nativelogin(username, password)
        try:
            self.assertEqual(self.Blog.create_new_blog(shortDescriptions, blog_type, tags, title, style_types, text_contents, list_items, imgPath, imgBlogLayout, imageArrays,  audiClip, caption),
                             True, msg="Verification Failed to Create a new Blog.")
        # Checking if assertion failed
        except (NoSuchElementException, AssertionError, TimeoutException, AttributeError) as e:
            allure.attach(self.driver.get_screenshot_as_png(), name="Creating new blog.", attachment_type=AttachmentType.PNG)
            raise e


    # Closing Method.
    def tearDown(self):
        try:
            self.driver.close()
        except WebDriverException as e:
            raise e
