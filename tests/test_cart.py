import allure

from online_market.models.pages.cart_menu import cart_menu
from online_market.models.pages.displays_page import displays_page


# @allure.label("owner", "Глеб")
# @allure.severity("Высокий")
# def test_add_first_display_in_cart():
#     displays_page.open()
#     cart_menu.add_first_display_in_cart()
#
#     cart_menu.should_display_in_cart()


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_del_display_in_cart(add_first_display_in_cart):
    cart_menu.del_product()

    cart_menu.should_del_product()
