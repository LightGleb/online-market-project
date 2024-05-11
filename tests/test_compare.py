import allure
from selene import browser, have, command, query

from online_market.models.pages.compare_page import compare_page


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_del_display_in_compare_page(add_first_display_to_compare):
    compare_page.open()
    compare_page.del_product()

    compare_page.should_clear_list()


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_clear_list_in_compare_page(add_first_display_to_compare):
    compare_page.open()
    compare_page.clear_list()

    compare_page.should_clear_list()
