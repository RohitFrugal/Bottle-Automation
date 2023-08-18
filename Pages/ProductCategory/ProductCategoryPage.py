import time
import logging
from selenium import webdriver
from Utilities.utils import Utils
from selenium.webdriver import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from selenium.common.exceptions import NoSuchElementException, TimeoutException



class ProductCategoryPage:
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.actionChain = ActionChains(self.driver)
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="ProductCategory_module", logLevel=logging.WARNING)


    # Locators
    PRODUCT_CATEGORY = (By.ID, "ProductCategoryMenu")
    HEADER_TEXT = (By.XPATH, "//h1[contains(text(),  'Product Category')]")

    ADD_NEW_CATEGORY = (By.XPATH, "//button[@class='ant-btn ant-btn-round ant-btn-primary add__button']")

    # Fill Category form
    UPLOAD_IMG = (By.XPATH, "//input[@accept='image/*']")
    OK_BTN_IMG = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']/span[contains(text(), 'OK')]")
    CATEGORY_NAME = (By.ID, "basic_title")
    ADD_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']/span[contains(text(), 'ADD')]")
    UPDATE_BUTTON = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']/span[contains(text(), 'UPDATE')]")

    # Edit Product Category
    PRODUCT_CATEGORY_CONTAINER = (By.XPATH, f"//h5[@class='ant-typography']/div[contains(text(), '')]")
    PRODUCT_EDIT_BTN = (By.XPATH, "//span[@aria-label='edit']")
    PRODUCT_VIEW_BTN = (By.XPATH, "//span[@aria-label='eye']")

    # Status Messages
    CREATED_SUCCESSFUL = (By.XPATH, "//div[@class='ant-message-custom-content ant-message-success']/span[contains(text(), 'ProductCategory created successfully')]")
    UPDATED_SUCCESSFUL = (By.XPATH, "//div[@class='ant-message-custom-content ant-message-success']/span[contains(text(), 'ProductCategory updated successfully')]")
    ERROR = (By.XPATH, "//div[@class='ant-message-custom-content ant-message-error']/span[contains(text(), 'Network Error while creating ProductCategory')]")

    # Sub-Category
    ADD_SUB_CATEGORY_BTN = (By.XPATH, "//button[@class='ant-btn ant-btn-round ant-btn-primary add__button']")


    # Helper Methods
    def clear(self, locator):
        try:
            self.wait.until(EC.element_to_be_clickable(locator)).send_keys(Keys.CONTROL + 'a')
            self.wait.until(EC.element_to_be_clickable(locator)).send_keys(Keys.BACKSPACE)
        except NoSuchElementException as e:
            self.log.error(f"Couldn't find the locator: {e}")


    # General Methods
    def click_on_Category(self):
        try:
            self.wait.until(EC.visibility_of_element_located(self.PRODUCT_CATEGORY)).click()
        except(NoSuchElementException, TimeoutException, AttributeError,Exception) as e:
            self.log.error(f"Unable to find the Navigation Button : {str(e)}")

    def check_header(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.HEADER_TEXT)).text
        except(NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find the Header Text : {str(e)}")


    # Add new Category

    def add_new_Category(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ADD_NEW_CATEGORY)).click()
        except(NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to find the Add New + button : {str(e)}")

    def upload_img(self, imgPath):
        try:
            self.driver.find_element(*self.UPLOAD_IMG).send_keys(imgPath)
            return self.wait.until(EC.visibility_of_element_located(self.OK_BTN_IMG)).click()
        except(NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locator to upload Image : {str(e)}")

    def enter_name(self, name):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CATEGORY_NAME)).send_keys(name)
        except(NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Category Name input box  : {str(e)}")

    def click_on_add(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ADD_BUTTON)).click()
        except(NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Add button : {str(e)}")

    def click_on_update(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.UPDATE_BUTTON)).click()
        except(NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Add button : {str(e)}")

    # Status

    def check_status_successful(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CREATED_SUCCESSFUL)).text
        except(NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Message box  : {str(e)}")

    def check_status_update(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.UPDATED_SUCCESSFUL)).text
        except(NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Message box  : {str(e)}")

    def check_status_error(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ERROR)).text
        except(NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Message box  : {str(e)}")


    # Editing a Category
    def view_button(self, name):
        try:
            view_locator = (By.XPATH, f"//div[@class='ant-card-body'][contains(., '{name}')]/div[@class='hoverable__action']/div/div/span[@aria-label='eye']")
            return self.wait.until(EC.visibility_of_element_located(view_locator)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate view button : {str(e)}")

    def edit_button(self, name):
        try:
            edit_locator = (By.XPATH, f"//div[@class='ant-card-body'][contains(., '{name}')]/div[@class='hoverable__action']/div/div/span[@aria-label='edit']")
            return self.wait.until(EC.visibility_of_element_located(edit_locator)).click()
        except(TimeoutException, NoSuchElementException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate edit button : {str(e)}")

    def edit_category(self, name):
        try:
            PRODUCT_CONTAINER = (By.XPATH, f"//h5[@class='ant-typography']/div[contains(text(), '{name}')]")
            CONTAINER = self.wait.until(EC.visibility_of_element_located(PRODUCT_CONTAINER))
            self.actionChain.move_to_element(CONTAINER).perform()
            time.sleep(2)
            self.edit_button(name)
        except(NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Container box  : {str(e)}")

    def view_category(self, name):
        try:
            PRODUCT_CONTAINER = (By.XPATH, f"//h5[@class='ant-typography']/div[contains(text(), '{name}')]")
            CONTAINER = self.wait.until(EC.visibility_of_element_located(PRODUCT_CONTAINER))
            self.actionChain.move_to_element(CONTAINER).perform()
            time.sleep(2)
            self.view_button(name)
        except(NoSuchElementException, TimeoutException, AttributeError, Exception) as e:
            self.log.error(f"Unable to locate Container box  : {str(e)}")