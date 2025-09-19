import json
import os

import allure
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate

load_dotenv()

base_api_url = os.getenv("BASE_API_URL")
payload = {
    "name": "morpheus",
    "job": "leader"
}
headers = {
    'x-api-key': 'reqres-free-v1',
    'Content-Type': 'application/json'
}


@allure.epic("API Tests")
@allure.tag("API", "POST")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.title("Создание нового пользователя")
@allure.description("Тест проверяет создание пользователя через POST запрос с валидацией JSON схемы")
def test_create_user():
    with allure.step("Отправка POST запроса на создание пользователя"):
        response = requests.post(base_api_url + '/users', headers=headers, json=payload)

    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 201

    with allure.step("Подготовка пути к JSON схеме"):
        current_dir = os.path.dirname(os.path.abspath(__file__))  # tests/API/
        tests_dir = os.path.dirname(current_dir)  # tests/
        project_root = os.path.dirname(tests_dir)  # diplom_project/
        schema_path = os.path.join(project_root, 'shemas', 'post_create_user.json')

    with allure.step("Загрузка и валидация JSON схемы"):
        with open(schema_path) as file:
            validate(response.json(), schema=json.loads(file.read()))
