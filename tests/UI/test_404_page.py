import allure
from allure_commons.types import Severity

from pages.web.not_found_page import NotFoundPage


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "nlevusenkov")
@allure.feature("Проверка Страницы 404")
@allure.story("Страница 404")
def test_404_scenario_in_main_flow(setting_browser):
    PagenotFound = NotFoundPage()
    PagenotFound.open_not_found_page()
    PagenotFound.check_not_found_page()
