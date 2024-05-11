import allure

from online_market.models.pages.displays_page import displays_page


@allure.label("owner", "Глеб")
@allure.severity("Высокий")
def test_filter_display_diagonal_15_6_():
    displays_page.open()
    displays_page.click_filter_diagonal_15_6()

    displays_page.should_filter_diagonal_15_6()


