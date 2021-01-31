# launch: pytest -v --tb=line --language=en test_product_page.py
import pytest
from .pages.product_page import ProductPage


@pytest.mark.parametrize("offer", ["0", "1", "2", "3", "4", "5", "6",
                                   pytest.param("bugged_link", marks=pytest.mark.xfail), "8", "9"])
def test_guest_can_add_product_to_basket(browser, offer):
    # link = "http://selenium1py.pythonanywhere.com/catalogue/the-shellcoders-handbook_209/?promo=newYear"
    # link = "http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=newYear2019"
    link = f"http://selenium1py.pythonanywhere.com/catalogue/coders-at-work_207/?promo=offer{offer}"
    page = ProductPage(browser, link)
    page.open()
    page.add_product_to_cart()
    page.solve_quiz_and_get_code()
    page.name_of_cart_product_equal_added_product()
    page.cost_of_cart_product_equal_price_added_product()
