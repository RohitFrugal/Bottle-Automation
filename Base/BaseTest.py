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



    def fetch_hidden_elements(self, container_div_xpath, element_xpath):
        """
        Scrolls through the elements of a container div and returns all elements present in the container div.
        The container div xpath and the element xpath should be passed as arguments to the function.
        """
        container_div = self.driver.find_element(container_div_xpath)
        elements = []

        # Scroll until all elements are fetched
        while True:
            # Fetch all elements present in the container div
            elements_present = container_div.find_elements(element_xpath)
            for element in elements_present:
                # Add the element to the list of elements
                elements.append(element)

            # Check if all elements are fetched
            if len(elements) == len(elements_present):
                break

            # Scroll to the bottom of the container div to load more elements
            actions = ActionChains(self.driver)
            actions.move_to_element(container_div)
            actions.click_and_hold()
            actions.perform()
            actions.move_by_offset(0, 100)  # adjust the scroll amount as per your requirement
            actions.release()
            actions.perform()

        return elements
