import allure
from allure_commons.types import Severity
from pydantic import ValidationError

from models.model import UpdateUserResponse

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

    with allure.step("Валидация ответа по схеме"):
        try:
            UpdateUserResponse(**response)
        except ValidationError as e:
            import pytest
            pytest.fail(f"Схема ответа не валидна: {e}")

    with allure.step("Проверка дополнительных условий ответа"):
        assert response["name"] == name
        assert response["job"] == job
