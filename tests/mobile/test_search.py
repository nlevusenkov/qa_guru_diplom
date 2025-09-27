import allure
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be
from allure_commons.types import Severity


@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'nlevusenkov')
@allure.feature('Поиск')
@allure.title('Проверка поиска статьи')
def test_search():
    with allure.step('Кликнуть на кнопку Skip для пропуска онбординга'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_skip_button')).click()

    with allure.step('В поле поиска ввести значение Appium'):
        browser.element((AppiumBy.ACCESSIBILITY_ID, 'Search Wikipedia')).click()
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_src_text')).type('Appium')

    with allure.step('Проверить наличие статьи Appium в поисковой выдаче'):
        results = browser.all((AppiumBy.ID, 'org.wikipedia.alpha:id/page_list_item_title'))
        results.should(have.size_greater_than(0))
        results.first.should(have.text('Appium'))