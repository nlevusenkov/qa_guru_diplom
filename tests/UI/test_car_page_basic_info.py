import allure
from allure_commons.types import Severity

from pages.web.vdp_page import CarPage


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature("Открытие и проверка основной информации автомобиля")
@allure.story("VDP page")
def test_car_page_basic_info():
    car_page = CarPage()
    car_id = "u3002728"
    car_model = "Daewoo Matiz 2011"
    # \u00A0 добавляем для добавление неразрывных пробелов
    car_title = "Daewoo Matiz 2011 Красный в наличии в Автосалон М53.RU (Кемерово, Терешковой) от 249\u00A0995 в городе Кемерово"
    car_page.open()
    car_page.open_used_vdp_page(car_id)
    car_page.used_car_page_opened(car_id, car_model, car_title)
