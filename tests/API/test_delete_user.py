import os

import allure
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate

@allure.epic("API Tests")
@allure.tag("API", "DELETE")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.story("Delete User")
@allure.title("Удаление пользователя через DELETE запрос")
@allure.description("Тест проверяет корректное удаление пользователя и валидацию пустого ответа")
def test_delete_user_status_code(api_client):
    with allure.step("Отправка delete запроса на удаление пользователя"):
        response = api_client.delete('/users/2')
    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 204

    with allure.step("Загрузка и валидация JSON схемы"):
        empty_schema = {
            "type": "null"
        }
        response_data = response.json() if response.content else None
        validate(instance=response_data, schema=empty_schema)
