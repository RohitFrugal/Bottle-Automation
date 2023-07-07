import time

from Pages.ProductManagement.ProductManagementPage import ProductManagementPage


def compareItems(Actual, Expected):
    if Actual == Expected:
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
            time.sleep(3)
            self.product.duplicate_Leather_profile(leather)
            self.product.click_duplicate()
            self.product.click_on_add_leather()


    # Test Methods

    def verify_navigate_to_productManagement(self):
        self.product.navigate()
        return compareItems(self.product.get_headerText(), "PRODUCT LIST")

    def add_new_product(self, imgPath, name, category, gender, rank, tag, hardware, lining, polyfill_flag, rib_flag, description, sizes, leatherType, sizes_list, duplicate_leather):
        self.product.navigate()
        self.product.clik_on_add()
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
        self.product.submit_package()
        time.sleep(5)
        self.product.click_on_add_leather()
        self.product.click_on_select_leather()
        time.sleep(3)
        self.product.get_leather_type(leatherType)
        self.product.get_Sizes(sizes_list)
        self.product.click_update()
        time.sleep(5)
        self.product.duplicate_Leather_profile(duplicate_leather)
        self.product.click_duplicate()
        self.product.click_on_add_leather()
        time.sleep(2)
        return True

    def edit_product(self, name, leatherType, sizes_list, duplicate_leather_list):
        print(type(duplicate_leather_list))
        print(type(sizes_list))

        self.product.navigate()
        self.product.search(name)
        self.product.click_on_edit()
        self.product.click_on_add_leather_profile()
        self.product.click_on_add_leather()
        self.product.click_on_select_leather()
        time.sleep(3)
        self.product.get_leather_type(leatherType)
        self.product.get_Sizes(sizes_list)
        self.product.click_update()
        time.sleep(3)
        self.get_duplicate_leather(duplicate_leather_list)




