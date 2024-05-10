import allure
from selene import browser, have, be


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_add_first_display_to_cart():
    with allure.step("Открываем страницу с мониторами"):
        browser.open('/display')

    with allure.step("Добавляем первый в списке монитор в корзину"):
        first_monitor = browser.all('.action-control').first.element('.btn-primary')
        first_monitor.click()

    with (allure.step("Проверяем что монитор добавился в корзину")):
        browser.element('.cartMenu .cartRespons').should(have.text('1 ТОВАР')).hover()


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_del_display_to_cart():
    with allure.step("Открываем страницу с мониторами"):
        browser.open('/display')

    with allure.step("Открываем корзину"):
        browser.element('#cart-link').click()

    with allure.step("Удаляем монитор из корзины"):
        browser.element('.dropdown-menu .delA').click()

    with allure.step("Проверяем что монитор удалился из корзины"):
        browser.element('.cartMenu .cartRespons').should(be.not_.visible)
