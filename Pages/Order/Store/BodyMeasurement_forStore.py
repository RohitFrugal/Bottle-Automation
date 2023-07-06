import logging

from Utilities.utils import Utils
from Pages.Order.OrderPage import OrderPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class BodyMeasurementForStore(OrderPage):
    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Order_module", logLevel=logging.WARNING)

    # Body Measurement
    ITEMSNAEM = (By.XPATH, '//*[@class="ant-select-item-option-content"]')
    BASE_SIZE = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[2]/'
                           'div[2]/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div')
    BODY_TYPE = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[1]/div[2]/div[2]'
                           '/div/div/div/div[1]/div[2]/div/div/div[2]/div/div/div/div/span[1]')
    LENGTH = (By.ID, 'length')
    CHEST = (By.ID, 'chest')
    WAIST = (By.ID, 'waist')
    HIPS = (By.ID, 'hips')
    SHOULDER = (By.ID, 'shoulder')
    SLEEVES = (By.ID, 'sleeves')
    ARMS = (By.ID, 'arms')
    WEIGHT = (By.ID, 'weight')
    FRONT = (By.ID, 'front')
    ARMHOLE = (By.ID, 'armhole')

    # Remarks
    REMARKS = (By.ID, 'remarks')

    # Fill Body Measurement
    def selectBasesize(self, size):
        try:
            return self.HandleDropdown(self.BASE_SIZE, self.ITEMSNAEM, size)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element for Selecting the Base Size : {str(e)}")

    def inputArmhole(self, armhole):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ARMHOLE)).send_keys(armhole)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element to input Armhole : {str(e)}")

    def inputFront(self, front):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.FRONT)).send_keys(front)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element to input Front : {str(e)}")

    def inputShoulder(self, shoulder):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SHOULDER)).send_keys(shoulder)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element to input Shoulder : {str(e)}")

    def inputWeight(self, weight):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.WEIGHT)).send_keys(weight)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element to input Weight : {str(e)}")

    def inputLength(self, length):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.LENGTH)).send_keys(length)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element to input Length : {str(e)}")

    def inputArms(self, arms):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ARMS)).send_keys(arms)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element to input Arms : {str(e)}")

    def inputHips(self, hips):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.HIPS)).send_keys(hips)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element to input Hips : {str(e)}")

    def inputChest(self, chest):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CHEST)).send_keys(chest)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element to input Chest : {str(e)}")

    def inputWaist(self, waist):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.WAIST)).send_keys(waist)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element to input Waist : {str(e)}")

    def inputSleeves(self, sleeves):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SLEEVES)).send_keys(sleeves)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element to input Sleeves : {str(e)}")

    def selectBodyType(self, bodytype):
        try:
            return self.HandleDropdown(self.BODY_TYPE, self.ITEMSNAEM, bodytype)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element to Select Body Type : {str(e)}")

    # Fill Remarks
    def inputRemark(self, remark):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.REMARKS)).send_keys(remark)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Failed to Find the element to input Remarks : {str(e)}")
