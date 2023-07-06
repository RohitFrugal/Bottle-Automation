from Pages.LeatherManagement.LeatherManagementPage import LeatherManagementPage


def compareItems(Actual, Expected):
    if Actual == Expected:
        return True
    else:
        return False


class LeatherMethod:

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.leather = LeatherManagementPage(driver)

    def verify_navigate_to_leatherManagement(self):
        self.leather.navigate()
        return compareItems(self.leather.get_headerText(), "LEATHER MANAGEMENT")
