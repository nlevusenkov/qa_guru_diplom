import allure
from allure import step
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have


@allure.story('Проверки приветственных страниц Wikipedia')
@allure.severity(allure.severity_level.NORMAL)
@allure.label('owner', 'nlevusenkov')
@allure.tag('Mobile')
def test_skip_pages():
    with step('Проверить текст на первой странице'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('The Free Encyclopedia\n…in over 300 languages'))
    with step('Кликнуть "Continue"'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    with step('Проверить текст на второй странице'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('New ways to explore'))
    with step('Кликнуть "Continue"'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    with step('Проверить текст на третьей странице'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Reading lists with sync'))
    with step('Кликнуть "Continue"'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()
    with step('Проверить текст на четвертой странице'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')).should(
            have.text('Data & Privacy'))
