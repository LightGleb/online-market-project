import allure
from selene import browser, have, command, query


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_add_first_display_15_6_diagonal_to_compare_page():
    with allure.step("Открываем страницу с мониторами"):
        browser.open('/display')

    with (allure.step("Проставляем значение фильтра 'Диагональ' как '15.6'")):
        diagonal = browser.element('#collapse-Diagonal')
        diagonal.all('.block-element').element_by_its('label', have.text('15.6')
                                                      ).element('[type="checkbox"]').click()

    with (allure.step("Проверяем что фильтр успешно применился")):
        monitor = browser.element('#productsList')
        monitor.all('.item').first.should(have.text('15.6'))

    with ((allure.step("Открываем первый монитор в списке"))):
        monitor.all('.item').first.perform(command.js.scroll_into_view).click()

    with allure.step("Добавляем монитор к сравнению"):
        browser.element('.add-to-compare').click()

    with allure.step("Проверяем что монитор добавился в список сравнения"):
        icon_comparison = browser.all('.button').first.element('sup').get(query.text)

        assert icon_comparison == '1'


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_add_first_display_21_5_diagonal_to_compare_page():
    with allure.step("Открываем страницу с мониторами"):
        browser.open('/display')

    with (allure.step("Проставляем значение фильтра 'Диагональ' как '16'")):
        diagonal = browser.element('#collapse-Diagonal')
        diagonal.all('.block-element').element_by_its('label', have.text('16')
                                                      ).element('[type="checkbox"]').click()

    with (allure.step("Проверяем что фильтр успешно применился")):
        monitor = browser.element('#productsList')
        monitor.all('.item').first.should(have.text('16'))

    with ((allure.step("Открываем первый монитор в списке"))):
        monitor.all('.item').first.perform(command.js.scroll_into_view).click()

    with allure.step("Добавляем монитор к сравнению"):
        browser.element('.add-to-compare').click()

    with allure.step("Проверяем что монитор добавился в список сравнения"):
        icon_comparison = browser.all('.button').first.element('sup').get(query.text)

        assert icon_comparison == '2'
