import json
import os
from pathlib import Path

import allure
import pytest
import requests
from allure_commons.types import Severity
from dotenv import load_dotenv
from jsonschema import validate
from pydantic import ValidationError

from models.model import UserResponse

payload = {
    "name": "morpheus",
    "job": "leader"
}


@allure.epic("API Tests")
@allure.tag("API", "POST")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.title("Создание нового пользователя")
@allure.description("Тест проверяет создание пользователя через POST запрос с валидацией JSON схемы")
def test_create_user(api_client):
    with allure.step("Отправка POST запроса на создание пользователя"):
        response = api_client.post('/users', json=payload)

    with allure.step("Проверка данных ответа"):
        assert response['name'] == "morpheus"
        assert response['job'] == "leader"

    with allure.step("Валидация ответа по схеме"):
        try:
            UserResponse(**response)
        except ValidationError as e:
            pytest.fail(f"Схема ответа не валидна: {e}")
