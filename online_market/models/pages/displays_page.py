import allure
from selene import browser, have, command


class DisplaysPage:

    def open(self):
        with allure.step("Открываем страницу с мониторами"):
            browser.open('/display')
        return self

    def click_filter_diagonal_15_6(self):
        with (allure.step("Проставляем значение фильтра 'Диагональ' как '15.6'")):
            diagonal = browser.element('#collapse-Diagonal')
            diagonal.all('.block-element').element_by_its('label', have.text('15.6')
                                                          ).element('[type="checkbox"]').click()
        return self

    def should_filter_diagonal_15_6(self):
        with (allure.step("Проверяем что фильтр 'Диагональ' как '15.6' успешно применился")):
            monitor = browser.element('#productsList')
            monitor.all('.item').first.should(have.text('15.6'))
        return self

    def open_first_display(self):
        with allure.step("Открываем первый монитор в списке"):
            monitor = browser.element('#productsList')

            monitor.all('.item').first.perform(command.js.scroll_into_view).click()

        with allure.step("Проверяем что открылся первый монитор"):
            pass
        #           todo: добавить проверку
        return self


displays_page = DisplaysPage()
