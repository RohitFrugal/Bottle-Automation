from Pages.Login.LoginPage import LoginPage

class LoginMethod:
    def __init__(self, driver):
        self.driver = driver
    def nativelogin(self, driver, username, password):
        loginPage = LoginPage(driver)
        loginPage.enter_user_id(username)
        loginPage.enter_password(password)
        loginPage.click_on_submit_button()
        # time.sleep(8)
    def nativeloginforWrongCred(self, driver, username, password):
        loginPage = LoginPage(driver)
        loginPage.enter_user_id(username)
        loginPage.enter_password(password)
        loginPage.click_on_submit_button()
        # time.sleep(2)
