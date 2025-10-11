import json
from pathlib import Path

import allure
from allure_commons.types import Severity
from jsonschema import validate

payload = {
    "email": "eve.holt@reqres.in",
    "password": "pistol"
}


@allure.epic("API Tests")
@allure.tag("API", "POST")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.story("post User register")
def test_successful_register(api_client):
    with allure.step("Отправка post запроса на успешную регистрацию пользователя"):
        user_register = api_client.post('/register', json=payload)

    with allure.step("Проверка статус кода ответа"):
        assert user_register.status_code == 200

    with allure.step("Загрузка и валидация JSON схемы"):
        project_root = Path(__file__).parent.parent.parent
        schema_path = project_root / 'shemas' / 'register_user.json'
        with open(schema_path) as file:
            validate(user_register.json(), schema=json.loads(file.read()))

    with allure.step("Проверка дополнительных условий ответа"):
        assert user_register.json()['id']
        assert user_register.json()['token']
