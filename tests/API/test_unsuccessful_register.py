import allure
import pytest
from allure_commons.types import Severity
from pydantic import ValidationError

from models.model import ErrorResponse

payload = {"email": "b9@ya.ru"}


@allure.epic("API Tests")
@allure.tag("API", "POST")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.title('Unsuccessful register')
def test_unsuccessful_register(api_client):
    with allure.step("Отправка post запроса на не успешную регистрацию пользователя"):
        user_register = api_client.post('/register', json=payload, expected_status=400)

    with allure.step("Валидация ответа по схеме"):
        try:
            ErrorResponse(**user_register)
        except ValidationError as e:
            pytest.fail(f"Схема ответа не валидна: {e}")

    with allure.step("Проверка дополнительных условий ответа"):
        assert user_register['error'] == 'Missing password'
