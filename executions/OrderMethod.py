import time
import logging
from Utilities.utils import Utils
from Pages.OrderPage import OrderPage


class OrderMethod:
    def __init__(self, driver):
        self.log = Utils.custom_logger(logLevel=logging.DEBUG)
        self.driver = driver
        self.order = OrderPage(driver)

    def verify_navigateToOrder(self):
        self.order.clickOnOrderTab()
        time.sleep(2)
        return self.order.verify_header()

    def navigateToOrder(self):
        self.order.clickOnOrderTab()
        time.sleep(2)
        self.order.click_on_add()
        time.sleep(2)

    def fill_form(self, name, email, dob, address):
        self.order.input_name(name)
        self.order.input_email(email)
        self.order.input_dob(dob)
        self.order.input_address(address)
        self.order.submit_new_user()


    def create_new_user(self, contactNo, name, email, dob, address):
        self.navigateToOrder()
        self.order.click_on_forCustomer()
        self.order.enter_contact(contactNo)
        time.sleep(5)
        self.order.click_on_customer()
        self.fill_form(name, email, dob, address)
        time.sleep(5)
        return self.order.verify_Create_user()


    def createOrder_Customer(self, contactNo):
        self.navigateToOrder()
        self.order.click_on_forCustomer()
        self.order.enter_contact(contactNo)
        time.sleep(2)
        self.order.click_on_customer()
        time.sleep(2)
        self.order.move_next()
        time.sleep(2)
        return self.order.verify_Create_user()

    def createOrder_Store(self):
        pass
