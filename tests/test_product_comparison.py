import allure
from selene import browser, have, query


def test_del_display_15_6_diagonal_in_compare_page():
    with allure.step("Открываем страницу сравнения товаров"):
        browser.all('.button').first.click()

    with allure.step("Проверяем что товары отображаются в списке сравнения"):
        browser.element('.col-sm-12').should(have.text('Сравнение товаров'))

    with allure.step("Удаляем первый дисплей со страницы сравнения"):
        products = browser.element('#details')
        uid = products.all('.compare-prd-img-wrap').first.element('.tag-compare-close'
                                                                  ).get(query.attribute('data-uid'))
        products.all('.compare-prd-img-wrap').first.element('.tag-compare-close').click()

    with (allure.step("Проверяем что первый дисплей удалился со страницы сравнения")):
        uid_after = products.all('.compare-prd-img-wrap').first.element('.tag-compare-close'
                                                                        ).get(query.attribute('data-uid'))
        assert uid != uid_after


def test_clear_list_in_compare_page():
    with allure.step("Очищаем список сравнения"):
        browser.element('.col-sm-12').element('.clear-compare-details').click()

    with allure.step("Проверяем что список сравнения пуст"):
        browser.element('.col-sm-12').should(have.text('Добавьте товары для сравнения'))
