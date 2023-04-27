import time
import logging


from Utilities.utils import Utils
from selenium.webdriver import Keys
from Pages.Order.OrderPage import OrderPage


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class Payments(OrderPage):
    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__(driver)
        self.log = Utils.custom_logger(logLevel=logging.DEBUG)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    # Payments
    TOTAL_AMOUNT = (By.ID, 'total_amount')
    DISCOUNT = (By.ID, 'discount')
    TYPE = (By.ID, 'rc_select_19')
    ADVANCE = (By.ID, 'advance')
    LEFT_TO_PAY = (By.ID, 'reminning_amonut')
    DELIVER_DATE = (By.ID, 'delivery_date')

    # Button
    CANCEL_BTN = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[3]/button[1]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[3]/button[2]')


    # OTP Input field
    OTPHEADER = (By.ID, 'rc_unique_0')
    getOTPText = (By.XPATH, '//*[@id="rc_unique_0"]')
    OTP_INPUT = (By.XPATH, '/html/body/div[14]/div/div[2]/div/div[2]/div[2]/form/input')
    OTP_SUBMIT = (By.XPATH, '/html/body/div[14]/div/div[2]/div/div[2]/div[3]/button[2]')

    # Verify Submit Order
    VERIFY_ORDER_TEXT = (By.XPATH, '/html/body/div[15]/div/div[2]/div/div[2]/div/div[2]/h3')


    # Fill Payments
    def gettotalamount(self):
        return self.wait.until(EC.visibility_of_element_located(self.TOTAL_AMOUNT)).text
    def inputDiscount(self, discountPrice):
        return self.wait.until(EC.visibility_of_element_located(self.DISCOUNT)).send_keys(discountPrice)
    def inputAdvance(self, advanceAmount):
        return self.wait.until(EC.visibility_of_element_located(self.ADVANCE)).send_keys(advanceAmount)
    def inputLefttopay(self, left_amount):
        return self.wait.until(EC.visibility_of_element_located(self.LEFT_TO_PAY)).send_keys(left_amount)
    def sendDeliveryDate(self, date):
        date_str = str(date)
        self.wait.until(EC.visibility_of_element_located(self.DELIVER_DATE)).send_keys(date_str)
        return self.wait.until(EC.visibility_of_element_located(self.DELIVER_DATE)).send_keys(Keys.ENTER)
    def cancel(self):
        return self.wait.until(EC.visibility_of_element_located(self.CANCEL_BTN)).click()
    def submitOrder(self):
        return self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BTN)).click()


    # Fill OTP
    def click_on_OTP_Header(self):
        OTP_Text = self.wait.until(EC.presence_of_element_located(self.getOTPText)).text
        self.log.info(f"I got text here before the click {OTP_Text}")
        return self.wait.until(EC.presence_of_element_located(self.OTPHEADER)).click()
    def enterOTP(self, OTP):
        str_OTP = str(OTP)
        self.driver.find_element(*self.OTP_INPUT).click()
        time.sleep(4)
        return self.driver.find_element(*self.OTP_INPUT).send_keys(str_OTP)

    def submitOTP(self):
        time.sleep(4)
        return self.wait.until(EC.visibility_of_element_located(self.OTP_SUBMIT)).click()

    # Verify Submit
    def verifyOrderSubmit(self):
        verify_order_text = self.wait.until(EC.visibility_of_element_located(self.VERIFY_ORDER_TEXT)).text
        print(verify_order_text)
        return verify_order_text
