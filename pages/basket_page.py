from .base_page import BasePage
from .locators import BasketPageLocators


class BasketPage(BasePage):
    def should_be_basket_page(self):
        self.is_not_product_present()
        self.should_be_message_about_empty_basket()

    def is_not_product_present(self):
        assert self.is_not_element_present(*BasketPageLocators.PRODUCTS_IN_BASKET), \
            "Product is presented in the basket, but should not be"

    def should_be_message_about_empty_basket(self):
        assert self.is_element_present(*BasketPageLocators.MESSAGE_EMPTY_BASKET), \
            "Message 'Your basket is empty' is not presented, but should be"
