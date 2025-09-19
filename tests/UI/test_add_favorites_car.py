import allure
from allure_commons.types import Severity
from selene import be

from pages.web.favorites_page import FavoritesPage


@allure.tag("web")
@allure.severity(Severity.NORMAL)
@allure.label("owner", "nlevusenkov")
@allure.feature("Проверка добавления авто в избранное")
@allure.story("Страница избранных")
def test_add_car_to_favorites():
    test_car_id = "u3012281"
    brand = "toyota"
    model = "rav4-2010"
    car_page = FavoritesPage()

    car_page.open_main_page()
    car_card = car_page.find_car_card(test_car_id)
    car_card.should(be.visible)
    car_page.click_favorites_button_on_car(test_car_id)
    car_page.open_favorites_page()
    car_page.check_car_in_favorites(brand, model, test_car_id)
