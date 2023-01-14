from .base_page import BasePage
from .locators import BasketPageLocators
from .locators import BasePageLocators


class BasketPage(BasePage, BasketPageLocators, BasePageLocators):
    def should_not_be_any_product(self):
        self.browser.find_element(*BasePageLocators.GO_TO_BASKET_BUTTON).click()
        assert self.is_element_present(*BasketPageLocators.EMPTY_BASKET), "Basket is not empty"
        assert self.is_not_element_present(*BasketPageLocators.BASKET_PRODUCTS), "Basket is not empty"
