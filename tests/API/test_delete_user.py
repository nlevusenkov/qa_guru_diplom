import allure
from allure_commons.types import Severity


@allure.epic("API Tests")
@allure.tag("API", "DELETE")
@allure.severity(Severity.BLOCKER)
@allure.label("owner", "nlevusenkov")
@allure.feature('Tests reqres.in')
@allure.story("Delete User")
@allure.title("Удаление пользователя через DELETE запрос")
@allure.description("Тест проверяет корректное удаление пользователя и валидацию пустого ответа")
def test_delete_user_status_code(api_client):
    with allure.step("Отправка delete запроса на удаление пользователя"):
        response = api_client.delete('/users/2')

    with allure.step("Проверка пустого ответа"):
        assert response is None, "Ожидался пустой ответ"
