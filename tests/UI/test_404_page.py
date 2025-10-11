import allure
from allure_commons.types import Severity

from pages.web import page_not_found


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "nlevusenkov")
@allure.feature("Проверка Страницы 404")
@allure.story("Страница 404")
def test_404_scenario_in_main_flow():
    page_not_found.open()
    page_not_found.check_not_found_page()
