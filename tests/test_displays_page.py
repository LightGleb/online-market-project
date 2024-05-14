import allure

from online_market.models.pages.displays_page import displays_page


@allure.parent_suite('UI Tests')
@allure.suite('Категория "Дисплеи"')
@allure.title(f'Проверка фильтра "Диагональ" значение "15.6"')
@allure.severity('Major')
@allure.label('owner', 'Глеб')
def test_filter_display_diagonal_15_6_():
    displays_page.open()
    displays_page.click_filter_diagonal_15_6()

    displays_page.should_filter_diagonal_15_6()
