import allure
from selene import browser, have, query


def test_del_display_in_favorites_products_page():
    with allure.step("Открываем страницу с избранным"):
        browser.all('.button').second.click()

    with allure.step("Проверяем что товары отображаются в избранном"):
        browser.element('.productFilter').element('p').should(have.text('Найдено 2 избранных товара'))

    with allure.step("Удаляем первый товар со страницы с избранным"):
        products = browser.element('#productsList')
        uid = products.all('.item').first.element('.tag-fav-close').get(query.attribute('data-uid'))
        products.all('.item').first.element('.tag-fav-close').click()

    with allure.step("Проверяем что первый товар удалился со страницы с избранным"):
        uid_after = products.all('.item').first.element('.tag-fav-close').get(query.attribute('data-uid'))
        assert uid != uid_after


def test_clear_list_in_favorites_products_page():
    with allure.step("Очищаем список избранного"):
        browser.element('#clearFavorites').click()

    with allure.step("Проверяем что список избранного пуст"):
        browser.element('.productFilter').element('p').should(have.text('Найдено 0 избранных товаров'))
