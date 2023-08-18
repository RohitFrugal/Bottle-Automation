import time
from selenium import webdriver
from selenium.webdriver import Keys
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException



URL = "https://www.suite.uat.latido.com.np/auth"
class BaseClass:
    driver: webdriver

    def __init__(self):
        self.log = None
        self.wait = None
        self.options = None
        self.service = None
        self.actionChains = None
        self.resources_path = None
        self.chromedriver_path = None

    def initialize_driver(self):
        # self.service = Service(executable_path=ChromeDriverManager().install())
        self.service = Service(executable_path="E:\POM_for_Bottle\WebApp\resources\chrome.exe")
        self.options = webdriver.ChromeOptions()
        self.driver = webdriver.Chrome(service=self.service, options=self.options)
        self.driver.maximize_window()
        self.driver.get(URL)
        self.actionChains = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)

    def scroll_up(self):
        self.driver.execute_script("window.scrollBy(0, -window.innerHeight);")

    def scroll_down(self):
        self.driver.execute_script("window.scrollBy(0, window.innerHeight);")

    def HandleDropdown(self, dropDownLocator, value, VISIBLE_ELEMENTS, ALL_ITEM_SELECTOR):
        """
        :param dropDownLocator: Dropdown selector - click on Dropdown
        :param value: Selecting Value
        :param VISIBLE_ELEMENTS: First element of the list
        :param ALL_ITEM_SELECTOR: Div selector
        :return : If element is found click
        """
        # Setting up the flags
        itme_found = False

        # Click on the Dropdown
        print("finding the Category selector!")
        time.sleep(3)
        self.driver.find_element(*dropDownLocator).click()

        # Getting to all the elements
        ELEMENTS = self.wait.until(EC.visibility_of_element_located(VISIBLE_ELEMENTS))
        self.actionChains.move_to_element(ELEMENTS).perform()
        elements = self.driver.find_elements(*ALL_ITEM_SELECTOR)
        print(f"List retrieved length : {len(elements)}")

        # Repeat until you find a match
        while True:
            for element in elements:
                try:
                    if element.is_displayed():
                        if value == element.text:
                            print(f"found : {value}.")
                            element.click()
                            itme_found = True
                            break
                except StaleElementReferenceException:
                    print("This is for StaleElementReferenceException")
                    continue
            if itme_found:
                break
            try:
                self.actionChains.send_keys(Keys.ARROW_DOWN).perform()
                elements = self.driver.find_elements(*ALL_ITEM_SELECTOR)
            except NoSuchElementException:
                print("This is for NoSuchElementException")

                break
        if not itme_found:
            print(f"Item not Found {value}.")

    def clear(self, SELECTOR):
        try:
            self.wait.until(EC.visibility_of_element_located(SELECTOR)).send_keys(Keys.CONTROL + 'a')
            self.wait.until(EC.visibility_of_element_located(SELECTOR)).send_keys(Keys.BACKSPACE)
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find  the Selector image locator : {str(e)} ")