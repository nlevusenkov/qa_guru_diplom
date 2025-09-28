import os

import pytest
from dotenv import load_dotenv
from selene import browser
from selenium import webdriver

from utils import attach

load_dotenv()


@pytest.fixture(scope='function', autouse=True)
def setting_browser():
    login = os.getenv("SELENIUM_USER")
    password = os.getenv("SELENIUM_PASS")
    options = webdriver.ChromeOptions()
    options.set_capability("goog:loggingPrefs", {"browser": "ALL"})
    selenoid_capabilities = {
        "browserName": "chrome",
        "browserVersion": "128.0",
        "selenoid:options": {
            "enableVNC": True,
            "enableVideo": True,
            "enableLog": True
        },
    }
    options.capabilities.update(selenoid_capabilities)
    driver = webdriver.Remote(
        command_executor=f"https://{login}:{password}@selenoid.autotests.cloud/wd/hub",
        options=options
    )
    browser.config.driver = driver
    browser.config.base_url = 'https://m53.ru/buy-cars'
    browser.config.window_width = 1920
    browser.config.window_height = 1080

    yield browser

    attach.add_screenshot(browser)
    attach.add_html(browser)
    attach.add_video(browser)
    browser.quit()