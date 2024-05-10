import allure
from selene import browser, command, query


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_add_first_display_to_favorites_page():
    with allure.step("Открываем страницу с мониторами"):
        browser.open('/display')

    with ((allure.step("Открываем первый монитор в списке"))):
        monitor = browser.element('#productsList')
        monitor.all('.item').first.perform(command.js.scroll_into_view).click()

    with allure.step("Добавляем монитор в избранное"):
        browser.element('.add-to-favorite').click()

    with allure.step("Проверяем что монитор добавился в избранное"):
        icon_favorite = browser.all('.button').second.element('sup').get(query.text)

        assert icon_favorite == '1'


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_add_first_iron_to_favorites_page():
    with allure.step("Открываем страницу с утюг"):
        browser.open('/iron')

    with allure.step("Открываем первый утюг в списке"):
        ssd = browser.element('#productsList')
        ssd.all('.item').first.perform(command.js.scroll_into_view).click()

    with allure.step("Добавляем утюг в избранное"):
        browser.element('.add-to-favorite').click()

    with allure.step("Проверяем что утюг добавился в избранное"):
        icon_favorite = browser.all('.button').second.element('sup').get(query.text)

        assert icon_favorite == '2'
