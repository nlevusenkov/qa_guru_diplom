import allure
from allure_commons.types import Severity

from pages.web import vdp_page


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature("Проверка опций автомобиля")
@allure.story("VDP page")
def test_car_options():
    car_id = "u3002728"
    expected_titles = ["Мультимедиа", "Салон", "Комфорт", "Прочее"]
    vdp_page.open()
    vdp_page.open_used_vdp_page(car_id)
    vdp_page.open_tab_equipment()
    vdp_page.check_options_title(expected_titles)
    vdp_page.cheack_bottom_options()
