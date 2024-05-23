import json

import allure
import pytest
import requests

from helpers import Helpers, Endpoints


class TestUpdateUserData:

    @allure.title('Тест на изменение данных пользователя с авторизацией')
    @pytest.mark.parametrize('data', [
        Helpers.UPDATED_NAME_FIELD,
        Helpers.UPDATED_EMAIL_FIELD
    ])
    def test_update_user_data_with_authorization_return_success_message_true_and_200(self, data):
        # Блок авторизации: запрос к эндпоинту, сохранение токена, запись токена в хедеры
        auth_response = requests.post(f'{Helpers.BASE_URL}{Endpoints.AUTHORIZATION_ENDPOINT}',
                                      data=Helpers.DATA_FOR_SUCCESS_AUTHORIZATION)

        token = auth_response.json()['accessToken']
        headers = {"Content-Type": "application/json", 'authorization': token}

        # Блок данных для обновления: сериализация данных в JSON
        json_data = json.dumps(data)

        # Запрос на обновление данных
        upd_response = requests.patch(f'{Helpers.BASE_URL}{Endpoints.UPDATE_USER_DATA_ENDPOINT}',
                                      json_data, headers=headers)

        # Блок данных для возвращения пользователя в прежний вид
        post_conditions_data = {
            "email": f"{Helpers.NON_UNIQUE_USER_DATA['email']}",
            "name": f"{Helpers.NON_UNIQUE_USER_DATA['name']}"
        }
        json_post_conditions_data = json.dumps(post_conditions_data)
        requests.patch(f'{Helpers.BASE_URL}{Endpoints.UPDATE_USER_DATA_ENDPOINT}',
                       json_post_conditions_data, headers=headers)

        assert upd_response.status_code == 200 and upd_response.json()['success'] is True

    @allure.title('Тест на изменение данных пользователя без авторизации')
    @pytest.mark.parametrize('data', [
        Helpers.UPDATED_NAME_FIELD,
        Helpers.UPDATED_EMAIL_FIELD
    ])
    def test_update_user_data_without_authorization_return_error_message_and_401(self, data):

        # Блок данных для обновления: сериализация данных в JSON
        json_data = json.dumps(data)

        # Запрос на обновление данных
        upd_response = requests.patch(f'{Helpers.BASE_URL}{Endpoints.UPDATE_USER_DATA_ENDPOINT}', json_data)

        assert upd_response.status_code == 401, upd_response.json()['message'] == 'You should be authorised'
