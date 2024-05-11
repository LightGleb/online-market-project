import allure

from online_market.models.pages.cart_menu import cart_menu


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_del_display_in_cart(add_first_display_in_cart):
    cart_menu.del_product()

    cart_menu.should_del_product()
