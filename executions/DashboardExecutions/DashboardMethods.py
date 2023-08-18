from Pages.Dashboard.DashboardPage import DashboardPage
from executions.OrdersExecutions.OrderMethods import OrderMethod


class DashboardMethod:
    def __init__(self, driver):
        self.driver = driver
        self.Order = OrderMethod(self.driver)
        self.Dashboard = DashboardPage(self.driver)

    def verify_total_user(self):
        return self.Dashboard.verify_total_user()

    def verify_total_order(self):
        return self.Dashboard.verify_total_order()

    def verify_total_sales(self):
        return self.Dashboard.verify_total_sales()

    def verify_pending(self):
        return self.Dashboard.verify_pending()

    def active_user(self):
        return self.Dashboard.active_user()

    def inactive_user(self):
        return self.Dashboard.inactive_user()

    def verify_sum_of_total_user(self):
        return self.Dashboard.verify_sum_of_total_user()

    def total_user(self):
        return self.Dashboard.total_user()

    def get_customer_page_details(self):
        # For customer - Page only
        first_page_customer = self.Dashboard.get_elements_perPage_Customer()
        print(f"first_page_customer : {first_page_customer}")
        number_of_pages_customer = self.Dashboard.get_lastPage_customer()
        print(f"number_of_pages_customer : {number_of_pages_customer}")
        last_page = self.Dashboard.get_elements_perPage_Customer()
        print(f"last_page : {last_page}")

        if last_page == 10:
            return int(first_page_customer) * int(number_of_pages_customer)
        elif last_page != 10:
            return (int(first_page_customer) * (int(number_of_pages_customer) - 1)) + int(last_page)


    def get_store_page_details(self):
        # For Store - Page
        self.Order.navigateToStorePage()
        first_page_Store = self.Dashboard.get_elements_perPage_Store()
        print(f"first_page_Store : {first_page_Store}")
        number_of_pages_store = self.Dashboard.get_lastPage_store()
        print(f"number_of_pages_store : {number_of_pages_store}")
        last_page = self.Dashboard.get_elements_perPage_Store()
        print(f"last_page Store : {last_page}")

        if last_page == 10:
            return int(first_page_Store) * int(number_of_pages_store)
        elif last_page != 10:
            return (int(first_page_Store) * (int(number_of_pages_store) - 1)) + int(last_page)



    def get_number_of_orders(self):
        self.Order.navigateToOrderTab()

        customer_page = self.get_customer_page_details()
        print(f"Customer Page : {customer_page}")
        self.driver.execute_script("window.scrollTo(0, -document.body.scrollHeight);")
        store_page = self.get_store_page_details()
        print(f"Store Page : {store_page}")
        return str(int(customer_page) + int(store_page))

