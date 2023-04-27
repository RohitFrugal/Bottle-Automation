import time
import logging

from Pages.Order.Store.PaymentsStore import PaymentsStore
from Utilities.utils import Utils
from Pages.Order.Customer.Payments import Payments
from Pages.Order.OrderPage import OrderPage
from Pages.Order.Customer.CreateNewUser import CreateNewUser
from Pages.Order.Customer.ProductDetails import ProductDetails
from Pages.Order.Customer.BodyMeasurement import BodyMeasurement
from Pages.Order.Store.ProductDetails_forStore import ProductDetailsForStore
from Pages.Order.Store.BodyMeasurement_forStore import BodyMeasurementForStore


class OrderMethod:

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.order = OrderPage(driver)
        self.payment = Payments(driver)
        self.storePay = PaymentsStore(driver)
        self.products = ProductDetails(driver)
        self.createUser = CreateNewUser(driver)
        self.store = ProductDetailsForStore(driver)
        self.bodyMeasurement = BodyMeasurement(driver)
        self.storeMeasurement = BodyMeasurementForStore(driver)

        self.log = Utils.custom_logger(logLevel=logging.DEBUG)


    # Verifying the header of Order List.
    def verify_navigateToOrder(self):
        self.order.clickOnOrderTab()
        time.sleep(2)
        return self.order.verify_header()

    # Verifying New Customer Creation.
    def verify_create_new_user(self, contactNo, name, email, dob, address):
        self.navigateToOrder()
        self.order.click_on_forCustomer()
        self.order.enter_contact(contactNo)
        time.sleep(5)
        self.order.click_on_customer()
        self.fill_form(name, email, dob, address)
        time.sleep(5)
        return self.createUser.verify_Create_user()

    # Verifying new Order creations for Existing Customer
    def verify_createOrder_Customer(self, contactNo):
        self.navigateToOrder()
        self.order.click_on_forCustomer()
        self.order.enter_contact(contactNo)
        time.sleep(2)
        self.order.click_on_customer()
        time.sleep(2)
        self.order.move_next()
        time.sleep(2)
        return self.createUser.verify_Create_user()


    # Navigate to Order List.
    def navigateToOrder(self):
        self.order.clickOnOrderTab()
        time.sleep(2)
        self.order.click_on_add()
        time.sleep(2)

    # Fill for New user.
    def fill_form(self, name, email, dob, address):
        self.createUser.input_name(name)
        self.createUser.input_email(email)
        self.createUser.input_dob(dob)
        self.createUser.input_address(address)
        self.createUser.submit_new_user()

    # Creating new user.
    def create_new_user(self, contactNo, name, email, dob, address):
        self.navigateToOrder()
        self.order.click_on_forCustomer()
        self.order.enter_contact(contactNo)
        time.sleep(5)
        self.order.click_on_customer()
        self.fill_form(name, email, dob, address)
        time.sleep(5)

    # Fill Product details for Customer
    def fill_CustomerProductDetails(self, productname, leatherProfile, leatherSize, hardware, lining, polyfill):

        self.products.selectProductName(productname)
        print(f'Selecting : {productname} and it is of "{type(productname)}" type')

        self.products.selectLeatherProfile(leatherProfile)
        print(f'Selecting : {leatherProfile}  and it is of "{type(leatherProfile)}" type')

        leatherSize_str = str(leatherSize)
        self.products.selectLeatherSize(leatherSize_str)
        print(f'Selecting : {leatherSize} and it is of "{type(leatherSize)}" type')

        self.products.selectHardware(hardware)
        print(f'Selecting : {hardware}  and it is of "{type(hardware)}" type')

        self.products.selectLining(lining)
        print(f'Selecting : {lining}  and it is of "{type(lining)}" type')

        self.products.selectPolyfill(polyfill)
        print(f'Selecting : {polyfill}  and it is of "{type(polyfill)}" type')

    # Fill Product details for Store
    def fill_StoreProductDetails(self, productname, leatherProfile, leatherSize, hardware, lining, polyfill):
        self.store.selectProductName(productname)
        self.store.selectLeatherProfile(leatherProfile)
        leatherSize_str = str(leatherSize)
        self.products.selectLeatherSize(leatherSize_str)
        self.store.selectLeatherSize(leatherSize)
        self.store.selectHardware(hardware)
        self.store.selectLining(lining)
        self.store.selectPolyfill(polyfill)

    # Fill Body Measurement for Customer
    def fillBodyMeasurements(self, size, armhole, height, shoulder, weight, length,arms, hips, chest, waist, sleeves, bodytype):
        Size_str = str(size)
        self.bodyMeasurement.selectBasesize(Size_str)
        print(f'Selecting : {size} and it is of "{type(size)}" type')

        self.bodyMeasurement.inputArmhole(armhole)
        print(f'Selecting : {armhole} and it is of "{type(armhole)}" type')

        self.bodyMeasurement.inputHeight(height)
        print(f'Selecting : {height} and it is of "{type(height)}" type')

        self.bodyMeasurement.inputShoulder(shoulder)
        print(f'Selecting : {shoulder} and it is of "{type(shoulder)}" type')

        self.bodyMeasurement.inputWeight(weight)
        print(f'Selecting : {weight} and it is of "{type(weight)}" type')

        self.bodyMeasurement.inputLength(length)
        print(f'Selecting : {length} and it is of "{type(length)}" type')

        self.bodyMeasurement.inputArms(arms)
        print(f'Selecting : {arms} and it is of "{type(arms)}" type')

        self.bodyMeasurement.inputHips(hips)
        print(f'Selecting : {hips} and it is of "{type(hips)}" type')

        self.bodyMeasurement.inputChest(chest)
        print(f'Selecting : {chest} and it is of "{type(chest)}" type')

        self.bodyMeasurement.inputWaist(waist)
        print(f'Selecting : {waist} and it is of "{type(waist)}" type')

        self.bodyMeasurement.inputSleeves(sleeves)
        print(f'Selecting : {sleeves} and it is of "{type(sleeves)}" type')

        self.bodyMeasurement.selectBodyType(bodytype)
        print(f'Selecting : {bodytype} and it is of "{type(bodytype)}" type')


    # Fill Body Measurement for Store
    def fillBodyMeasurementsForStore(self, size, bodytype, length, chest, waist, hips, shoulder, sleeves, arms, weight, front, armhole):

        Size_str = str(size)
        self.storeMeasurement.selectBasesize(Size_str)
        self.storeMeasurement.selectBodyType(bodytype)
        self.storeMeasurement.inputLength(length)
        self.storeMeasurement.inputChest(chest)
        self.storeMeasurement.inputWaist(waist)
        self.storeMeasurement.inputHips(hips)
        self.storeMeasurement.inputShoulder(shoulder)
        self.storeMeasurement.inputSleeves(sleeves)
        self.storeMeasurement.inputArms(arms)
        self.storeMeasurement.inputWeight(weight)
        self.storeMeasurement.inputFront(front)
        self.storeMeasurement.inputArmhole(armhole)

    # Fill OTP
    def fill_otp(self, OTP):
        # self.payment.click_on_OTP_Header()
        self.payment.enterOTP(OTP)
        self.payment.submitOTP()

    # Fill OTP For Store
    def fill_otp_store(self, OTP):
        self.payment.click_on_OTP_Header()
        self.storePay.enterOTP(OTP)
        self.storePay.submitOTP()


    # Creating an Order for an Existing Customer.
    def createOrder_Customer(self, contactNo, gender, productname, leatherProfile, leatherSize, hardware, lining, polyfill,
                             size, armhole, height, shoulder, weight, length, arms, hips, chest, waist, sleeves, bodytype,
                             remark, date, OTP):
        self.navigateToOrder()
        self.order.click_on_forCustomer()
        self.order.enter_contact(contactNo)
        time.sleep(2)
        self.order.click_on_customer()
        time.sleep(2)
        self.order.move_next()
        time.sleep(2)
        self.order.click_gender(gender)
        time.sleep(3)
        self.fill_CustomerProductDetails(productname, leatherProfile, leatherSize, hardware, lining, polyfill)
        self.fillBodyMeasurements(size, armhole, height, shoulder, weight, length, arms, hips, chest, waist, sleeves, bodytype)
        self.bodyMeasurement.inputRemark(remark)


        self.payment.sendDeliveryDate(date)
        time.sleep(2)
        self.payment.submitOrder()
        time.sleep(2)
        self.fill_otp(OTP)
        time.sleep(20)
        return self.payment.verifyOrderSubmit()

    # Creating an Order for Store
    def createOrder_Store(self, productname, leatherProfile, leatherSize, hardware, lining, polyfill,
                          size, bodytype, length, chest, waist, hips, shoulder, sleeves, arms, weight, front, armhole,
                          remarks, price, discount, OTP):
        self.navigateToOrder()
        self.order.click_on_forStore()
        self.fill_StoreProductDetails(productname, leatherProfile, leatherSize, hardware, lining, polyfill)
        self.fillBodyMeasurementsForStore(size, bodytype, length, chest, waist, hips, shoulder, sleeves, arms, weight, front, armhole)
        self.storeMeasurement.inputRemark(remarks)
        self.storePay.inputPrice(price)
        self.storePay.inputDiscount(discount)
        time.sleep(2)
        self.storePay.submitOrder()
        time.sleep(5)
        self.fill_otp_store(OTP)
        time.sleep(5)
        return self.storePay.verifyOrderSubmit()
