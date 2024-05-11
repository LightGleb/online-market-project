import allure
from selene import browser, query


class DisplayPage:

    def add_display_to_compare(self):
        with allure.step("Добавляем монитор к сравнению"):
            browser.element('.add-to-compare').click()
        return self

    def should_display_to_compare(self):
        with allure.step("Проверяем что монитор добавился в список сравнения"):
            icon_comparison = browser.all('.button').first.element('sup').get(query.text)

            assert icon_comparison == '1'
        return self

    def add_display_in_favorites(self):
        with allure.step("Добавляем монитор в избранное"):
            browser.element('.add-to-favorite').click()
        return self

    def should_display_in_favorites(self):
        with allure.step("Проверяем что монитор добавился в избранное"):
            icon_favorite = browser.all('.button').second.element('sup').get(query.text)

            assert icon_favorite == '1'
        return self


display_page = DisplayPage()
