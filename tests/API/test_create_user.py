import json
import os
from pathlib import Path

import allure
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate

payload = {
    "name": "morpheus",
    "job": "leader"
}


@allure.epic("API Tests")
@allure.tag("API", "POST")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.title("Создание нового пользователя")
@allure.description("Тест проверяет создание пользователя через POST запрос с валидацией JSON схемы")
def test_create_user(api_client):
    with allure.step("Отправка POST запроса на создание пользователя"):
        response = api_client.post('/users', json=payload)

    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 201
        assert response.json()['name'] == "morpheus"
        assert response.json()['job'] == "leader"

    with allure.step("Загрузка и валидация JSON схемы"):
        project_root = Path(__file__).parent.parent.parent
        schema_path = project_root / 'shemas' / 'post_create_user.json'
        with open(schema_path) as file:
            validate(response.json(), schema=json.loads(file.read()))
