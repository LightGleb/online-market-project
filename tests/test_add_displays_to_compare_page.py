import allure
from selene import browser, have


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_add_first_display_15_6_diagonal_to_compare_page():
    with allure.step("Открываем страницу с мониторами"):
        browser.open('/display')

    with (allure.step("Проставляем значение фильтра 'Диагональ' как '15.6'")):
        diagonal = browser.element('#collapse-Diagonal')
        diagonal.all('.block-element').element_by_its('label', have.text('15.6')
                                                      ).element('[type="checkbox"]').click()

    # with ((allure.step("Открываем первый монитор в списке"))):
    #     first_monitor = browser.all('.product stock-0'
    #                                 ).first.element('.image').get(query.attribute("href"))
    #     browser.open(first_monitor)

    with allure.step("Добавляем монитор к сравнению"):
        pass

    with allure.step("Проверяем что монитор добавился в список сравнения"):
        pass


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_add_first_display_21_5_diagonal_to_compare_page():
    with allure.step("Открываем страницу с мониторами"):
        browser.open('/display')

    with (allure.step("Проставляем значение фильтра 'Диагональ' как '21.5'")):
        diagonal = browser.element('#collapse-Diagonal')
        diagonal.all('.block-element').element_by_its('label', have.text('21.5')
                                                      ).element('[type="checkbox"]').click()

        # with ((allure.step("Открываем первый монитор в списке"))):
        #     first_monitor = browser.all('.product stock-0'
        #                                 ).first.element('.image').get(query.attribute("href"))
        #     browser.open(first_monitor)

    with allure.step("Добавляем монитор к сравнению"):
        pass

    with allure.step("Проверяем что монитор добавился в список сравнения"):
        pass
