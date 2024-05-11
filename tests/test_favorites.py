import allure

from online_market.models.pages.favorites_page import favorites_page


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_del_display_in_favorites_page(add_first_display_in_favorites):
    favorites_page.open()
    favorites_page.del_product()


def test_clear_list_in_favorites_page(add_first_display_in_favorites):
    favorites_page.open()
    favorites_page.clear_list()

    favorites_page.should_clear_list()
