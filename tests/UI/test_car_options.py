import allure
import pytest
from allure_commons.types import Severity
from selene import browser

from pages.web.vdp_page import CarPage


@pytest.fixture(autouse=True)
def setup():
    car_page = CarPage()
    car_id = "u3012281"
    expected_titles = ["Обзор", "Защита от угона", "Мультимедиа", "Салон", "Комфорт", "Безопасность", "Прочее"]

    yield car_page, car_id, expected_titles



@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature("Проверка опций автомобиля")
@allure.story("VDP page")
def test_car_options(setup):
    car_page, car_id, expected_titles = setup
    car_page.open()
    car_page.open_used_vdp_page(car_id)
    car_page.open_tab_equipment()
    car_page.check_options_title(expected_titles)
    car_page.cheack_bottom_options()
