import allure
from allure_commons.types import Severity

from pages.web import favorites_page


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "nlevusenkov")
@allure.feature("Проверка добавления авто в избранное")
@allure.story("Страница избранных")
def test_add_car_to_favorites():
    test_car_id = "u3034981"
    brand = "daewoo"
    model = "matiz"

    favorites_page.open_main_page()
    favorites_page.add_car_to_favorites(test_car_id)
    favorites_page.open_favorites_page()
    favorites_page.should_have_car_in_favorites(brand, model, test_car_id)
