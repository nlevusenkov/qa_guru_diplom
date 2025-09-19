import allure
from allure_commons.types import Severity
from appium.webdriver.common.appiumby import AppiumBy
from selene import browser, have, be


@allure.tag('mobile')
@allure.severity(Severity.NORMAL)
@allure.label('owner', 'fgoncharenko')
@allure.feature('Онбординг')
@allure.title('Проверка текста онбординг скрина')
def test_onboarding_texts():
    with allure.step('Проверить текст на первой странице онбординга'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('The Free Encyclopedia\n…in over 300 languages'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')
                        ).should(have.text('We’ve found the following on your device:'))

    with allure.step('Кликнуть на кнопку Continue'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Проверить текст на второй странице онбординга'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('New ways to explore'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')
                        ).should(have.text(
            'Dive down the Wikipedia rabbit hole with a constantly updating Explore feed. \n'
            'Customize the feed to your interests – whether it’s learning about historical events '
            'On this day, or rolling the dice with Random.'))

    with allure.step('Кликнуть на кнопку Continue'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Проверить текст на третьей странице онбординга'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Reading lists with sync'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')
                        ).should(have.text(
            'You can make reading lists from articles you want to read later, even when you’re offline. \n'
            'Login to your Wikipedia account to sync your reading lists. Join Wikipedia'))

    with allure.step('Кликнуть на кнопку Continue'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_forward_button')).click()

    with allure.step('Проверить текст на четвертой странице онбординга'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/primaryTextView')
                        ).should(have.text('Data & Privacy'))

        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/secondaryTextView')
                        ).should(have.text(
            'We believe that you should not have to provide personal information to participate in the free knowledge '
            'movement. Usage data collected for this app is anonymous. '
            'Learn more about our privacy policy and terms of use.'))

    with allure.step('Проверить текст кнопки Get Started'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')
                        ).should(have.text('Get started'))

    with allure.step('Кликнуть на кнопку Get started'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/fragment_onboarding_done_button')).click()

    with allure.step('Проверить наличие поля поиска'):
        browser.element((AppiumBy.ID, 'org.wikipedia.alpha:id/search_container')).should(be.visible)
