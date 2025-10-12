import json
import os

import allure
import pytest
import requests
from dotenv import load_dotenv

load_dotenv()


class APIClient:
    def __init__(self, base_url: str, default_headers: dict):
        self.base_url = base_url
        self.default_headers = default_headers

    def post(self, endpoint: str, expected_status=201, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = {**self.default_headers, **kwargs.pop('headers', {})}

        # Логирование
        allure.attach(url, "URL", allure.attachment_type.TEXT)
        allure.attach(json.dumps(headers, indent=2), "Headers", allure.attachment_type.JSON)
        if 'json' in kwargs:
            allure.attach(json.dumps(kwargs['json'], indent=2), "Request Body", allure.attachment_type.JSON)

        with allure.step(f"Выполнение POST запроса к {endpoint}"):
            response = requests.post(url, headers=headers, **kwargs)

        allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT)
        allure.attach(response.text, "Response Body", allure.attachment_type.JSON)

        if expected_status is not None:
            with allure.step(f"Проверка статус кода (ожидается {expected_status})"):
                assert response.status_code == expected_status, \
                    f"Ожидался статус {expected_status}, получен {response.status_code}"

        if response.text:
            return response.json()
        return None

    def get(self, endpoint: str, expected_status=200, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = {**self.default_headers, **kwargs.pop('headers', {})}

        allure.attach(url, "URL", allure.attachment_type.TEXT)
        allure.attach(json.dumps(headers, indent=2), "Headers", allure.attachment_type.JSON)

        with allure.step(f"Выполнение GET запроса к {endpoint}"):
            response = requests.get(url, headers=headers, **kwargs)

        allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT)
        allure.attach(response.text, "Response Body", allure.attachment_type.JSON)

        if expected_status is not None:
            with allure.step(f"Проверка статус кода (ожидается {expected_status})"):
                assert response.status_code == expected_status, \
                    f"Ожидался статус {expected_status}, получен {response.status_code}"

        if response.text:
            return response.json()
        return None

    def delete(self, endpoint: str, expected_status=204, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = {**self.default_headers, **kwargs.pop('headers', {})}

        # Логирование
        allure.attach(url, "URL", allure.attachment_type.TEXT)
        allure.attach(json.dumps(headers, indent=2), "Headers", allure.attachment_type.JSON)

        with allure.step(f"Выполнение DELETE запроса к {endpoint}"):
            response = requests.delete(url, headers=headers, **kwargs)

        allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT)
        if response.content:
            allure.attach(response.text, "Response Body", allure.attachment_type.JSON)
        else:
            allure.attach("Empty Response", "Response Body", allure.attachment_type.TEXT)

        if expected_status is not None:
            with allure.step(f"Проверка статус кода (ожидается {expected_status})"):
                assert response.status_code == expected_status, \
                    f"Ожидался статус {expected_status}, получен {response.status_code}"

        if response.text:
            return response.json()
        return None

    def put(self, endpoint: str, expected_status=200, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = {**self.default_headers, **kwargs.pop('headers', {})}

        # Логирование
        allure.attach(url, "URL", allure.attachment_type.TEXT)
        allure.attach(json.dumps(headers, indent=2), "Headers", allure.attachment_type.JSON)
        if 'json' in kwargs:
            allure.attach(json.dumps(kwargs['json'], indent=2), "Request Body", allure.attachment_type.JSON)

        with allure.step(f"Выполнение PUT запроса к {endpoint}"):
            response = requests.put(url, headers=headers, **kwargs)

        allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT)
        allure.attach(response.text, "Response Body", allure.attachment_type.JSON)

        # Проверка статус-кода, если указан
        if expected_status is not None:
            with allure.step(f"Проверка статус кода (ожидается {expected_status})"):
                assert response.status_code == expected_status, \
                    f"Ожидался статус {expected_status}, получен {response.status_code}"

        # Возвращаем JSON если есть тело ответа
        if response.text:
            return response.json()
        return None


@pytest.fixture(scope="session")
def api_client():
    base_url = os.getenv("BASE_API_URL")
    headers = {
        'x-api-key': 'reqres-free-v1',
        'Content-Type': 'application/json'
    }
    return APIClient(base_url, headers)
