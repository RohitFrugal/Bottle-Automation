import logging

from Utilities.utils import Utils
from Pages.Order.OrderPage import OrderPage

from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BodyMeasurement(OrderPage):
    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__(driver)
        self.log = Utils.custom_logger(logLevel=logging.DEBUG)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Body Measurement
    ITEMSNAEM = (By.XPATH, '//*[@class="ant-select-item-option-content"]')
    BASE_SIZE = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[2]/div[3]/div[2]'
                           '/div/div/div/div[1]/div[1]/div/div/div[2]/div/div/div/div')
    ARMHOLE = (By.ID, 'armhole')
    HEIGHT = (By.ID, 'height')
    SHOULDER = (By.ID, 'shoulder')
    WEIGHT = (By.ID, 'weight')
    LENGTH = (By.ID, 'length')
    ARMS = (By.ID, 'arms')
    HIPS = (By.ID, 'hips')
    CHEST = (By.ID, 'chest')
    WAIST = (By.ID, 'waist')
    SLEEVES = (By.ID, 'sleeves')
    BODY_TYPE = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[2]/div[3]/div[2]/div/'
                           'div/div/div[6]/div/div/div/div[2]/div/div/div/div/span[1]')

    # Remarks
    REMARKS = (By.ID, 'remarks')

    # Fill Body Measurement
    def selectBasesize(self, size):
        return self.HandleDropdown(self.BASE_SIZE, self.ITEMSNAEM, size)

    def inputArmhole(self, armhole):
        return self.wait.until(EC.visibility_of_element_located(self.ARMHOLE)).send_keys(armhole)

    def inputHeight(self, height):
        return self.wait.until(EC.visibility_of_element_located(self.HEIGHT)).send_keys(height)

    def inputShoulder(self, shoulder):
        return self.wait.until(EC.visibility_of_element_located(self.SHOULDER)).send_keys(shoulder)

    def inputWeight(self, weight):
        return self.wait.until(EC.visibility_of_element_located(self.WEIGHT)).send_keys(weight)

    def inputLength(self, length):
        return self.wait.until(EC.visibility_of_element_located(self.LENGTH)).send_keys(length)

    def inputArms(self, arms):
        return self.wait.until(EC.visibility_of_element_located(self.ARMS)).send_keys(arms)

    def inputHips(self, hips):
        return self.wait.until(EC.visibility_of_element_located(self.HIPS)).send_keys(hips)

    def inputChest(self, chest):
        return self.wait.until(EC.visibility_of_element_located(self.CHEST)).send_keys(chest)

    def inputWaist(self, waist):
        return self.wait.until(EC.visibility_of_element_located(self.WAIST)).send_keys(waist)

    def inputSleeves(self, sleeves):
        return self.wait.until(EC.visibility_of_element_located(self.SLEEVES)).send_keys(sleeves)

    def selectBodyType(self, bodytype):
        return self.HandleDropdown(self.BODY_TYPE, self.ITEMSNAEM, bodytype)

    # Fill Remarks
    def inputRemark(self, remark):
        return self.wait.until(EC.visibility_of_element_located(self.REMARKS)).send_keys(remark)
