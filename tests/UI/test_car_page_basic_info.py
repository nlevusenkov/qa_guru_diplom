import allure
import pytest
from allure_commons.types import Severity

from pages.web.vdp_page import CarPage


class TestCarPage:
    @pytest.fixture(autouse=True)
    def setup(self):
        self.car_page = CarPage()
        self.car_id = "u3012281"
        self.car_model = "Toyota RAV4 2010"
        # \u00A0 добавляем для добавление неразрывных пробелов
        self.car_title = "Toyota RAV4 2010 Красный в наличии в Автосалон М53.RU (Кемерово, Терешковой) от 1\u00A0615\u00A0995 в городе Кемерово"

    @allure.tag("web")
    @allure.severity(Severity.BLOCKER)
    @allure.label("owner", "nlevusenkov")
    @allure.feature("Открытие и проверка основной информации автомобиля")
    @allure.story("VDP page")
    def test_car_page_basic_info(self):
        self.car_page.open()
        self.car_page.open_used_vdp_page(self.car_id)
        self.car_page.used_car_page_opened(self.car_id, self.car_model, self.car_title)
