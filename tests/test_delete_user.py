import allure
import requests

from helpers import Helpers, Endpoints


class TestDeleteUser:

    @allure.title('Тест на удаление пользователя')
    def test_delete_user_return_202(self):
        reg_response = requests.post(f'{Helpers.BASE_URL}{Endpoints.REGISTER_ENDPOINT}',
                                     data=Helpers.UNIQUE_USER_DATA)
        token = reg_response.json()['accessToken']
        headers = {"Content-Type": "application/json", 'authorization': token}
        del_response = requests.delete(f'{Helpers.BASE_URL}{Endpoints.DELETE_ENDPOINT}', headers=headers)
        assert del_response.status_code == 202 and del_response.json()["message"] == "User successfully removed", \
            f"status code is {del_response.status_code}, response text is {del_response.json()}"
