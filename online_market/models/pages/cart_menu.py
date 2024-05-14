import allure
from selene import browser, have, be


class CartMenu:

    def add_first_product(self):
        with allure.step("Добавляем первый в списке монитор в корзину"):
            first_monitor = browser.all('.action-control').first.element('.btn-primary')
            first_monitor.click()
        return self

    def should_product(self):
        with (allure.step("Проверяем что монитор добавился в корзину")):
            browser.element('.cartMenu .cartRespons').should(have.text('1 ТОВАР')).hover()
        return self

    def del_product(self):
        with allure.step("Удаляем монитор из корзины"):
            browser.element('.dropdown-menu .delA').click()
        return self

    def should_del_product(self):
        with allure.step("Проверяем что монитор удалился из корзины"):
            browser.element('.cartMenu .cartRespons').should(be.not_.visible)
        return self


cart_menu = CartMenu()
