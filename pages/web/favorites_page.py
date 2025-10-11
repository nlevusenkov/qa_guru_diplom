import allure
from selene import browser, be, have


@allure.step('Открыть главную страницу')
def open_main_page():
    browser.open('/used?order=price')
    browser.element('[id^="car-"]').should(be.visible)


@allure.step('Найти карточку автомобиля {car_id}')
def find_car_card(car_id):
    return browser.element(f'#car-{car_id}')


@allure.step('Найти кнопку избранного в карточке {car_id}')
def find_favorites_button_in_card(car_id):
    car_card = find_car_card(car_id)
    return car_card.element('.//tr-favorite-button//button')


@allure.step('Добавить автомобиль {car_id} в избранное')
def add_car_to_favorites(car_id):
    favorites_button = find_favorites_button_in_card(car_id)
    favorites_button.click()
    browser.execute_script("window.scrollTo(0, 0);")


@allure.step('Открыть страницу избранного')
def open_favorites_page():
    browser.element('[icon="favorite"]').click()


@allure.step('Проверить что автомобиль {car_id} в избранном')
def should_have_car_in_favorites(brand, model, car_id):
    browser.element(
        f'a.tr-overlay-link[href="/buy-cars/used/{brand}/{model}/{car_id}"]'
    ).should(be.present)


@allure.step('Оистка авто из избранного')
def clear_favorites_page(text_title):
    browser.element('.tr-clear-btn').click()
    browser.element('[class*="tr-h2 tr-indent-bottom-sm tr-title"]').should(have.text(text_title))
