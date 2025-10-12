import allure
from allure_commons.types import Severity


@allure.epic("API Tests")
@allure.tag("API", "put", "users")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.story("put User invalid unauthorize")
def test_single_user_invalid_id_unauthorized(api_client):
    payload = {
        "name": "morpheus",
        "job": "zion resident"
    }

    with allure.step("Отправка put запроса на авторизацию пользователя"):
        response = api_client.post('/login', json=payload, headers={}, expected_status=400)

    with allure.step("Проверка json схемы"):
        assert 'error' in response


@allure.epic("API Tests")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature("User Management")
@allure.story("get User not found")
def test_users_not_found(api_client):
    with allure.step("Отправка GET запроса для несуществующего пользователя"):
        response = api_client.get('/users/23', expected_status=404)

    with allure.step("Проверка пустого ответа"):
        assert response == {} or response is None
