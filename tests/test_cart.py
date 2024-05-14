import allure

from online_market.models.pages.cart_menu import cart_menu


@allure.parent_suite('UI Tests')
@allure.suite('Корзина')
@allure.title(f'Удаление монитора из корзины')
@allure.severity('Major')
@allure.label('owner', 'Глеб')
def test_del_display_in_cart(add_first_display_in_cart):
    cart_menu.del_product()

    cart_menu.should_del_product()
