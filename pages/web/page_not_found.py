import allure
from selene import browser, be


def open():
    with allure.step('Открыли странице 404'):
        browser.open('/used/changan/cs55plus/u2984265423423423424')


def check_not_found_page():
    # time.sleep(4)
    with allure.step('Проверяем страницу 404'):
        browser.element('//div[contains(@class, "tr-h1") and contains(text(), "404. Страница не найдена")]')
        browser.element('//div[contains(text(), "Страница была перемещена, или вы неверно указали адрес")]').should(
            be.visible)
        browser.element('//h2[contains(text(), "Рекомендованные авто")]').should(be.visible)
        browser.element('//tr-car-vertical-card').should(be.visible)
