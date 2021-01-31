from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage):
    def should_be_login_page(self):
        self.should_be_login_url()
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self):
        # реализуйте проверку на корректный url адрес
        assert "login" in self.browser.current_url, "'login' is not presented in current URl"

    def should_be_login_form(self):
        # реализуйте проверку, что есть форма логина
        assert self.is_element_present(*LoginPageLocators.LOGIN_FORM), "Login form is not presented"

    def should_be_register_form(self):
        # реализуйте проверку, что есть форма регистрации на странице
        assert self.is_element_present(*LoginPageLocators.REGISTER_FORM), "Register form is not presented"

    def register_new_user(self, email_value, password_value):
        # fill email field
        self.browser.find_element(*LoginPageLocators.EMAIL_FIELD).send_keys(email_value)
        # fill password field
        self.browser.find_element(*LoginPageLocators.PASSWORD_FIELD).send_keys(password_value)
        # fill confirm password field
        self.browser.find_element(*LoginPageLocators.CONFIRM_PASSWORD_FIELD).send_keys(password_value)
        # press button LogIn
        self.browser.find_element(*LoginPageLocators.REGISTER_BUTTON).click()
