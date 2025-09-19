import json
import os

import allure
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate

load_dotenv()

base_api_url = os.getenv("BASE_API_URL")
headers = {
    'x-api-key': 'reqres-free-v1',
    'Content-Type': 'application/json'
}

payload = {"email": "b9@ya.ru"}


@allure.epic("API Tests")
@allure.tag("API", "POST")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.title('Unsuccessful register')
def test_unsuccessful_register():
    with allure.step("Отправка post запроса на не успешную регистрацию пользователя"):
        user_register = requests.post(base_api_url + '/register', json=payload, headers=headers)

    with allure.step("Проверка статус кода ответа"):
        assert user_register.status_code == 400

    with allure.step("Подготовка пути к JSON схеме"):
        current_dir = os.path.dirname(os.path.abspath(__file__))  # tests/API/
        tests_dir = os.path.dirname(current_dir)  # tests/
        project_root = os.path.dirname(tests_dir)  # diplom_project/
        schema_path = os.path.join(project_root, 'shemas', 'unsuccessful_register.json')

    with allure.step("Загрузка и валидация JSON схемы"):
        with open(schema_path) as file:
            validate(user_register.json(), schema=json.loads(file.read()))

    with allure.step("Проверка дополнительных условий ответа"):
        assert user_register.json()['error'] == 'Missing password'
