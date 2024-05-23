import allure
import pytest
import requests

from helpers import Helpers, Endpoints


class TestRegisterEndpoint:

    @allure.title('Тест на создание уникального пользователя')
    def test_create_unique_user_return_success_true_and_200(self):

        payload = Helpers.UNIQUE_USER_DATA  # Создаем уникальный набор данных для регистрации пользователя

        reg_response = requests.post(f"{Helpers.BASE_URL}{Endpoints.REGISTER_ENDPOINT}", data=payload)  # Регистрируем

        assert reg_response.status_code == 200 and reg_response.json()["success"] is True, \
            f"status code is {reg_response.status_code}, response text is {reg_response.json()}"

    @allure.title('Тест на создание пользователя, который уже зарегестрирован')
    def test_create_non_unique_user_return_error_message_and_403(self):
        response = requests.post(f'{Helpers.BASE_URL}{Endpoints.REGISTER_ENDPOINT}',
                                 data=Helpers.NON_UNIQUE_USER_DATA)

        assert response.status_code == 403 and response.json()["message"] == "User already exists", \
            f"status code is {response.status_code}, response text is {response.json()}"

    @allure.title('Тест на создание пользователя без одного из обязательных полей')
    @pytest.mark.parametrize('data', [
        Helpers.DATA_WITHOUT_PASSWORD_FOR_REGISTER_ENDPOINT,
        Helpers.DATA_WITHOUT_NAME_FOR_REGISTER_ENDPOINT,
        Helpers.DATA_WITHOUT_EMAIL_FOR_REGISTER_ENDPOINT
    ])
    def test_create_user_without_one_required_field_return_error_message_and_403(self, data):
        response = requests.post(f'{Helpers.BASE_URL}{Endpoints.REGISTER_ENDPOINT}', data=data)

        required_message = "Email, password and name are required fields"

        assert response.status_code == 403 and response.json()["message"] == required_message, \
            f"status code is {response.status_code}, response text is {response.json()}"
