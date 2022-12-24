from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage, ProductPageLocators):
    def should_add_product_to_basket(self):
        self.browser.find_element(*ProductPageLocators.ADD_TO_BASKET_BUTTON).click()
        self.solve_quiz_and_get_code()
        message_product = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_NAME).text
        message_price = self.browser.find_element(*ProductPageLocators.ADDED_PRODUCT_PRICE).text
        product_name = self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text
        product_price = self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text
        assert product_name == message_product, f"expected '{product_name}' to be substring of '{message_product}'"
        assert product_price in message_price, f"expected '{product_price}' to be substring of '{message_price}'"
