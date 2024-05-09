import allure
from selene import browser, have, command


def test_del_display_15_6_diagonal_in_compare_page():
    with allure.step("Открываем страницу с мониторами"):
        browser.open('/display')

    with allure.step("Удаляем дисплей с диагональю 15.6 со страницы сравнения"):
        pass


def test_clear_list_in_compare_page():
    with allure.step("Открываем страницу с мониторами"):
        browser.open('/display')

    with allure.step("Очищаем список сравнения"):
        pass
