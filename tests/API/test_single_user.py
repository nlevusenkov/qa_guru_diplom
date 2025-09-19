import os

import allure
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv

load_dotenv()

base_api_url = os.getenv("BASE_API_URL")
payload = {
    "name": "morpheus",
    "job": "zion resident"
}
headers = {
    'x-api-key': 'reqres-free-v1',
    'Content-Type': 'application/json'
}


@allure.epic("API Tests")
@allure.tag("API", "put", "users")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.story("put User invalid unauthorize")
def test_single_user_invalid_id_unauthorized():
    with allure.step("Отправка put запроса на авторизацию пользователя"):
        response = requests.put(base_api_url + '/users/2', data=payload)
    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 401

    with allure.step("Проверка json схемы"):
        assert response.json() == {
            'error': 'Missing API key'
        }


@allure.epic("API Tests")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature("User Management")
@allure.story("get User not found")
def test_users_not_found():
    with allure.step("Отправка put запроса на авторизацию пользователя"):
        response = requests.get("https://reqres.in/api/users/23", headers=headers)
    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 404
