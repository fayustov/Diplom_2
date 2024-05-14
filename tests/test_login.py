import allure
import pytest
import requests

from helpers import Helpers, Endpoints


class TestLogin:

    @allure.title('Тест на логин под существующим пользователем')
    def test_login_under_existing_user_return_succes_true_and_200(self):

        response = requests.post(f'{Helpers.BASE_URL}{Endpoints.AUTHORIZATION_ENDPOINT}',
                                 data=Helpers.DATA_FOR_SUCCESS_AUTHORIZATION)

        assert response.status_code == 200 and response.json()["success"] is True, \
            f"status code is {response.status_code}, response text is {response.json()}"

    @pytest.mark.parametrize('data', [
        Helpers.DATA_FOR_AUTHORIZATION_WITH_INVALID_PASSWORD,
        Helpers.DATA_FOR_AUTHORIZATION_WITH_INVALID_EMAIL
    ])
    def test_login_with_invalid_login_or_password_return_error_message_and_401(self, data):

        response = requests.post(f'{Helpers.BASE_URL}{Endpoints.AUTHORIZATION_ENDPOINT}', data=data)

        assert response.status_code == 401 and response.json()["message"] == "email or password are incorrect", \
            f"status code is {response.status_code}, response text is {response.json()}"
