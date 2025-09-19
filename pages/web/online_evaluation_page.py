from selene.support.shared import browser


class OnlineEvaluationPage:
    def open_online_evaluation_page(self):
        browser.element(
            '//*[@id="root"]/tr-newcars-vdp/tr-vdp-version-1/div/tr-about/div/div[3]/div[2]/div/div[1]/button').click()
        browser.element('//button[.//span[contains(text(), "Оценить онлайн")]]').click()

    def fill_state_number(self, state_number):
        browser.element('//tr-control[.//div[contains(text(), "Укажите Госномер")]]//input').type(state_number)
        browser.element('//button[.//span[contains(text(), "Определить автомобиль")]]').click()

    def check_result_no_evaluation(self):
        browser.element('[class*="tr-block tr-indent-top-lg tr-size-lg tr-fill-primary ng-star-inserted"]').click()
        browser.element('//form//button[.//span[contains(text(), "Рассчитать")]]').click()
        browser.element(
            '//tr-evaluation-not-available//*[contains(text(), "К сожалению, данный автомобиль невозможно оценить онлайн")]')
