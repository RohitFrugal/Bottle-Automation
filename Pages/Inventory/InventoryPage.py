import logging
import time

from selenium import webdriver

from Utilities.utils import Utils
from Base.BaseTest import BaseClass
from selenium.webdriver import Keys

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains


class InventoryPage(BaseClass):
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.log = Utils.custom_logger(logLevel=logging.DEBUG)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Locators
    INVENTORY_TAB = (By.XPATH, "(//a[@id='InventoryMenu'])[1]")
    ADD_INVENTORY = (By.XPATH, "(//span[@class='anticon anticon-plus-circle'])[1]")
    TITLE = (By.XPATH, "//h1[@class='ant-typography product-name']")


    # Add Category
    CATEGOTY_IMAGE = (By.XPATH, "//input[@type = 'file']")
    OK_BTN = (By.XPATH, "//button[@class= 'ant-btn ant-btn-primary']/span[contains(text(), 'OK')]")
    CATEGORY_NAME = (By.XPATH, "//input[@id='name']")
    CATEGORY_CODE = (By.XPATH, "//input[@id='code']")
    CATEGORY_DESC = (By.XPATH, "//input[@id='description']")
    CATEGORY_UNIT = (By.XPATH, "//span[@class='ant-select-selection-search']")
    SELECT_UNIT = (By.XPATH, "//div[@class='ant-select-item-option-content']")
    SUBMIT = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']/span")

    # ERROR MESSAGES
    ALREADY_PRESENT = (By.XPATH, "//div[@class='ant-notification-notice-message'][contains(text(), 'Inventory Item Already exists!!!')]")
    REQUIRED_ERR_MSG = (By.XPATH, "//div[@class='ant-form-item-explain-error']")

    # SELECT Category
    CATEGORY_TITLE = (By.XPATH, "//div[contains(@class, 'swiper-slide')]/div/div/h4")


    # ADD ITEMS
    ADD_ITEMS = (By.XPATH, "//button[@class='ant-btn ant-btn-ghost material_item_add_button']")
    ITEM_NAME = (By.ID, "item_name")
    LATIDO_CODE = (By.ID, "latido_code")
    SKU = (By.ID, "sku")
    TAGS = (By.XPATH, "//div[@class='ant-select-selection-search']/input")
    COLOR = (By.XPATH, "//input[@name='color']")
    DESCRIPTION = (By.XPATH, "//textarea[@name='description']")
    LEAST_QUANTITY = (By.XPATH, "//input[@id='least_quantity']")
    HIGH_QUANTITY = (By.XPATH, "//input[@id='high_quantity']")
    PRIMARY_IMG = (By.XPATH, "//input[@type='file']")
    BRAND = (By.XPATH, "//input[@id='brand']")
    WEIGHT = (By.XPATH, "//input[@id='weight']")
    ITEM_SUBMIT = (By.XPATH, "//button[@type='submit']/span")


    # Add Stock
    ITEM_STATUS = (By.XPATH, "//div[contains(@class, 'ant-ribbon ant-ribbon-placement-end material_item_badge')]")

    PRODUCT_IMAGE = (By.XPATH, "//img[@class='material_item_image']")
    ADD_INVENTORY_BUTTON = (By.XPATH, "//button[@type = 'button']")

    # Filling the details
    VENDOR_TBA = (By.XPATH, "//span[@class= 'ant-select-selection-item']")
    PRICE = (By.XPATH, "//input[@name='price']")
    DATE = (By.XPATH, "//input[@placeholder='Select date']")
    QUANTITY = (By.XPATH, "(//input[@type='number'])[2]")
    QUALITY = (By.XPATH, "(//span[@class='ant-select-selection-item'])[3]")
    TRANSPORTATION_MODE = (By.XPATH, "(//span[@class='ant-select-selection-item'])[4]")



    # Helper Methods

    def categorySelector(self, ItemSelector, ItemName):
        all_selected_Item = self.wait.until(EC.presence_of_all_elements_located(ItemSelector))

        for item in all_selected_Item:
            if item.text == ItemName:
                item.click()
                break
            else:
                print(f"{item.text} not found")



    # Methods

    # Creating a new category
    def check_title(self):
        time.sleep(2)
        return self.driver.find_element(*self.TITLE).text

    def click_on_inventoryTab(self):
        return self.wait.until(EC.visibility_of_element_located(self.INVENTORY_TAB)).click()

    def click_on_add(self):
        return self.wait.until(EC.visibility_of_element_located(self.ADD_INVENTORY)).click()

    def upload_image(self, imagePath):
        time.sleep(3)
        self.driver.find_element(*self.CATEGOTY_IMAGE).send_keys(imagePath)
        return self.wait.until(EC.visibility_of_element_located(self.OK_BTN)).click()

    def enter_name(self, name):
        return self.wait.until(EC.visibility_of_element_located(self.CATEGORY_NAME)).send_keys(name)

    def enter_code(self, code):
        return self.wait.until(EC.visibility_of_element_located(self.CATEGORY_CODE)).send_keys(code)

    def enter_desc(self, description):
        return self.wait.until(EC.visibility_of_element_located(self.CATEGORY_DESC)).send_keys(description)

    def select_unit(self, unit):
        self.wait.until(EC.visibility_of_element_located(self.CATEGORY_UNIT)).click()
        SELECT_UNIT = (By.XPATH, f"//div[@class='ant-select-item-option-content'][contains(text(), '{unit}')]")
        return self.wait.until(EC.visibility_of_element_located(self.SELECT_UNIT)).click()

    def click_submit(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUBMIT)).click()

    # Select a new category
    def selectCategoryItem(self, ItemName):
        return self.categorySelector(self.CATEGORY_TITLE, ItemName)

    def click_add_Items(self):
        return self.wait.until(EC.visibility_of_element_located(self.ADD_ITEMS)).click()


    # Fill form
    def input_item_name(self, name):
        self.wait.until(EC.visibility_of_element_located(self.ITEM_NAME)).send_keys(name)

    def input_code(self, code):
        return self.wait.until(EC.visibility_of_element_located(self.LATIDO_CODE)).send_keys(code)

    def input_sku(self, sku):
        return self.wait.until(EC.visibility_of_element_located(self.SKU)).send_keys(sku)

    def input_Tags(self, Tags):
        return self.wait.until(EC.visibility_of_element_located(self.TAGS)).send_keys(Tags)

    def input_color(self, color):
        return self.wait.until(EC.visibility_of_element_located(self.COLOR)).send_keys(color)

    def input_description(self, description):
        return self.wait.until(EC.visibility_of_element_located(self.DESCRIPTION)).send_keys(description)

    def input_least_quantity(self, l_quantity):
        return self.wait.until(EC.visibility_of_element_located(self.LEAST_QUANTITY)).send_keys(l_quantity)

    def input_high_quantity(self, h_quantity):
        return self.wait.until(EC.visibility_of_element_located(self.HIGH_QUANTITY)).send_keys(h_quantity)

    def upload_primary_img(self, imgPath):
        time.sleep(2)
        self.driver.find_element(*self.PRIMARY_IMG).send_keys(imgPath)

    def input_brand(self, brand):
        return self.wait.until(EC.visibility_of_element_located(self.BRAND)).send_keys(brand)

    def input_weight(self, weight):
        return self.wait.until(EC.visibility_of_element_located(self.WEIGHT)).send_keys(weight)

    def item_submit(self):
        return self.wait.until(EC.visibility_of_element_located(self.ITEM_SUBMIT)).click()

    # Checking Error's while creating a new Item
    def check_already_present(self):
        return self.driver.find_element(*self.ALREADY_PRESENT).text

    def check_required_present(self):
        time.sleep(2)
        return self.wait.until(EC.visibility_of_element_located(self.REQUIRED_ERR_MSG)).text


    # Checking for the Items
    def checkItemStatus(self):
        status = self.wait.until(EC.visibility_of_element_located(self.ITEM_STATUS)).text
        print(status)
        return status

    def click_on_Product_image(self):
        return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_IMAGE)).click()

    def click_on_add_inventory(self):
        return self.wait.until(EC.visibility_of_element_located(self.ADD_INVENTORY_BUTTON)).click()

    def enter_vendor_name(self, vendor_name):
        self.wait.until(EC.visibility_of_element_located(self.VENDOR_TBA)).click()
        VENDOR_NAME = (By.XPATH, f"//div[@class= 'ant-select-item-option-content'][contains(text(), '{vendor_name}')]")
        return self.wait.until(EC.visibility_of_element_located(VENDOR_NAME)).click()

    def enterPrice(self, price):
        return self.wait.until(EC.visibility_of_element_located(self.PRICE)).send_keys(price)

    def enter_date(self, date):
        return self.wait.until(EC.visibility_of_element_located(self.DATE)).send_keys(date)

    def enterQuantity(self, quantity):
        return self.wait.until(EC.visibility_of_element_located(self.QUANTITY)).send_keys(quantity)

    def selectQuality(self, quality):
        self.wait.until(EC.visibility_of_element_located(self.QUALITY)).click()
        select_quality = (By.XPATH, f"//div[@class='ant-select-item-option-content'][contains(text(), '{quality}')]")
        return self.wait.until(EC.visibility_of_element_located(select_quality)).click()

    def selectTransportation_mode(self):
        self.wait.until(EC.visibility_of_element_located(self.TRANSPORTATION_MODE)).click()
        return self.wait.until(EC.visibility_of_element_located(self.TRANSPORTATION_MODE)).send_keys(Keys.ENTER)

    # -- TODO Make Payment Methods and add Billing sections
