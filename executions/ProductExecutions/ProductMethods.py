import time
from Pages.ProductManagement.ProductManagementPage import ProductManagementPage


def compareItems(Actual, Expected):
    if Actual == Expected:
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

class ProductMethod:

    # Initializing driver and logger.
    def __init__(self, driver):
        self.driver = driver
        self.product = ProductManagementPage(driver)


    # Helper Methods:
    def get_sizes(self, sizes):
        for size in sizes:
            time.sleep(3)
            self.product.get_Sizes(size)

    def get_duplicate_leather(self, duplicate_leather):
        duplicate_leather = duplicate_leather.split(",")
        print(f"Leather of the list : {type(duplicate_leather)}")

        for leather in duplicate_leather:
            print(f"I was called for {leather}")
            self.product.duplicate_Leather_profile(leather)
            self.product.click_duplicate()
            time.sleep(5)

    # Fill Form
    def fill_product_Details(self, imgPath, name, category, gender, rank, tag, hardware, lining, polyfill_flag, rib_flag, description, sizes):
        self.product.upload_img(imgPath)
        self.product.enter_product_name(name)
        self.product.get_category(category)
        self.product.get_gender(gender)
        self.product.get_ranking(str(rank))
        self.product.get_Tags(tag)
        self.product.get_hardware(hardware)
        self.product.get_lining(lining)
        self.product.get_polyfill(polyfill_flag)
        self.product.get_rib(rib_flag)
        self.product.enter_description(description)
        self.product.enter_pattern_packages(sizes)

    # Get Leather Type
    def fill_leather_details(self, leatherType):
        self.product.click_on_add_leather()
        self.product.click_on_select_leather()
        time.sleep(5)
        self.product.get_leather_type(leatherType)

    def edit_leather_profile(self, leatherType):
        self.product.click_on_add_leather()
        self.product.click_on_select_edit_leather()
        time.sleep(5)
        self.product.get_leather_type(leatherType)

    # Upload Secondary Images
    def upload_secondary_img(self, secondaryImg):
        self.product.navigate_to_secondary_img()
        self.product.click_upload_img()
        self.product.input_secondary_img(secondaryImg)
        self.product.submit_secondary_img()

    # Test Methods
    def verify_navigate_to_productManagement(self):
        self.product.navigate()
        return compareItems(self.product.get_headerText(), "PRODUCT LIST")

    def add_new_product(self, imgPath, name, category, gender, rank, tag, hardware, lining, polyfill_flag, rib_flag, description, sizes,
                        leatherType, sizes_list, price_list, duplicate_leather_list):
        self.product.navigate()
        self.product.clik_on_add()
        self.fill_product_Details(imgPath, name, category, gender, rank, tag, hardware, lining, polyfill_flag, rib_flag, description, sizes)
        self.product.submit_package()
        time.sleep(3)
        self.fill_leather_details(leatherType)
        self.product.get_Sizes(sizes_list, price_list)
        self.product.click_update()
        time.sleep(3)
        confirm_msg = self.product.get_confirm_msg()
        print(confirm_msg)
        self.get_duplicate_leather(duplicate_leather_list)
        return compareItems(confirm_msg, "Product updated successfully")

    def edit_product(self, name, tags, hardware, lining, polyfill_flag, description, secondaryImg):
        self.product.navigate()
        self.product.search(name)
        time.sleep(3)
        self.product.click_on_edit()

        # Editable - content
        self.product.get_Tags(tags)
        self.product.get_hardware(hardware)
        self.product.get_lining(lining)
        self.product.get_polyfill(polyfill_flag)
        self.product.clear(self.product.DESCRIPTION)
        self.product.enter_description(description)
        time.sleep(3)
        self.product.submit_package()
        self.upload_secondary_img(secondaryImg)
        return compareItems(self.product.get_confirm_msg(), "Product updated successfully")

    def check_synchronization(self,  imgPath, name, category, gender, rank, tag, hardware, lining, polyfill_flag, rib_flag, description, sizes,
                        leatherType, sizes_list, price_list, duplicate_leather_list):
        result = []
        self.product.navigate()

        self.product.clik_on_add()
        self.fill_product_Details(imgPath, name, category, gender, rank, tag, hardware, lining, polyfill_flag, rib_flag, description, sizes)
        self.product.submit_package()
        time.sleep(3)
        self.fill_leather_details(leatherType)
        self.product.get_Sizes(sizes_list, price_list)
        self.product.click_update()
        time.sleep(3)
        self.get_duplicate_leather(duplicate_leather_list)
        print("Done with adding product!")


        # Checking synchronization
        self.product.navigate()
        self.product.search(name)
        self.product.click_on_view()
        time.sleep(3)

        # Checking the results
        result.append(compareItems(name, self.product.view_name()))
        result.append(compareItems(category, self.product.view_category()))
        result.append(compareItems(tag, self.product.view_tag()))
        result.append(compareItems(hardware, self.product.view_hardware()))
        result.append(compareItems(lining, self.product.view_lining()))
        result.append(compareItems(polyfill_flag, self.product.view_polyfill()))
        result.append(compareItems(rib_flag, self.product.view_rib()))

        return check_result(result)

