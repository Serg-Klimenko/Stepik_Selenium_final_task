# launch: pytest -v --tb=line --language=en test_product_page.py
import time
from .pages.product_page import ProductPage


def test_guest_can_add_product_to_basket(browser):
    link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.name_of_cart_product_equal_added_product()
    page.cost_of_cart_product_equal_price_added_product()
    time.sleep(10)


