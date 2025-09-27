import time

import allure
from selene import browser, be, have


class FavoritesPage:

    @allure.step('Открываем главную страницу')
    def open_main_page(self):
        with allure.step('Открыли главную страницу'):
            browser.open('/used?order=price')
            time.sleep(5)

    @allure.step('Найти карточку автомобиля')
    def find_car_card(self, car_id: str):
        return browser.element(f'#car-{car_id}')

    @allure.step('Найти кнопку избранного в карточке')
    def find_favorites_button_in_card(self, car_id: str):
        car_card = self.find_car_card(car_id)
        return car_card.element(
            f'//*[@id="car-{car_id}"]/div[3]/div[2]/tr-favorite-button/div[1]/tr-button-navigational/button')

    @allure.step('Кликнуть на кнопку избранного в карточке {car_id}')
    def click_favorites_button_on_car(self, car_id: str):
        with allure.step(f'Кликаем на кнопку избранного автомобиля {car_id}'):
            favorites_button = self.find_favorites_button_in_card(car_id)
            favorites_button.click()
            browser.execute_script("window.scrollTo(0, 0);")

    def open_favorites_page(self):
        with allure.step('Открыли страницу с избранными авто'):
            browser.element('[icon="favorite"]').click()

    @allure.step('Проверить, что автомобиль в избранном')
    def check_car_in_favorites(self, brand, model, car_id):
        browser.element(f'a.tr-overlay-link[href="/buy-cars/used/{brand}/{model}/{car_id}"]').should(be.present)

    @allure.step('Оистка авто из избранного')
    def clear_favorites_page(self, text_title):
        browser.element('.tr-clear-btn').click()
        browser.element('[class*="tr-h2 tr-indent-bottom-sm tr-title"]').should(have.text(text_title))
