from .base_page import BasePage
from .login_page import LoginPage
from .locators import MainPageLocators


class MainPage(BasePage, LoginPage):
    def go_to_login_page(self):
        login_link = self.browser.find_element(*MainPageLocators.LOGIN_LINK)
        login_link.click()
        self.should_be_login_page()

    def should_be_login_link(self):
        assert self.is_element_present(*MainPageLocators.LOGIN_LINK), "Login link is not presented"
