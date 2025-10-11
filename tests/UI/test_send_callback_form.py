import allure
from allure_commons.types import Severity

from pages.web import vdp_page


@allure.tag("web")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature("Проверка отправки формы кредитного калькулятора")
@allure.story("VDP page")
def test_form():
    car_id = "u3002728"
    name = "тест"
    number = "79999999999"
    vdp_page.open()
    vdp_page.open_used_vdp_page(car_id)
    vdp_page.open_callback_form()
    vdp_page.fill_callback_form(name, number)
    vdp_page.check_open_thanks_modal()
