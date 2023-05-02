import time
import logging

from Pages.Order.OrderList import OrderList
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
        self.createUser = CreateNewUser(driver)

        self.store = ProductDetailsForStore(driver)
        self.products = ProductDetails(driver)

        self.bodyMeasurement = BodyMeasurement(driver)
        self.storeMeasurement = BodyMeasurementForStore(driver)

        self.payment = Payments(driver)
        self.storePay = PaymentsStore(driver)

        self.order_ls = OrderList(driver)

        self.log = Utils.custom_logger(logLevel=logging.INFO)

# ******************************************************************* Helping Methods *******************************************************************
    # Verifying the header of Order List.
    def verify_navigateToOrder(self):
        self.order.clickOnOrderTab()
        time.sleep(2)
        return self.order.verify_header()

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
        print(f'Selecting : {productname} and it is of "{type(productname)}" type')

        self.store.selectLeatherProfile(leatherProfile)
        print(f'Selecting : {leatherProfile}  and it is of "{type(leatherProfile)}" type')

        leatherSize_str = str(leatherSize)
        self.store.selectLeatherSize(leatherSize_str)
        print(f'Selecting : {leatherSize} and it is of "{type(leatherSize_str)}" type')

        self.store.selectHardware(hardware)
        print(f'Selecting : {hardware}  and it is of "{type(hardware)}" type')

        self.store.selectLining(lining)
        print(f'Selecting : {lining}  and it is of "{type(lining)}" type')

        self.store.selectPolyfill(polyfill)
        print(f'Selecting : {polyfill}  and it is of "{type(polyfill)}" type')

    # Fill Body Measurement for Customer
    def fillBodyMeasurements(self, size, armhole, height, shoulder, weight, length, arms, hips, chest, waist, sleeves,
                             bodytype):
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
    def fillBodyMeasurementsForStore(self, size, bodytype, length, chest, waist, hips, shoulder, sleeves, arms, weight,
                                     front, armhole):
        Size_str = str(size)
        self.storeMeasurement.selectBasesize(Size_str)
        print(f'Selecting : {Size_str} and it is of "{type(Size_str)}" type')

        self.storeMeasurement.selectBodyType(bodytype)
        print(f'Selecting : {bodytype} and it is of "{type(bodytype)}" type')

        self.storeMeasurement.inputLength(length)
        print(f'Selecting : {length} and it is of "{type(length)}" type')

        self.storeMeasurement.inputChest(chest)
        print(f'Selecting : {chest} and it is of "{type(chest)}" type')

        self.storeMeasurement.inputWaist(waist)
        print(f'Selecting : {waist} and it is of "{type(waist)}" type')

        self.storeMeasurement.inputHips(hips)
        print(f'Selecting : {hips} and it is of "{type(hips)}" type')

        self.storeMeasurement.inputShoulder(shoulder)
        print(f'Selecting : {shoulder} and it is of "{type(shoulder)}" type')

        self.storeMeasurement.inputSleeves(sleeves)
        print(f'Selecting : {sleeves} and it is of "{type(sleeves)}" type')

        self.storeMeasurement.inputArms(arms)
        print(f'Selecting : {arms} and it is of "{type(arms)}" type')

        self.storeMeasurement.inputWeight(weight)
        print(f'Selecting : {weight} and it is of "{type(weight)}" type')

        self.storeMeasurement.inputFront(front)
        print(f'Selecting : {front} and it is of "{type(front)}" type')

        self.storeMeasurement.inputArmhole(armhole)
        print(f'Selecting : {armhole} and it is of "{type(armhole)}" type')

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

    # Comparing the Order Id's
    def compare_id(self, storeId, customerId):
        if int(customerId) > int(storeId):
            print(f"Customer order was created recently : {customerId}")
            self.order_ls.click_on_customer()
            return self.order_ls.get_latest_customer_orderID().click()
        elif int(storeId) > int(customerId):
            print(f"Store order was created recently : {storeId}")
            return self.order_ls.get_latest_store_orderID().click()






# ******************************************************************* Test Executors *******************************************************************

    # Creating an Order for an Existing Customer.
    def createOrder_Customer(self, contactNo, gender, productname, leatherProfile, leatherSize, hardware, lining,
                             polyfill,
                             size, armhole, height, shoulder, weight, length, arms, hips, chest, waist, sleeves,
                             bodytype,
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
        self.fillBodyMeasurements(size, armhole, height, shoulder, weight, length, arms, hips, chest, waist, sleeves,
                                  bodytype)
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
        self.fillBodyMeasurementsForStore(size, bodytype, length, chest, waist, hips, shoulder, sleeves, arms, weight,
                                          front, armhole)
        self.storeMeasurement.inputRemark(remarks)
        self.storePay.inputPrice(price)
        self.storePay.inputDiscount(discount)
        time.sleep(2)
        self.storePay.submitOrder()
        time.sleep(5)
        self.fill_otp_store(OTP)
        time.sleep(5)
        return self.storePay.verifyOrderSubmit()

    # Creating a new user and submitting an Order
    def create_new_user_order(self, contactNo, name, email, dob, address, gender, productname, leatherProfile,
                              leatherSize, hardware, lining, polyfill, size, armhole, height, shoulder, weight,
                              length, arms, hips, chest, waist, sleeves, bodytype, remark, date, OTP):
        self.create_new_user(contactNo, name, email, dob, address)
        self.order.click_gender(gender)
        time.sleep(3)
        self.fill_CustomerProductDetails(productname, leatherProfile, leatherSize, hardware, lining, polyfill)
        self.fillBodyMeasurements(size, armhole, height, shoulder, weight, length, arms, hips, chest, waist, sleeves,
                                  bodytype)
        self.bodyMeasurement.inputRemark(remark)

        self.payment.sendDeliveryDate(date)
        time.sleep(2)
        self.payment.submitOrder()
        time.sleep(2)
        self.fill_otp(OTP)
        time.sleep(20)
        return self.payment.verifyOrderSubmit()

    def navigate_to_order_list(self, contactNo, gender, productname, leatherProfile, leatherSize, hardware, lining,
                               polyfill, size, armhole, height, shoulder, weight, length, arms, hips, chest, waist,
                               sleeves, bodytype, remark, date, OTP):

        self.createOrder_Customer(contactNo, gender, productname, leatherProfile, leatherSize, hardware,
                                  lining, polyfill, size, armhole, height, shoulder, weight, length, arms, hips,
                                  chest, waist, sleeves, bodytype, remark, date, OTP)
        self.order_ls.click_on_goto_order()
        latest_customer_id = self.order_ls.get_latest_customer_orderID().text
        self.order_ls.click_on_store()
        latest_store_id = self.order_ls.get_latest_store_orderID().text
        self.compare_id(latest_store_id, latest_customer_id)

