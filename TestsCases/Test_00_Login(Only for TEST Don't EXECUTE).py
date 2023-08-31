import os
import subprocess
import sys
import unittest
import allure
from ddt import ddt, data, unpack
from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from selenium.common import WebDriverException
from allure_commons.types import AttachmentType
from executions.LoginExecutions.LoginMethods import LoginMethod
from selenium.common.exceptions import NoSuchElementException, TimeoutException

@ddt
@allure.feature('Login Page')
@allure.title('Login Test')
class TestLogin(unittest.TestCase):




    browser_list = None

    # -- Getting the browser name from the CMD --
    if len(sys.argv) != 2:
        print("Usage: python test_case.py <browser>")
        sys.exit(1)

    @classmethod
    def setUpClass(cls):
        cls.browser_list = ['chrome', 'firefox']  # Add other browsers here

    def setUp(self):
        self.browser = sys.argv[1]
        self.base = BaseClass(self.browser)
        self.base.initialize_driver(self.browser)
        self.driver = self.base.driver
        self.Login = LoginMethod(self.driver)

    @staticmethod
    def generate_allure_report(browser):
        subprocess.run(['pytest', '-n', 'auto', '--alluredir', f'reports_{browser}', 'Test_00_Login.py::TestLogin'], shell=True)
        allure_report_dir = f'reports_{browser}'
        allure_results_dir = os.path.join(allure_report_dir, 'allure-results')
        allure_report_cmd = f'allure generate {allure_results_dir} -o {allure_report_dir} --clean'
        subprocess.run(allure_report_cmd, shell=True)

    @classmethod
    def tearDownClass(cls):
        for browser in cls.browser_list:
            cls.generate_allure_report(browser)

    def test_LoginSuccessful(self):
        for browser in self.browser_list:
            with self.subTest(browser=browser):
                self.base.initialize_driver(browser)
                self.driver = self.base.driver
                self.Login = LoginMethod(self.driver)
                username, password = "your_username", "your_password"  # Replace with appropriate data
                self.Login.nativelogin(username, password)
                try:
                    self.assertEqual(self.Login.verify_correct_login(), True, msg="Login verification failed.")
                except (NoSuchElementException, AssertionError, TimeoutException, Exception) as e:
                    allure.attach(self.driver.get_screenshot_as_png(), name="test_LoginSuccessful",
                                  attachment_type=AttachmentType.PNG)
                    raise e

if __name__ == '__main__':
    unittest.main()
