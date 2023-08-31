import sys
import threading
import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.firefox import GeckoDriverManager
from webdriver_manager.chrome import ChromeDriverManager
from webdriver_manager.microsoft import EdgeChromiumDriverManager
from selenium.webdriver.chrome.service import Service as BraveService

from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException


URL = "https://www.suite.uat.latido.com.np/auth"
# brave_path = "C:\Program Files\BraveSoftware\Brave-Browser\Application\brave.exe"




class BaseClass:
    _driver_local = threading.local()

    def __init__(self, browser):
        self.log = None
        self.wait = None
        self.options = None
        self.driver = None
        self.service = None
        self.actionChains = None
        self.resources_path = None
        self.chromedriver_path = None

        self.initialize_driver(browser)

    def initialize_driver(self, browser):
        if browser == 'chrome':
            self.service = Service(ChromeDriverManager().install())
            self.options = webdriver.ChromeOptions()
            self.driver = webdriver.Chrome(service=self.service, options=self.options)
            self._driver_local.driver = self.driver

        elif browser == 'Edge':
            self.service = Service(executable_path=EdgeChromiumDriverManager().install())
            self.options = webdriver.EdgeOptions()
            self.driver = webdriver.Edge(service=self.service, options=self.options)
            self._driver_local.driver = self.driver

        elif browser == 'firefox':
            self.options = webdriver.FirefoxOptions()
            self.driver = webdriver.Firefox(executable_path="E:\POM_for_Bottle\WebApp\resources\geckodriver.exe", options=self.options)
            self._driver_local.driver = self.driver

        self.driver.maximize_window()
        self.driver.get(URL)
        self.actionChains = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)