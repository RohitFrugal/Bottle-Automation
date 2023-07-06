import time
import logging


from Utilities.utils import Utils
from selenium.webdriver import Keys
from Pages.Order.OrderPage import OrderPage


from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException, TimeoutException


class PaymentsStore(OrderPage):
    # Initializing driver and logger.
    def __init__(self, driver):
        super().__init__(driver)
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)
        self.log = Utils.custom_logger(module_name="Order_module", logLevel=logging.WARNING)

    # Payments
    TOTAL_AMOUNT = (By.ID, 'total_amount')
    DISCOUNT = (By.ID, 'discount')
    DELIVER_DATE = (By.ID, 'delivery_date')

    # Button
    CANCEL_BTN = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[2]/button[1]')
    SUBMIT_BTN = (By.XPATH, '//*[@id="root"]/section/main/div/div/form/div[2]/button[2]')


    # OTP Input field
    OTPHEADER = (By.XPATH, "//div[@class='ant-modal-header']")
    OTP_INPUT = (By.XPATH, "//input[@class='ant-input input-field']")
    OTP_SUBMIT = (By.XPATH, "//button[@class='ant-btn ant-btn-primary']")

    # Verify Submit Order
    VERIFY_ORDER_TEXT = (By.XPATH, "//h3[@class='ant-typography']")
    GET_OTP_Text = (By.XPATH, '//*[@id="rc_unique_0"]')

    # Fill Payments
    def inputPrice(self, price):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.TOTAL_AMOUNT)).send_keys(price)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Price Input : \n {str(e)}")

    def inputDiscount(self, discountPrice):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.DISCOUNT)).send_keys(discountPrice)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Discount Input : \n {str(e)}")

    def sendDeliveryDate(self, date):
        try:
            self.wait.until(EC.visibility_of_element_located(self.DELIVER_DATE)).send_keys(date)
            return self.wait.until(EC.visibility_of_element_located(self.DELIVER_DATE)).send_keys(Keys.ENTER)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Delivery Date Input : \n {str(e)}")

    def cancel(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.CANCEL_BTN)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Cancel Button: \n {str(e)}")

    def submitOrder(self):
        try:
            return self.wait.until(EC.visibility_of_element_located(self.SUBMIT_BTN)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for Submit Button: \n {str(e)}")

    # OTP Sections



    # Fill OTP
    def click_on_OTP_Header(self):
        try:
            OTP_Text = self.wait.until(EC.presence_of_element_located(self.GET_OTP_Text)).text
            self.log.info(f"I got text here before the click {OTP_Text}")
            return self.wait.until(EC.presence_of_element_located(self.OTPHEADER)).click()
        except Exception as e:
            self.log.warning(f"Unable to find the element : \n {str(e)}")

    def enterOTP(self, OTP):
        try:
            self.driver.find_element(*self.OTP_INPUT).click()
            time.sleep(5)
            return self.driver.find_element(*self.OTP_INPUT).send_keys(OTP)
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element for OTP input : \n {str(e)}")

    def submitOTP(self):
        try:
            time.sleep(5)
            return self.wait.until(EC.visibility_of_element_located(self.OTP_SUBMIT)).click()
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Submit OTP: \n {str(e)}")

    # Verify Submit
    def verifyOrderSubmit(self):
        try:
            verify_order_text = self.wait.until(EC.visibility_of_element_located(self.VERIFY_ORDER_TEXT)).text
            return verify_order_text
        except (NoSuchElementException, TimeoutException, Exception) as e:
            self.log.error(f"Couldn't find the Element to Verify Order Submit : \n {str(e)}")
