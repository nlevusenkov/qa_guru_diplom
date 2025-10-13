import allure
from selene import have, be, query
from selene.support.shared import browser
from selene.support.shared.jquery_style import ss


@allure.step('Открываем браузер на странице https://m53.ru/buy-cars/used')
def open():
    with allure.step("браузер открыт"):
        browser.open('/used?order=price')


@allure.step('Переходим на страницу автомобиля')
def open_used_vdp_page(car_id: str):
    with allure.step(f'Открыли автомобиль с id {car_id}'):
        # time.sleep(4)
        browser.element(f'#car-{car_id}').should(be.visible).click()


@allure.step('Проверяем страницу автомобиля')
def used_car_page_opened(car_id, car_model, car_title):
    # time.sleep(4)
    with allure.step(f'Идентификатор авто: {car_id}:'):
        browser.should(have.url_containing(car_id))
    with allure.step(f'Название модели: {car_model}:'):
        browser.element('.tr-title-content').should(have.text(car_model))
    with allure.step(f'Название заголовка: {car_title}:'):
        browser.should(have.title_containing(car_title))
    with allure.step('Цена присутсвует'):
        browser.element('.tr-price-content').should(be.visible)


@allure.step('Открываем вкладку опций')
def open_tab_equipment():
    with allure.step("Вкладка опций открыта"):
        browser.element('[id="tab_options"]').click()


@allure.step('Проверяем заголовки опций')
def check_options_title(expected_titles):
    actual_titles = [el.get(query.text).strip() for el in ss('.tr-head .tr-h4').by(be.visible)]
    assert len(actual_titles) == len(expected_titles), \
        f"Ожидали {len(expected_titles)} заголовков, но нашли {len(actual_titles)}: {actual_titles}"
    # Проверяем тексты
    with allure.step(f"Текста заголовков: {expected_titles}"):
        assert actual_titles == expected_titles, \
            f"Ожидали заголовки: {expected_titles}, но нашли: {actual_titles}"


@allure.step('Проверяем Название кнопки')
def cheack_bottom_options():
    with allure.step('Смотрим название кнопки когда табы свернуты'):
        browser.element('//*[@id="tabs"]/tr-vdp-description/div[3]/div/tr-options/div/div[2]/button').should(
            have.text("Посмотреть все опции"))
    with allure.step('Нажимаем на кнопку'):
        browser.element('//*[@id="tabs"]/tr-vdp-description/div[3]/div/tr-options/div/div[2]/button').click()
    with allure.step('Смотрим название кнопки когда табы открыты'):
        browser.element('//*[@id="tabs"]/tr-vdp-description/div[3]/div/tr-options/div/div[2]/button').should(
            have.text("Свернуть все опции"))


def open_callback_form():
    with allure.step("Открыли форму отправки заявки"):
        browser.element('[class*="tr-block tr-size-lg tr-fill-secondary ng-star-inserted"]').should(be.visible).click()


def fill_callback_form(name, number):
    with allure.step(f'Заполняем Имя: {name}'):
        browser.element('.tr-modal input[formcontrolname="name"]').type(name)
    with allure.step(f'Заполняем телефон: {number}'):
        browser.element('.tr-modal input[autocomplete="tel"]').type(number)
    with allure.step('Проставляем чекбокс политик'):
        browser.element('.tr-modal .tr-agreement-checkbox').click()
    with allure.step('Отправляем форму'):
        browser.element('.tr-modal .tr-middle-slot').click()


def check_open_thanks_modal():
    with allure.step('Проверяем содержение спасибки формы'):
        # time.sleep(5)
        browser.element('/html/body/tr-modal-window/div/div/tr-thanks-modal').should(be.visible)
        browser.element('/html/body/tr-modal-window/div/div/tr-thanks-modal/tr-modal-layout/div[2]/div[2]/h2').should(
            have.text('Ваша заявка отправлена!'))
