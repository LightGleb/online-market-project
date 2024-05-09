import allure
from selene import browser, have, query


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_add_first_display_to_cart():
    with allure.step("Открываем страницу с мониторами"):
        browser.open('/display')

    with allure.step("Добавляем первый в списке монитор в корзину"):
        first_monitor = browser.all('.action-control').first.element('.btn-primary')
        first_monitor.click()

    with (allure.step("Проверяем что первый монитор добавился в корзину")):

        name_first_monitor_in_list = browser.all('.product stock-0'
                                                 ).first.element('.image').element('.img-responsive').get(query.attribute("alt"))
        pass
        # name_monitor_in_cart =
        # assert name_first_monitor_in_list == name_monitor_in_cart


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_del_display_to_cart():
    with allure.step("Открываем страницу с мониторами"):
        browser.open('/display')

    with allure.step("Открываем корзину"):
        browser.element('#cart-link').click()

    # with allure.step("Удаляем монитор из корзины"):
    #     browser.element('.miniCartDelete').element('.delA').click()
    #     pass

    with allure.step("Проверяем что монитор удалился из корзины"):
        pass
