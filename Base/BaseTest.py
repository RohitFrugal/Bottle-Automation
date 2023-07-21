import time

from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.wait import WebDriverWait
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://www.suite.uat.latido.com.np/auth"


class BaseClass:
    driver: webdriver

    def __init__(self):
        self.log = None
        self.wait = None
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
        self.wait = WebDriverWait(self.driver, 10)

    def page_scroll(self):
        pageLength = self.driver.execute_script(
            "window.scrollTo(0,document.body.scrollHeight);var pageLength=document.body.scrollHeight")
        match = False
        while not match:
            lastCount = pageLength
            time.sleep(3)
            pageLength = self.driver.execute_script(
                "window.scrollTo(0,document.body.scrollHeight);var pageLength=document.body.scrollHeight")
            if lastCount == pageLength:
                match = True
        time.sleep(4)



