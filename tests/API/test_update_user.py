import json
from pathlib import Path

import allure
from allure_commons.types import Severity
from jsonschema import validate

payload = {
    "name": "morpheus",
    "job": "zion resident"
}


@allure.epic("API Tests")
@allure.tag("API", "PUT")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.title('update user')
@allure.title("Обновление пользователя")
@allure.description("Тест проверяет обновление пользователя с валидацией JSON схемы")
def test_update_user_status(api_client):
    name = "morpheus"
    job = "zion resident"
    with allure.step("Отправка put запроса на обновление пользователя"):
        response = api_client.put('/users/2', json=payload)

    with allure.step("Загрузка и валидация JSON схемы"):
        project_root = Path(__file__).parent.parent.parent
        schema_path = project_root / 'shemas' / 'put_update_user.json'
        with open(schema_path) as file:
            validate(response.json(), schema=json.loads(file.read()))

    with allure.step("Проверка статус кода ответа"):
        assert response.status_code == 200

    with allure.step("Проверка дополнительных условий ответа"):
        assert response.json()["name"] == name
        assert response.json()["job"] == job
