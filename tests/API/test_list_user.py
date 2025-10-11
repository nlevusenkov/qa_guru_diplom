import json
import os
from pathlib import Path

import allure
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate


@allure.epic("API Tests")
@allure.tag("API", "get", "users")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.story("get User list")
@allure.title("Получение списка пользователей с пагинацией")
@allure.description("Тест проверяет получение списка пользователей со второй страницы с валидацией JSON схемы")
def test_list_users(api_client):
    with allure.step("Отправка get запроса на получение списка пользователей"):
        response = api_client.get('/users', params={'page': 2})

    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 200

    with allure.step("Загрузка и валидация JSON схемы"):
        project_root = Path(__file__).parent.parent.parent
        schema_path = project_root / 'shemas' / 'get_users.json'
        with open(schema_path) as file:
            validate(response.json(), schema=json.loads(file.read()))
