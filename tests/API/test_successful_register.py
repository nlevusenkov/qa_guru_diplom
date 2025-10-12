import allure
import pytest
from allure_commons.types import Severity
from pydantic import ValidationError

from models.model import RegisterResponse

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
        user_register = api_client.post('/register', json=payload, expected_status=200)

    with allure.step("Валидация ответа по схеме"):
        try:
            RegisterResponse(**user_register)
        except ValidationError as e:
            pytest.fail(f"Схема ответа не валидна: {e}")

    with allure.step("Проверка дополнительных условий ответа"):
        assert user_register['id']
        assert user_register['token']
