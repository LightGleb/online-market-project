import allure

from online_market.models.pages.compare_page import compare_page


@allure.parent_suite('UI Tests')
@allure.suite('Список сравнения')
@allure.title(f'Удаление монитора из списка сравнения')
@allure.severity('Major')
@allure.label('owner', 'Глеб')
def test_del_display_in_compare_page(add_first_display_to_compare):
    compare_page.open()
    compare_page.del_product()

    compare_page.should_clear_list()


@allure.parent_suite('UI Tests')
@allure.suite('Список сравнения')
@allure.title(f'Очистка списка сравнения')
@allure.severity('Major')
@allure.label('owner', 'Глеб')
def test_clear_list_in_compare_page(add_first_display_to_compare):
    compare_page.open()
    compare_page.clear_list()

    compare_page.should_clear_list()
