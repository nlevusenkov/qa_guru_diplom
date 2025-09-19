import time

from selene import browser, be


class NotFoundPage:

    def open_not_found_page(self):
        browser.open('/used/changan/cs55plus/u2984265423423423424')

    def check_not_found_page(self):
        time.sleep(4)
        browser.element('//div[contains(@class, "tr-h1") and contains(text(), "404. Страница не найдена")]')
        browser.element('//div[contains(text(), "Страница была перемещена, или вы неверно указали адрес")]').should(
            be.visible)
        browser.element('//h2[contains(text(), "Рекомендованные авто")]').should(be.visible)
        browser.element('//tr-car-vertical-card').should(be.visible)
