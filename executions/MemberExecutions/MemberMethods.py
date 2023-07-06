import time

from Pages.Login.LoginPage import LoginPage
from Pages.MemberManagement.MemberPage import MemberPage
from executions.LoginExecutions.LoginMethods import LoginMethod
from executions.OrdersExecutions.OrderMethods import OrderMethod
from executions.ProductExecutions.ProductMethods import ProductMethod
from executions.LeatherExecutions.LeatherMethods import LeatherMethod
from executions.InventoryExecutions.InventoryMethods import InventoryMethods


def compare(Actual_response, Expected_response):
    print(f"Actual_response : {Actual_response}   --- Expected_response : {Expected_response} ")
    if Actual_response == Expected_response:
        return True
    else:
        return False


def check_result(result):
    """If the result list is contains any False Item at any Index it will return True or else False
    If result == False then the condition met return true
    else result == True then condition contradicted and return false
    """

    if result.__contains__(False):
        return True
    else:
        return False


class MemberMethods:

    def __init__(self, driver):
        self.driver = driver
        self.member = MemberPage(driver)
        self.loginPage = LoginPage(driver)
        self.LoginMethod = LoginMethod(self.driver)
        self.Order = OrderMethod(self.driver)
        self.Inventory = InventoryMethods(self.driver)
        self.product = ProductMethod(self.driver)
        self.leather = LeatherMethod(self.driver)



    # Validations Methods

    def verify_header_Text(self):
        if self.member.get_Header_Text() == "MANAGE MEMBER":
            return True
        else:
            return False

    # Helper Methods
    def navigate_member(self):
        return self.member.navigate_to_member()

    def fill_form(self, name, designations, email, phone_number, address, password):
        self.member.enter_name(name)
        self.member.enter_designation(designations)
        self.member.enter_email(email)
        self.member.enter_phone_number(phone_number)
        self.member.enter_address(address)
        self.member.enter_password(password)

    def edit_form(self, edit_name, edit_role, edit_phone_number):
        self.member.BackSpace(self.member.NAME)
        self.member.enter_name(edit_name)

        self.member.enter_edit_designation(edit_role)

        self.member.BackSpace(self.member.PHONE_NUMBER)
        self.member.enter_phone_number(edit_phone_number)

    # TODO --- Create a new Execution logic to delete a user.

    # Executions Methods
    def verify_landing(self):
        time.sleep(2)
        self.navigate_member()
        time.sleep(2)
        return self.verify_header_Text()

    def create_new_member(self, name, role, email, phone_number, address, password):
        result = []
        self.navigate_member()
        self.member.click_on_add()
        self.fill_form(name, role, email, phone_number, address, password)
        self.member.save()
        if compare(self.member.validating_string(), "Member created successfully"):
            self.member.delete()
            time.sleep(2)
            result.append(compare(name, self.member.get_username()))  # False
            result.append(compare(role, self.member.get_designated_role()))  # False
            return check_result(result)
        else:
            return False

    def edit_user_details(self, name, role, email, phone_number, address, password, edit_name, edit_role, edit_phone_number):
        result = []
        temp_result = []
        self.navigate_member()
        self.member.click_on_add()
        self.fill_form(name, role, email, phone_number, address, password)
        self.member.save()
        if compare(self.member.validating_string(), "Member created successfully"):
            time.sleep(5)
            self.member.edit()
            self.edit_form(edit_name, edit_role, edit_phone_number)
            self.member.save()

            if compare(self.member.validating_string(), "Member updated successfully"):
                result.append(compare(edit_name, self.member.get_username()))  # True
                result.append(compare(edit_role, self.member.get_designated_role()))  # True
                print(f"Result for Validation for edit : {result}")

                # if the result list contains any False item in it then it is supposed to return True
                if not check_result(result):
                    self.member.delete()
                    time.sleep(2)
                    temp_result.append(compare(edit_role, self.member.get_designated_role()))  # False
                    temp_result.append(compare(edit_name, self.member.get_username()))  # False
                    return check_result(temp_result)
                else:
                    self.member.log.error(f"Edited values are mismatching -- edit_new_member - 106")
                    return False
            else:
                return False
        else:
            return False

    def reset_password(self, name, role, email, phone_number, address, password, new_password):
        self.navigate_member()
        self.member.click_on_add()
        self.fill_form(name, role, email, phone_number, address, password)
        self.member.save()
        if compare(self.member.validating_string(), "Member created successfully"):
            time.sleep(5)
            self.member.edit()
            self.member.resetPassword(new_password)
            if compare(self.member.get_password_verify(), "Password updated successfully"):
                result = []
                print("Reset Successfully performed!")
                self.member.navigate_to_member()
                time.sleep(2)
                self.member.delete()
                time.sleep(2)
                result.append(compare(name, self.member.get_username()))  # False
                result.append(compare(role, self.member.get_designated_role()))  # False
                time.sleep(5)
                return check_result(result)
            else:
                return False
        else:
            return False


    def checkLogin(self, name, role, email, phone_number, address, password):
        self.navigate_member()
        self.member.click_on_add()
        self.fill_form(name, role, email, phone_number, address, password)
        self.member.save()
        if compare(self.member.validating_string(), "Member created successfully"):
            time.sleep(3)
            self.loginPage.click_on_logOut_button()
            time.sleep(5)
            self.LoginMethod.nativelogin(f"{email}@latido.com.np", password)
            time.sleep(5)
            match role:
                case "Store Manager":
                    print(f"This case is for Store Manager : {role}")
                    # navigate to Order Tab
                    result = self.Order.verify_navigateToOrder()
                    print(f"Result = {result}")
                    return result
                case "Product Manager":
                    print(f"This case is for Product Manager : {role}")
                    # navigate to Product Management
                    return self.product.verify_navigate_to_productManagement()

                case "Factory Manager":
                    print(f"This case is for Factory Manager : {role}")
                    # navigate to Inventory
                    return self.Inventory.verify_navigate_to_Inventory()
                case "Inventory Manager":
                    print(f"This case is for Inventory Manager : {role}")
                    # navigate to Inventory
                    return self.Inventory.verify_navigate_to_Inventory()

                case "Order Manager":
                    print(f"This case is for Order Manager : {role}")
                    # navigate to Order Tab
                    return self.Order.verify_navigateToOrder()

                case "Karigar":
                    print(f"This case is for Karigar : {role}")
                    # navigate to Leather management Tab
                    return self.leather.verify_navigate_to_leatherManagement()

                case _:
                    print(f"This default case something went wrong for this role : {role}")
                    return False

