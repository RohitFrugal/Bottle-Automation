import logging

from selenium import webdriver
from Utilities.utils import Utils
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class LeatherManagementPage:
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Leather_management", logLevel=logging.WARNING)

    # MainPage - Locators
    LEATHER_TAB = (By.ID, "LeatherManagementMenu")
    HEADER_TEXT = (By.XPATH, "//h1[@class='ant-typography product-name']")
    ADD_LEATHER_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-round ant-btn-primary']")

    # Adding a new Leather Locators
    RIGHT_ARROW = (By.XPATH, "(//span[@class='anticon anticon-arrow-right'])[1]")
    NEXT_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']/span[contains(text(), 'Next')]")
    PREVIOUS_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']/span[contains(text(), 'Previous')]")
    ADD_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']/span[contains(text(), 'Add')]")

    # Profile Operation Locators
    EDIT_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-link']/span[@class='anticon anticon-edit']")
    TITLE = (By.XPATH, "//input[@id='title']")
    DATA = (By.XPATH, "//textarea[@id='data']")
    EDIT_OK = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']/span[contains(text(), 'OK')]")

    DELETE_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-link']/span[@class='anticon anticon-delete']")
    CONFIRM_DELETE = (
        By.XPATH, "//button[@class='ant-btn ant-btn-default ant-btn-dangerous']/span[contains(text(), 'Delete')]")

    ADD_NEW_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-link']/span[@class='anticon anticon-plus-circle']")
    ADD_IMG = (By.XPATH, "//input[@accept='image/*']")
    ADD_IMG_OK = (By.XPATH, "(//button[@class='ant-btn ant-btn-primary']/span[contains(text(), 'OK')])[2]")
    TYPE_SELECTOR_DIV = (By.XPATH, "//span[@class='ant-select-selection-item']")

    # Verification - Methods

    # Helper Method
    def clear(self, SELECTOR):
        try:
            self.wait.until(EC.visibility_of_element_located(SELECTOR)).send_keys(Keys.CONTROL + 'a')
            self.wait.until(EC.visibility_of_element_located(SELECTOR)).send_keys(Keys.BACKSPACE)
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find  the Selector image locator : {str(e)} ")

    def select_type_for_add_new_leather_profile(self, type_selector):
        try:
            TYPE_SELECTOR = (By.XPATH, f"//div[contains(@class, 'ant-select-item ant-select-item-option') and contains(@title, '{type_selector}')]")
            self.wait.until(EC.visibility_of_element_located(self.TYPE_SELECTOR_DIV)).click()
            self.wait.until(EC.visibility_of_element_located(TYPE_SELECTOR)).click()
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to locate Type of  Item : {str(e)}")

    def get_profile_Items(self, profile_item_Selector):
        PROFILE = (By.XPATH, f"//div[@class='ant-tabs-tabpane ant-tabs-tabpane-active']/div/div/div[@class='innerSlider']/div/div/div[2]/div/h3[contains(text(), '{profile_item_Selector}')]")
        return self.wait.until(EC.visibility_of_element_located(PROFILE)).click()

    # MainPage-Methods
    def navigate(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.LEATHER_TAB)).click()
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to locate Nav Item : {str(e)}")

    def get_headerText(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.HEADER_TEXT)).text
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to fetch the title Text : {str(e)}")

    def click_on_addLeather(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ADD_LEATHER_BTN)).click()
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to Locate ADD Leather Button : {str(e)}")

    # Add Leather-Page Methods - Buttons
    def click_next(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.NEXT_BTN)).click()
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to Locate Next Button : {str(e)}")

    def click_previous(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.PREVIOUS_BTN)).click()
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to Locate Next Button : {str(e)}")

    def click_add(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ADD_BTN)).click()
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to Locate Add Button : {str(e)}")

    # Profile Operation Methods
    def click_edit_leather_profile(self, title, data):
        try:
            self.wait.until(EC.visibility_of_element_located(self.EDIT_BTN)).click()
            self.clear(self.TITLE)
            self.wait.until(EC.visibility_of_element_located(self.TITLE)).send_keys(title)
            self.clear(self.DATA)
            self.wait.until(EC.visibility_of_element_located(self.DATA)).send_keys(data)
            return self.wait.until(EC.visibility_of_element_located(self.EDIT_OK)).click()
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to Locate Edit Button : {str(e)}")

    def click_delete_leather_profile(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.DELETE_BTN)).click()
            return self.wait.until(EC.visibility_of_element_located(self.CONFIRM_DELETE)).click()
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to Locate DELETE Button : {str(e)}")

    def click_add_leather_profile(self, Type, imgPath, addTitle, addData):
        """
        Create a new item in the selected tab

        **NOTE: Run this before selecting a newly created item from the tab.**

        :param Type: Number representing the profile tab
        :param imgPath: Takes in path to the image
        :param addTitle: Tile of the new Profile
        :param addData: Description
        :return: Creates a new Item in the tab
        """

        try:
            type_selector = {1: "Finish", 2: "Texture", 3: "Aging Process", 4: "Hide Type", 5: "Touch"}

            self.wait.until(EC.visibility_of_element_located(self.ADD_NEW_BTN)).click()
            self.driver.find_element(*self.ADD_IMG).send_keys(imgPath)
            self.wait.until(EC.visibility_of_element_located(self.ADD_IMG_OK)).click()

            self.select_type_for_add_new_leather_profile(type_selector[Type])
            self.wait.until(EC.visibility_of_element_located(self.TITLE)).send_keys(addTitle)
            self.wait.until(EC.visibility_of_element_located(self.DATA)).send_keys(addData)
            return self.wait.until(EC.visibility_of_element_located(self.EDIT_OK)).click()

        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to Locate Add Button : {str(e)}")

    # Operations

    # Getting Leather Profile
    def get_leather(self, name):
        try:
            found_flag = False
            LEATHER_PROFILE = (
                By.XPATH, f"//div[@class='ant-tabs-tabpane ant-tabs-tabpane-active']/div/div/div[@class='innerSlider']"
                          f"/div/div/div[2]/div/h3[contains(text(), '{name}')]")
            Leather = self.wait.until(EC.visibility_of_element_located(LEATHER_PROFILE))
            while not found_flag:
                if Leather.is_displayed():
                    Leather.click()
                    found_flag = True
                    # break
                else:
                    self.wait.until(EC.visibility_of_element_located(self.RIGHT_ARROW)).click()
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to Locate Leather profile : {str(e)}")

    # Getting Item Profile
    def input_details(self, item_selector):
        try:
            self.get_profile_Items(item_selector)
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to Locate Item Profile : {str(e)}")

    # Verification Text
    def check_creation(self, name):
        try:
            MAIN_PAGE_TITLE = (By.XPATH, f"//h3[contains(text(), '{name}')]")
            return self.wait.until(EC.visibility_of_element_located(MAIN_PAGE_TITLE)).text
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to Locate Item Title Locator : {str(e)}")

    def click_item_leather(self, name):
        try:
            MAIN_PAGE_TITLE = (By.XPATH, f"//h3[contains(text(), '{name}')]")
            return self.wait.until(EC.visibility_of_element_located(MAIN_PAGE_TITLE)).click()
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to Locate Item Title Locator : {str(e)}")

    def verify_item_creation(self, itme_field):
        try:
            item_selector = (By.XPATH, f"(//h1[@class='ant-typography'])[{itme_field}]")
            return self.wait.until(EC.visibility_of_element_located(item_selector)).text
        except (TimeoutException, NoSuchElementException, AssertionError, Exception) as e:
            self.log.error(f"Unable to Locate Item Filed Locator : {str(e)}")
