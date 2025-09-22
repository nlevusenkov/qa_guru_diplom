import allure
from allure_commons.types import Severity

from pages.web.vdp_page import CarPage


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature("Проверка отправки формы кредитного калькулятора")
@allure.story("VDP page")
def test_form():
    car_page = CarPage()
    car_id = "u3013249"
    name = "тест"
    number = "79999999999"
    car_page.open()
    car_page.open_used_vdp_page(car_id)
    car_page.open_callback_form()
    car_page.fill_callback_form(name, number)
    car_page.check_open_thanks_modal()
