import allure
from selene import browser


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_add_first_display_to_favorites_page():
    with allure.step("Открываем страницу с мониторами"):
        browser.open('/display')

    with allure.step("Открываем первый монитор"):
        pass

    with allure.step("Добавляем монитор в избранное"):
        pass

    with allure.step("Открываем страницу с избранным"):
        browser.open('/favorites')

    with allure.step("Проверяем что монитор добавился в избранное"):
        pass


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_add_first_ssd_to_favorites_page():
    with allure.step("Открываем страницу с ssd"):
        browser.open('/ssd')

    with allure.step("Открываем первый ssd"):
        pass

    with allure.step("Добавляем ssd в избранное"):
        pass

    with allure.step("Открываем страницу с избранным"):
        browser.open('/favorites')

    with allure.step("Проверяем что ssd добавился в избранное"):
        pass
