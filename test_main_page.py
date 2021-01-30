import time
from .pages.main_page import MainPage


def test_guest_can_go_to_login_page(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    # init Page Object, pass driver instance and url to the constructor
    page = MainPage(browser, link)
    page.open()  # open page in the browser
    page.go_to_login_page()  # method page - move to the login page


def test_guest_should_see_login_link(browser):
    link = "http://selenium1py.pythonanywhere.com/"
    page = MainPage(browser, link)
    page.open()
    page.should_be_login_link()
