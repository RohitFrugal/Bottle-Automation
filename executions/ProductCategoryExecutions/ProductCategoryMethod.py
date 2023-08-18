import time

from Pages.ProductCategory.ProductCategoryPage import ProductCategoryPage




# Return Functions

def compare(actual, expected):
    """
    Check the Actual input argument with expected input argument and return True or False
    :param actual: Actual Input
    :param expected: Expected Input
    :return: True / False
    """
    print(f"Actual : {actual}")
    print(f"Expected : {expected}")

    if actual == expected:
        return True
    else:
        return False


class ProductCategoryMethod:

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.Category = ProductCategoryPage(self.driver)

    HEADER_VERIFICATION = "PRODUCT CATEGORY"
    SUCCESSFUL_MSG = "ProductCategory created successfully"
    UPDATE_MSG = "ProductCategory updated successfully"

    # Helper Methods


    # Methods


    # Test Methods -
    def test_navigation(self):
        self.Category.click_on_Category()
        return compare(self.Category.check_header(), self.HEADER_VERIFICATION)


    def test_add_new_category(self, imgPath, name):
        self.Category.click_on_Category()
        self.Category.add_new_Category()
        self.Category.upload_img(imgPath)
        self.Category.enter_name(name)
        self.Category.click_on_add()
        return compare(self.Category.check_status_successful(), self.SUCCESSFUL_MSG)

    def test_edit_category(self, name, edit_name):
        self.Category.click_on_Category()
        self.Category.edit_category(name)
        self.Category.clear(self.Category.CATEGORY_NAME)
        self.Category.enter_name(edit_name)
        self.Category.click_on_update()
        return compare(self.Category.check_status_update(), self.UPDATE_MSG)

    def test_add_Subcategory(self, main_category, imgPath, sub_Category_name):
        self.Category.click_on_Category()
        self.Category.view_category(main_category)
        self.Category.add_new_Category()
        time.sleep(2)
        self.Category.upload_img(imgPath)
        time.sleep(2)
        self.Category.enter_name(sub_Category_name)
        self.Category.click_on_add()
        return compare(self.Category.check_status_successful(), self.SUCCESSFUL_MSG)

    def test_edit_Subcategory(self, main_category, sub_category, edit_name):
        self.Category.click_on_Category()
        self.Category.view_category(main_category)
        self.Category.edit_category(sub_category)
        self.Category.clear(self.Category.CATEGORY_NAME)
        self.Category.enter_name(edit_name)
        self.Category.click_on_update()
        return compare(self.Category.check_status_update(), self.UPDATE_MSG)
