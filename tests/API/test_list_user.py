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


@allure.epic("API Tests")
@allure.tag("API", "get", "users")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.story("get User list")
@allure.title("Получение списка пользователей с пагинацией")
@allure.description("Тест проверяет получение списка пользователей со второй страницы с валидацией JSON схемы")
def test_list_users():
    with allure.step("Отправка get запроса на получение списка пользователей"):
        response = requests.get(base_api_url + '/users?page=2', headers=headers)

    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 200

    with allure.step("Подготовка пути к JSON схеме"):
        current_dir = os.path.dirname(os.path.abspath(__file__))  # tests/API/
        tests_dir = os.path.dirname(current_dir)  # tests/
        project_root = os.path.dirname(tests_dir)  # diplom_project/
        schema_path = os.path.join(project_root, 'shemas', 'get_users.json')

    with allure.step("Загрузка и валидация JSON схемы"):
        with open(schema_path) as file:
            validate(response.json(), schema=json.loads(file.read()))
