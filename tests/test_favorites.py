import allure

from online_market.models.pages.favorites_page import favorites_page


@allure.parent_suite('UI Tests')
@allure.suite('Список избранного')
@allure.title(f'Удаление монитора из списка избранного')
@allure.severity('Major')
@allure.label('owner', 'Глеб')
def test_del_display_in_favorites_page(add_first_display_in_favorites):
    favorites_page.open()
    favorites_page.del_product()

    favorites_page.should_clear_list()


@allure.parent_suite('UI Tests')
@allure.suite('Список избранного')
@allure.title(f'Очистка списка избранного')
@allure.severity('Major')
@allure.label('owner', 'Глеб')
def test_clear_list_in_favorites_page(add_first_display_in_favorites):
    favorites_page.open()
    favorites_page.clear_list()

    favorites_page.should_clear_list()
