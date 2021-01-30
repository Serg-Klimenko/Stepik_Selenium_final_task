class BasePage():
    # constructor
    def __init__(self, browser, url):
        self.browser = browser
        self.url = url

    # open page
    def open(self):
        self.browser.get(self.url)
