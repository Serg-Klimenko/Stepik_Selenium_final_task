from .base_page import BasePage
from .locators import ProductPageLocators


class ProductPage(BasePage):

    def __init__(self, browser, url, timeout=10):
        super().__init__(browser, url, timeout)
        self.product_price = ""
        self.product_name = ""

    def should_be_product_page(self):
        self.name_of_cart_product_equal_added_product()
        self.cost_of_cart_product_equal_price_added_product()
        self.add_product_to_cart()
        self.get_product_name()
        self.get_product_price()

    def get_product_name(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_NAME).text

    def get_product_price(self):
        return self.browser.find_element(*ProductPageLocators.PRODUCT_PRICE).text

    def add_product_to_cart(self):
        self.product_name = self.get_product_name()
        self.product_price = self.get_product_price()
        add_product_button = self.browser.find_element(*ProductPageLocators.ADD_BUTTON)
        add_product_button.click()

    def name_of_cart_product_should_be_equal_added_product(self):
        assert self.browser.find_element(*ProductPageLocators.PRODUCT_NAME_IN_BASKET).text == self.product_name, \
            "Product name in the basket not egual product name on the product page"

    def cost_of_cart_product_should_be_equal_price_added_product(self):
        assert self.browser.find_element(*ProductPageLocators.BASKET_COST).text == self.product_price, \
            "Product price in the basket not egual product price on the product page"

    def should_not_be_success_message(self):
        assert self.is_not_element_present(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), \
            "Success message is presented, but should not be"

    def should_be_disappeared(self):
        assert self.is_disappeared(*ProductPageLocators.PRODUCT_NAME_IN_BASKET), \
            "Element is presented, but should be disappeared"
