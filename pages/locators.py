from selenium.webdriver.common.by import By


class MainPageLocators():
    # each locator consists two values: (how search, what search)
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")


class LoginPageLocators():
    LOGIN_FORM = (By.CSS_SELECTOR, "#login_form")
    REGISTER_FORM = (By.CSS_SELECTOR, "#register_form")


class ProductPageLocators():
    ADD_BUTTON = (By.CSS_SELECTOR, "button.btn-add-to-basket")
    PRODUCT_PRICE = (By.CSS_SELECTOR, "div.product_main > p.price_color")
    PRODUCT_NAME = (By.CSS_SELECTOR, "div.product_main > h1")
    PRODUCT_NAME_IN_BASKET = (By.CSS_SELECTOR, "#messages > div > div > strong")
    BASKET_COST = (By.CSS_SELECTOR, "div.fade > div > p > strong")
