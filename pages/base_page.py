from selenium.common.exceptions import NoSuchElementException


class BasePage():
    # constructor
    def __init__(self, browser, url, timeout=10):
        self.browser = browser
        self.url = url
        self.browser.implicitly_wait(timeout)

    # open page
    def open(self):
        self.browser.get(self.url)

    # catch exeption
    def is_element_present(self, how, what):
        try:
            self.browser.find_element(how, what)
        except (NoSuchElementException):
            return False
        return True
