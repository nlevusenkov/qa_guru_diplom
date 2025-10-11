import allure
from allure_commons.types import Severity
from selene import be

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
    car_card = favorites_page.find_car_card(test_car_id)
    car_card.should(be.visible)
    favorites_page.add_car_to_favorites(test_car_id)
    favorites_page.find_favorites_button_in_card(test_car_id)
    favorites_page.open_favorites_page()
    favorites_page.should_have_car_in_favorites(brand, model, test_car_id)
    favorites_page.clear_favorites_page("В избранном пусто")
