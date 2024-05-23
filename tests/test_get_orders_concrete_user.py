import allure
import requests

from helpers import Helpers, Endpoints


class TestGetOrdersConcreteUser:

    @allure.title('Тест на получение заказов конкретного пользователя с авторизацией')
    def test_get_orders_concrete_user_with_auth_return_order_list_and_200(self, create_user):

        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        get_orders_response = requests.get(f"{Helpers.BASE_URL}{Endpoints.ORDERS_ENDPOINT}", headers=headers)

        assert get_orders_response.status_code == 200 and type(get_orders_response.json()['orders']) is list, \
            f"status code is {get_orders_response.status_code}, response json object is {get_orders_response.json()}"

    @allure.title('Тест на получение заказов конкретного пользователя без авторизации')
    def test_get_orders_concrete_user_without_auth_return_error_message_and_401(self):
        get_orders_response = requests.get(f"{Helpers.BASE_URL}{Endpoints.ORDERS_ENDPOINT}")

        assert get_orders_response.status_code == 401 and get_orders_response.json()['message'] == \
               'You should be authorised', f'status code is {get_orders_response.status_code}, error message is ' \
                                           f'{get_orders_response.json()["message"]} '
