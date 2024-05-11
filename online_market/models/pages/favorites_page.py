import allure
from selene import browser, have, query


class FavoritesPage:

    def open(self):
        with allure.step("Открываем страницу с избранным"):
            browser.all('.button').second.click()
        return self

    def del_product(self):
        with allure.step("Удаляем товар со страницы с избранным и проверяем что удалился"):
            products = browser.element('#productsList')
            uid = products.all('.item').first.element('.tag-fav-close').get(query.attribute('data-uid'))
            products.all('.item').first.element('.tag-fav-close').click()
            uid_after = products.all('.item').first.element('.tag-fav-close').get(query.attribute('data-uid'))

        with allure.step("Проверяем что товар удалился удалился"):
            assert uid != uid_after
        return self

    def clear_list(self):
        with allure.step("Очищаем список избранного"):
            browser.element('#clearFavorites').click()
        return self

    def should_clear_list(self):
        with allure.step("Проверяем что список избранного пуст"):
            browser.element('.productFilter').element('p').should(have.text('Найдено 0 избранных товаров'))
        return self


favorites_page = FavoritesPage()
