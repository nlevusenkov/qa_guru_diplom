import json
import os
from pathlib import Path

import allure
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate


payload = {"email": "b9@ya.ru"}


@allure.epic("API Tests")
@allure.tag("API", "POST")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.title('Unsuccessful register')
def test_unsuccessful_register(api_client):
    with allure.step("Отправка post запроса на не успешную регистрацию пользователя"):
        user_register = api_client.post('/register', json=payload)

    with allure.step("Проверка статус кода ответа"):
        assert user_register.status_code == 400

    with allure.step("Загрузка и валидация JSON схемы"):
        project_root = Path(__file__).parent.parent.parent
        schema_path = project_root / 'shemas' / 'unsuccessful_register.json'
        with open(schema_path) as file:
            validate(user_register.json(), schema=json.loads(file.read()))

    with allure.step("Проверка дополнительных условий ответа"):
        assert user_register.json()['error'] == 'Missing password'
