import time

from Pages.LeatherManagement.LeatherManagementPage import LeatherManagementPage


def compareItems(Actual, Expected):
    print(f"\nActual : {Actual}")
    print(f"Expected : {Expected}")
    if Actual == Expected:
        return True
    else:
        return False


def check_result(result):
    """If the result list is containing any False Item at any Index it will return True or else False
    If result == False then the condition met return true
    else result == True then condition contradicted and return false
    """

    if result.__contains__(False):
        return False
    else:
        return True


class LeatherMethod:

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.leather = LeatherManagementPage(driver)


    def check_add_flag(self, add_flag, profileType, imgPath, title, data_item):
        """
        **NOTE:Please provide the hardcoded profile type while calling this function. **
        :param add_flag:
        :param profileType:
        :param imgPath:
        :param title:
        :param data_item:
        :return:
        """

        if add_flag == 1:
            self.leather.click_add_leather_profile(add_flag, profileType, imgPath, title, data_item)
            self.leather.click_next()
        else:
            self.leather.click_next()

    def verify_navigate_to_leatherManagement(self):
        self.leather.navigate()
        return compareItems(self.leather.get_headerText(), "LEATHER MANAGEMENT")

    def add_new_Leather(self, leather_name, finish, texture, aging, hide, touch, ):
        self.leather.navigate()
        self.leather.click_on_addLeather()

        # Selecting Leather -> Inventory
        time.sleep(3)
        self.leather.get_leather(leather_name)
        self.leather.click_next()

        # Selecting Finish
        self.leather.input_details(item_selector=finish)
        time.sleep(2)
        self.leather.click_next()

        # Selecting Texture
        self.leather.input_details(item_selector=texture)
        self.leather.click_next()

        # Selecting Aging Process
        time.sleep(2)
        self.leather.input_details(item_selector=aging)
        self.leather.click_next()

        # Selecting Hide
        self.leather.input_details(item_selector=hide)
        self.leather.click_next()

        # Selecting Touch
        time.sleep(2)
        self.leather.input_details(item_selector=touch)

        self.leather.click_add()
        time.sleep(5)
        return compareItems(self.leather.check_creation(leather_name), leather_name)

    def check_synchronization(self, leather_name, finish, texture, aging_process, hide_type, touch):

        self.leather.navigate()
        result = []
        self.leather.click_item_leather(leather_name)
        # Obtaining Items
        result.append(compareItems(touch, self.leather.verify_item_creation(1)))
        result.append(compareItems(finish, self.leather.verify_item_creation(2)))
        result.append(compareItems(texture, self.leather.verify_item_creation(3)))
        result.append(compareItems(aging_process, self.leather.verify_item_creation(4)))
        result.append(compareItems(hide_type, self.leather.verify_item_creation(5)))
        result.append(compareItems(leather_name, self.leather.verify_item_creation(6)))
        print(result)
        return check_result(result)
