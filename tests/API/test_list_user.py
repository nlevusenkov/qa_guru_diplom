import allure
import pytest
from allure_commons.types import Severity
from pydantic import ValidationError

from models.model import UsersResponse


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

    with allure.step("Валидация ответа по схеме"):
        try:
            UsersResponse(**response)
        except ValidationError as e:
            pytest.fail(f"Схема ответа не валидна: {e}")
