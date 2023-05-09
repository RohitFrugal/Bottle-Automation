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
    OTP_INPUT = (By.XPATH, '//form/input[@class="ant-input input-field"]')
    OTP_SUBMIT = (By.XPATH, '//div[@class="ant-modal-footer"]/button[2][@class="ant-btn ant-btn-primary"]/span')

    # Verify Submit Order
    VERIFY_ORDER_TEXT = (By.XPATH, '//div[2][@class="ant-row ant-row-center"]/h3')


    # Fill Payments
    def gettotalamount(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.TOTAL_AMOUNT)).text
        except Exception as e:
            self.log.error(f"Failed to get Total Amount {str(e)}")
    def inputDiscount(self, discountPrice):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.DISCOUNT)).send_keys(discountPrice)
        except Exception as e:
            self.log.error(f"Failed to input Discount amount {str(e)}")
    def inputAdvance(self, advanceAmount):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.ADVANCE)).send_keys(advanceAmount)
        except Exception as e:
            self.log.error(f"Failed to input Advance amount {str(e)}")

    def inputLefttopay(self, left_amount):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.LEFT_TO_PAY)).send_keys(left_amount)
        except Exception as e:
            self.log.error(f"Failed to input Amount ot Pay {str(e)}")
    def sendDeliveryDate(self, date):
        try:
            date_str = str(date)
            self.wait.until(EC.visibility_of_element_located(self.DELIVER_DATE)).send_keys(date_str)
            return self.wait.until(EC.visibility_of_element_located(self.DELIVER_DATE)).send_keys(Keys.ENTER)
        except Exception as e:
            self.log.error(f"Failed to input  Delivery date {str(e)}")
    def cancel(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CANCEL_BTN)).click()
        except Exception as e:
            self.log.error(f"Failed to click on Cancel button {str(e)}")
    def submitOrder(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BTN)).click()
        except Exception as e:
            self.log.error(f"Failed to Click on Submit button {str(e)}")



    # Fill OTP
    def click_on_OTP_Header(self):
        try:
            OTP_Text = self.wait.until(EC.presence_of_element_located(self.getOTPText)).text
            self.log.info(f"I got text here before the click {OTP_Text}")
            return self.wait.until(EC.presence_of_element_located(self.OTPHEADER)).click()
        except Exception as e:
            self.log.error(f"Failed to get Header Text {str(e)}")
    def enterOTP(self, OTP):
        try:
            str_OTP = str(OTP)
            self.driver.find_element(*self.OTP_INPUT).click()
            time.sleep(4)
            return self.driver.find_element(*self.OTP_INPUT).send_keys(str_OTP)
        except Exception as e:
            self.log.error(f"Failed to Enter the OTP {str(e)}")

    def submitOTP(self):
        try:
            time.sleep(4)
            return self.wait.until(EC.visibility_of_element_located(self.OTP_SUBMIT)).click()
        except Exception as e:
            self.log.error(f"Failed to Submit the OTP {str(e)}")

    # Verify Submit
    def verifyOrderSubmit(self):
        try:
            verify_order_text = self.wait.until(EC.visibility_of_element_located(self.VERIFY_ORDER_TEXT)).text
            print(verify_order_text)
            return verify_order_text
        except Exception as e:
            self.log.error(f"Failed to Verify Order Submission {str(e)}")
