import os
import sys
import pytest
from appium import webdriver
from dotenv import load_dotenv
from selene import browser

import config as app_config
from utils import attach


# Добавляем корневую директорию проекта в PYTHONPATH
# Поднимаемся на два уровня вверх от tests/mobile/ к корню проекта
project_root = os.path.dirname(os.path.dirname(os.path.dirname(os.path.abspath(__file__))))
if project_root not in sys.path:
    sys.path.insert(0, project_root)




def pytest_addoption(parser):
    parser.addoption(
        "--context",
        default="bstack",
        help="Specify the test context"
    )


def pytest_configure(config):  # Оставляем оригинальное имя параметра
    context = config.getoption("--context")
    env_file_path = f".env.{context}"

    if os.path.exists(env_file_path):
        load_dotenv(dotenv_path=env_file_path)
    else:
        print(f"Warning: Configuration file '{env_file_path}' not found.")


@pytest.fixture
def context(request):
    return request.config.getoption("--context")


@pytest.fixture(scope='function', autouse=True)
def mobile_management(context):
    options = app_config.to_driver_options(context=context)  # Используем переименованный импорт

    browser.config.driver = webdriver.Remote(options.get_capability('remote_url'), options=options)
    browser.config.timeout = 10.0

    yield

    attach.add_bstack_screenshot()
    attach.add_xml()
    session_id = browser.driver.session_id

    browser.quit()

    if context == 'bstack':
        attach.attach_bstack_video(session_id)
