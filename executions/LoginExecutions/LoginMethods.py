from Pages.Login.LoginPage import LoginPage

class LoginMethod:
    def __init__(self, driver):
        self.driver = driver
        self.loginPage = LoginPage(driver)

    # Don't Touch this Code here!!
    def nativelogin(self, username, password):
        """ Login Methods for all the modules """
        self.loginPage.enter_user_id(username)
        self.loginPage.enter_password(password)
        self.loginPage.click_on_submit_button()
    # Don't Touch this Code here!!

    # Helper Method
    def verify_msg(self, expected_msg, actual_msg):
        if expected_msg == actual_msg:
            return True
        else:
            return False


    # Check Login
    def verify_correct_login(self):
        return self.verify_msg(self.loginPage.verify_login(), "OVERVIEW")

    def verify_invalid_login(self):
        return self.verify_msg(self.loginPage.verify_login_error_message(), "Please check username")

    def verify_login_with_invalid_mail(self):
        return self.verify_msg(self.loginPage.verify_login_error_message_for_invalid_email(), "Please check username")

    def verify_empty_email_field(self):
        return self.verify_msg(self.loginPage.verify_login_error_message_with_noEmail(), "Please input your Email!")

    def verify_empty_password_field(self):
        return self.verify_msg(self.loginPage.verify_login_error_message_with_noPassword(), "Please input your password!")