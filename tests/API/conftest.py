# conftest.py
import os
import pytest
import requests
import allure
import json
from dotenv import load_dotenv

load_dotenv()


class APIClient:
    def __init__(self, base_url: str, default_headers: dict):
        self.base_url = base_url
        self.default_headers = default_headers

    def post(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = {**self.default_headers, **kwargs.pop('headers', {})}

        # Логирование
        allure.attach(url, "URL", allure.attachment_type.TEXT)
        allure.attach(json.dumps(headers, indent=2), "Headers", allure.attachment_type.JSON)
        if 'json' in kwargs:
            allure.attach(json.dumps(kwargs['json'], indent=2), "Request Body", allure.attachment_type.JSON)

        response = requests.post(url, headers=headers, **kwargs)

        allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT)
        allure.attach(response.text, "Response Body", allure.attachment_type.JSON)

        return response

    def get(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = {**self.default_headers, **kwargs.pop('headers', {})}

        allure.attach(url, "URL", allure.attachment_type.TEXT)
        allure.attach(json.dumps(headers, indent=2), "Headers", allure.attachment_type.JSON)

        response = requests.get(url, headers=headers, **kwargs)

        allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT)
        allure.attach(response.text, "Response Body", allure.attachment_type.JSON)

        return response

    def delete(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = {**self.default_headers, **kwargs.pop('headers', {})}

        # Логирование
        allure.attach(url, "URL", allure.attachment_type.TEXT)
        allure.attach(json.dumps(headers, indent=2), "Headers", allure.attachment_type.JSON)

        response = requests.delete(url, headers=headers, **kwargs)

        allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT)
        if response.content:
            allure.attach(response.text, "Response Body", allure.attachment_type.JSON)
        else:
            allure.attach("Empty Response", "Response Body", allure.attachment_type.TEXT)

        return response

    def put(self, endpoint: str, **kwargs):
        url = f"{self.base_url}{endpoint}"
        headers = {**self.default_headers, **kwargs.pop('headers', {})}

        # Логирование
        allure.attach(url, "URL", allure.attachment_type.TEXT)
        allure.attach(json.dumps(headers, indent=2), "Headers", allure.attachment_type.JSON)
        if 'json' in kwargs:
            allure.attach(json.dumps(kwargs['json'], indent=2), "Request Body", allure.attachment_type.JSON)

        response = requests.put(url, headers=headers, **kwargs)

        allure.attach(str(response.status_code), "Status Code", allure.attachment_type.TEXT)
        allure.attach(response.text, "Response Body", allure.attachment_type.JSON)

        return response


@pytest.fixture(scope="session")
def api_client():
    """API клиент с базовым URL и headers"""
    base_url = os.getenv("BASE_API_URL")
    headers = {
        'x-api-key': 'reqres-free-v1',
        'Content-Type': 'application/json'
    }
    return APIClient(base_url, headers)