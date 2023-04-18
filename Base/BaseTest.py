import os
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager


URL = "https://www.suite.uat.latido.com.np/auth"


class BaseClass:
    driver: webdriver

    def __init__(self):
        self.options = None
        self.service = None
        self.chromedriver_path = None
        self.resources_path = None

    def initialize_driver(self):
        self.service = Service(executable_path=ChromeDriverManager().install())
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.maximize_window()
        self.driver.get(URL)
