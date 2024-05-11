import allure
from selene import browser, have, query


class ComparePage:

    def open(self):
        with allure.step("Открываем страницу сравнения товаров"):
            browser.all('.button').first.click()
        return self

    def del_product(self):
        with allure.step("Удаляем товар со страницы сравнения"):
            products = browser.element('#details')
            products.all('.compare-prd-img-wrap').first.element('.tag-compare-close').click()
        return self

    def clear_list(self):
        with allure.step("Очищаем список сравнения"):
            browser.element('.col-sm-12').element('.clear-compare-details').click()
        return self

    def should_clear_list(self):
        with allure.step("Проверяем что список сравнения пуст"):
            browser.element('.col-sm-12').should(have.text('Добавьте товары для сравнения'))
        return self


compare_page = ComparePage()
