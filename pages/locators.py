from selenium.webdriver.common.by import By


class MainPageLocators():
    # each locator consists two values: (how search, what search)
    LOGIN_LINK = (By.CSS_SELECTOR, "#login_link")
