import time

import allure
from selene import have
from selene.support.shared import browser


def open_online_evaluation_page():
    with allure.step('Open Online Evaluation Page'):
        browser.element(
            '//*[@id="root"]/tr-newcars-vdp/tr-vdp-version-1/div/tr-about/div/div[3]/div[2]/div/div[1]/button').click()
        browser.element('//button[.//span[contains(text(), "Оценить онлайн")]]').click()


def fill_state_number(state_number):
    with allure.step('Заполняем гос номер авто'):
        browser.element('//tr-control[.//div[contains(text(), "Укажите Госномер")]]//input').type(state_number)


def find_auto():
    with allure.step('Ищем автомобиль'):
        browser.element('//button[.//span[contains(text(), "Определить автомобиль")]]').click()


def go_to_next_page():
    with allure.step('Переходим на страницу результата оценки'):
        browser.element(
            '//*[@id="tr-locator-app-top"]/tr-online-evaluation-steps-form/div[2]/form/div/tr-online-evaluation-choice-run/div/tr-online-evaluation-accordion-slider-step/button').click()
        browser.element('tr-online-evaluation-start-page button[type="submit"]').click()


def check_result_no_evaluation():
    with allure.step('Проверка содержания страницы не успешной оценки авто'):
        # time.sleep(4)
        browser.element('tr-online-evaluation-start-page .tr-h3').should(
            have.text("К сожалению, данный автомобиль невозможно оценить онлайн"))
