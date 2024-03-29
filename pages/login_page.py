from .base_page import BasePage
from .locators import LoginPageLocators


class LoginPage(BasePage, LoginPageLocators):
    def should_be_login_page(self):
        self.should_be_login_url(self.browser.current_url, 'login')
        self.should_be_login_form()
        self.should_be_register_form()

    def should_be_login_url(self, full_string, substring):
        # проверка на корректный url адрес
        assert substring in full_string, f"expected '{substring}' to be substring of '{full_string}'"

    def should_be_login_form(self):
        # проверка, что есть форма логина
        self.is_element_present(*LoginPageLocators.LOGIN_EMAIL), "Login link is not presented"
        self.is_element_present(*LoginPageLocators.LOGIN_PASSWORD), "Login link is not presented"
        assert True

    def should_be_register_form(self):
        # проверка, что есть форма регистрации на странице
        self.is_element_present(*LoginPageLocators.REGISTRATION_EMAIL), "Login link is not presented"
        self.is_element_present(*LoginPageLocators.REGISTRATION_PASSWORD), "Login link is not presented"
        assert True

    def register_new_user(self, email, password):
        self.browser.find_element(*LoginPageLocators.REGISTRATION_EMAIL).send_keys(email)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_PASSWORD_REPEAT).send_keys(password)
        self.browser.find_element(*LoginPageLocators.REGISTRATION_SUBMIT_BUTTON).click()
