import allure
from allure_commons.types import Severity

from pages.web.vdp_page import CarPage


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature("Проверка опций автомобиля")
@allure.story("VDP page")
def test_car_options():
    car_page = CarPage()
    car_id = "u3002728"
    expected_titles = ["Мультимедиа", "Салон", "Комфорт", "Прочее"]
    car_page.open()
    car_page.open_used_vdp_page(car_id)
    car_page.open_tab_equipment()
    car_page.check_options_title(expected_titles)
    car_page.cheack_bottom_options()
