import allure
from selene import browser, have, command


def test_del_display_in_favorites_products_page():
    with allure.step("Открываем страницу с избранным"):
        browser.open('/favorites')

    with allure.step("Удаляем дисплей со страницы с избранным"):
        pass


def test_clear_list_in_favorites_products_page():
    with allure.step("Открываем страницу с избранным"):
        browser.open('/favorites')

    with allure.step("Очищаем список избранного"):
        pass
