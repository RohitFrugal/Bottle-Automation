import logging
import time

from selenium import webdriver
from selenium.webdriver import Keys

from Utilities.utils import Utils
from Base.BaseTest import BaseClass

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException, StaleElementReferenceException


class InventoryPage(BaseClass):
    wait: WebDriverWait
    driver: webdriver

    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__()
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.actionChain = ActionChains(self.driver)
        self.log = Utils.custom_logger(module_name="Inventory", logLevel=logging.DEBUG)


    INVENTORY_TAB = (By.XPATH, "(//a[@id='InventoryMenu'])[1]")
    ADD_INVENTORY = (By.XPATH, "(//span[@class='anticon anticon-plus-circle'])[1]")
    TITLE = (By.XPATH, "//h1[@class='ant-typography product-name']")

    # Add Category
    CATEGORY_IMAGE = (By.XPATH, "//input[@type = 'file']")
    OK_BTN = (By.XPATH, "//button[@class= 'ant-btn ant-btn-primary']/span[contains(text(), 'OK')]")
    CATEGORY_NAME = (By.XPATH, "//input[@id='name']")
    CATEGORY_CODE = (By.XPATH, "//input[@id='code']")
    CATEGORY_DESC = (By.XPATH, "//input[@id='description']")
    LEATHER_UNIT = (By.XPATH, "(//input[@class='ant-checkbox-input'])")
    CATEGORY_UNIT = (By.XPATH, "(//span[@class='ant-select-selection-search'])[2]")
    SUBMIT = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']/span")
    CONFIRM_MSG = (By.XPATH, "//div[@class='ant-notification-notice-message'][contains(text(), 'Category created successfully')]")

    # ERROR MESSAGES
    ALREADY_PRESENT = (By.XPATH, "//div[@class='ant-notification-notice-message'][contains(text(), 'Inventory category Already exists!!!')]")
    REQUIRED_ERR_MSG = (By.XPATH, "//div[@class='ant-form-item-explain-error']")

    # SELECT Category
    CATEGORY_TITLE = (By.XPATH, "(//div[@class='swiper-wrapper']/div[contains(@class, 'swiper-slide')]/div/div[@class='ant-card-body'])/h4")

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
    GET_ITEM_NAME = (By.XPATH, "//h4[@class='ant-typography material_item_name']")



    PRODUCT_IMAGE = (By.XPATH, "//img[@class='material_item_image']")
    ADD_INVENTORY_BUTTON = (By.XPATH, "//button[@type = 'button']")

    # Filling the details
    VENDOR_TBA = (By.XPATH, "(//span[@class= 'ant-select-selection-item'])[1]")
    VENDOR_LIST_CONTAINER = (By.XPATH, "//div[@class='rc-virtual-list-holder-inner']/div")
    ALL_VISIBLE_VENDORS = (By.XPATH, "(//div[contains(@class,'ant-select-item ant-select-item-option')])")


    PRICE = (By.XPATH, "//input[@name='price']")
    DATE = (By.XPATH, "//input[@placeholder='Select date']")
    QUANTITY = (By.XPATH, "(//input[@type='number'])[2]")
    SPECIAL_QUANTITY = (By.XPATH, "(//input[@name='quality'][contains(@value, 'DCM')])")
    QUALITY = (By.XPATH, "(//span[@class='ant-select-selection-item'])[3]")
    TRANSPORTATION_MODE = (By.XPATH, "(//span[@class='ant-select-selection-item'])[4]")
    PAYMENT_METHOD = (By.XPATH, "(//span[@class= 'ant-select-selection-item'])[5]")
    RECEIVED_BY = (By.XPATH, "//input[@name='received_by']")
    BILL = (By.XPATH, "//input[@type='file']")
    NEXT = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")
    FINAL_SUBMIT = (By.XPATH, "(//button[@class='ant-btn ant-btn-primary'])[2]")

    # Search Bar
    SEARCH_BAR = (By.XPATH, "//input[@placeholder='Search Category']")
    ITEM_LIST = (By.XPATH, "//div[@class='ant-card-body']/h4")



    # Helper Methods
    def categorySelector(self, ItemSelector, ItemName):
        all_selected_Item = self.wait.until(EC.presence_of_all_elements_located(ItemSelector))
        for item in all_selected_Item:
            time.sleep(3)
            print(f"This is the Item currently Selected : {item.text}")
            if item.text == ItemName:
                print("Found")
                item.click()
                return True
            break

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
        self.driver.find_element(*dropDownLocator).click()

        # Getting to all the elements
        ELEMENTS = self.wait.until(EC.visibility_of_element_located(VISIBLE_ELEMENTS))
        self.actionChain.move_to_element(ELEMENTS).perform()
        elements = self.driver.find_elements(*ALL_ITEM_SELECTOR)
        print(f"List retrieved length : {len(elements)}")

        # Repeat until you
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
                    continue
            if itme_found:
                break
            try:
                self.actionChain.send_keys(Keys.ARROW_DOWN).perform()
                elements = self.driver.find_elements(*ALL_ITEM_SELECTOR)
            except NoSuchElementException:
                break
        if not itme_found:
            print(f"Item not Found {value}.")

    # Methods

    # Creating a new category
    def check_title(self):
        try:
            time.sleep(2)
            return self.driver.find_element(*self.TITLE).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to check the title : \n {str(e)}")

    def click_on_inventoryTab(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.INVENTORY_TAB)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Navigation to Inventory  : \n {str(e)}")

    def click_on_add(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ADD_INVENTORY)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to click on Add : \n {str(e)}")

    def upload_image(self, imagePath):
        try:
            time.sleep(3)
            self.driver.find_element(*self.CATEGORY_IMAGE).send_keys(imagePath)
            return self.wait.until(EC.visibility_of_element_located(self.OK_BTN)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to upload Image : \n {str(e)}")

    def enter_name(self, name):
        try:
            self.wait.until(EC.visibility_of_element_located(self.CATEGORY_NAME)).click()
            time.sleep(2)
            return self.wait.until(EC.visibility_of_element_located(self.CATEGORY_NAME)).send_keys(name)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input Category name : \n {str(e)}")

    def enter_code(self, code):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CATEGORY_CODE)).send_keys(code)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input Category code : \n {str(e)}")

    def enter_desc(self, description):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CATEGORY_DESC)).send_keys(description)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input descriptions: \n {str(e)}")

    def click_leather(self):
        try:
            return self.driver.find_element(*self.LEATHER_UNIT).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to select leather Unit : \n {str(e)}")

    def select_unit(self, unit):
        try:
            self.wait.until(EC.visibility_of_element_located(self.CATEGORY_UNIT)).click()
            SELECT_UNIT = (By.XPATH, f"//div[@class='ant-select-item-option-content'][contains(text(), '{unit}')]")
            return self.driver.find_element(*SELECT_UNIT).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to select the category Unit : \n {str(e)}")

    def click_submit(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SUBMIT)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Click submit : \n {str(e)}")

    def check_submit(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CONFIRM_MSG))
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Confirm msg element : \n {str(e)}")


    # Select a new category
    def selectCategoryItem(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CATEGORY_TITLE)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Select the Inventory Category : \n {str(e)}")

    def click_add_Items(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ADD_ITEMS)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to add new Item to the Selected Category : \n {str(e)}")


    # Fill form
    def input_item_name(self, name):
        try:
            self.wait.until(EC.visibility_of_element_located(self.ITEM_NAME)).send_keys(name)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input new Item Name to Selected Category : \n {str(e)}")

    def input_code(self, code):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.LATIDO_CODE)).send_keys(code)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input code for Selected Category : \n {str(e)}")

    def input_sku(self, sku):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SKU)).send_keys(sku)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input SKU for Selected Category : \n {str(e)}")

    def input_Tags(self, Tags):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.TAGS)).send_keys(Tags)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input Tags for Selected Category : \n {str(e)}")

    def input_color(self, color):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.COLOR)).send_keys(color)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input color for new Item: \n {str(e)}")

    def input_description(self, description):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.DESCRIPTION)).send_keys(description)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input description for the Selected Category : \n {str(e)}")

    def input_least_quantity(self, l_quantity):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.LEAST_QUANTITY)).send_keys(l_quantity)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input Least quantity for the Selected Category : \n {str(e)}")

    def input_high_quantity(self, h_quantity):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.HIGH_QUANTITY)).send_keys(h_quantity)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input High quantity for the Selected Category : \n {str(e)}")

    def upload_primary_img(self, imgPath):
        try:
            time.sleep(2)
            self.driver.find_element(*self.PRIMARY_IMG).send_keys(imgPath)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Upload Primary Image for Selected Category : \n {str(e)}")


    def input_brand(self, brand):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.BRAND)).send_keys(brand)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input Brand for the Selected Category : \n {str(e)}")

    def input_weight(self, weight):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.WEIGHT)).send_keys(weight)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input weight for the Selected Category : \n {str(e)}")

    def item_submit(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ITEM_SUBMIT)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Submit element : \n {str(e)}")

    # Checking Error's while creating a new Item
    def check_already_present(self):
        try:
            return self.driver.find_element(*self.ALREADY_PRESENT).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to check if already present : \n {str(e)}")

    def check_required_present(self):
        try:
            time.sleep(2)
            return self.wait.until(EC.visibility_of_element_located(self.REQUIRED_ERR_MSG)).text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to check required present : \n {str(e)}")

    # Checking for the Items
    def checkItemStatus(self):
        try:
            status = self.wait.until(EC.visibility_of_element_located(self.ITEM_STATUS)).text
            itemName = self.driver.find_element(*self.GET_ITEM_NAME).text
            print(f"{itemName} is {status}")
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to check status of the Item : \n {str(e)}")

    def getProduct_name(self, productName):
        try:
            PRODUCT_NAME = (By.XPATH, f"//h4[@class='ant-typography material_item_name'][contains(text(), '{productName}')]")
            name = self.wait.until(EC.visibility_of_element_located(PRODUCT_NAME)).text
            print(f'Name of the Product Selected : {name}')
            self.wait.until(EC.visibility_of_element_located(PRODUCT_NAME)).click()
        except {NoSuchElementException, TimeoutException, Exception} as e:
            self.log.error(f"Couldn't find the Element to fetch Product name : \n {str(e)}")


    def click_on_Product_image(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PRODUCT_IMAGE)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to click on Product Image : \n {str(e)}")

    def click_on_add_inventory(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ADD_INVENTORY_BUTTON)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to click on add inventory : \n {str(e)}")

    def select_vendor_name(self, vendor_name):
        try:
            self.HandleDropdown(self.VENDOR_TBA, vendor_name, self.VENDOR_LIST_CONTAINER, self.ALL_VISIBLE_VENDORS)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to select Vendor: \n {str(e)}")

    def enterPrice(self, price):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.PRICE)).send_keys(price)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input Price: \n {str(e)}")

    def enter_date(self, date):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.DATE)).send_keys(date)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to enter Date : \n {str(e)}")

    def enterQuantity(self, quantity):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.QUANTITY)).send_keys(quantity)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to enter the quantity : \n {str(e)}")

    def selectQuality(self, quality):
        try:
            self.wait.until(EC.visibility_of_element_located(self.QUALITY)).click()
            select_quality = (By.XPATH, f"//div[@class='ant-select-item-option-content'][contains(text(), '{quality}')]")
            return self.wait.until(EC.visibility_of_element_located(select_quality)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input Quality: \n {str(e)}")

    def selectTransportation_mode(self, transport_mode):
        try:
            self.wait.until(EC.visibility_of_element_located(self.TRANSPORTATION_MODE)).click()
            TransportMode = (By.XPATH, f"//div[@class='ant-select-item-option-content'][contains(text(), '{transport_mode}')]")
            return self.wait.until(EC.visibility_of_element_located(TransportMode)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Select Transportation mode: \n {str(e)}")

    def selectPaymentMethod(self, Pay_mode):
        try:
            self.wait.until(EC.visibility_of_element_located(self.PAYMENT_METHOD)).click()
            mode = (By.XPATH, f"(//div[@class= 'ant-select-item-option-content'])[contains(text(), '{Pay_mode}')]")
            return self.wait.until(EC.visibility_of_element_located(mode)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to input Payment MethodSS: \n {str(e)}")


    # **********************************
    # Done up to here Move Up from here*
    # **********************************

    def enter_received_by(self, receiver_name):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.RECEIVED_BY)).send_keys(receiver_name)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Input receiver name : \n {str(e)}")

    def upload_bill(self, imgPath):
        try:
            time.sleep(3)
            return self.driver.find_element(*self.BILL).send_keys(imgPath)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Upload Bill : \n {str(e)}")

    def click_next(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.NEXT)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to click Next : \n {str(e)}")

    def final_submit(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.FINAL_SUBMIT)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Click on Submit : \n {str(e)}")

    # Search Bar
    def input_search(self, search_input):
        try:
            return self.driver.find_element(*self.SEARCH_BAR).send_keys(search_input)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Input Search : \n {str(e)}")

    def select_Searched_item(self, search_input):
        try:
            print(f"This is from Select Search item method : {self.categorySelector(self.ITEM_LIST, search_input)}")
            return self.categorySelector(self.ITEM_LIST, search_input)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"No Item fond for the Search Operations: \n {str(e)}")