import allure
import requests

from helpers import Helpers, Endpoints, Ingredients


class TestsCreateOrder:

    @allure.title('Тест на создание заказа из под авторизованного пользователя')
    def test_create_order_with_authorization_return_success_message_true_and_owner_dict_and_200(self, create_user):

        token = create_user[1].json()['accessToken']
        headers = {'Authorization': token}
        order_response = requests.post(f"{Helpers.BASE_URL}{Endpoints.ORDERS_ENDPOINT}",
                                       headers=headers, data=Ingredients.CORRECT_INGREDIENTS_DATA)

        expected_owner_name = Helpers.NON_UNIQUE_USER_DATA['name']
        actual_owner_name = order_response.json()['order']['owner']['name']

        assert order_response.status_code == 200 and order_response.json()['success'] is True \
               and expected_owner_name == actual_owner_name, f"status code is {order_response.status_code}," \
                                                             f" success order status is " \
                                                             f"{order_response.json()['success']}, " \
                                                             f"actual owner name is {actual_owner_name}"

    @allure.title('Тест на создание заказа без авторизации и с ингредиентами')
    def test_create_order_without_auth_with_ingredients_return_success_message_true_and_200(self):
        order_response = requests.post(f"{Helpers.BASE_URL}{Endpoints.ORDERS_ENDPOINT}",
                                       data=Ingredients.CORRECT_INGREDIENTS_DATA)

        assert order_response.status_code == 200 and order_response.json()['success'] is True, \
            f"status code is {order_response.status_code}, success message is {order_response.json()['success']}"

    @allure.title('Тест на создание заказа без ингредиентов')
    def test_create_order_without_ingredients_return_error_message_and_400(self):
        order_response = requests.post(f"{Helpers.BASE_URL}{Endpoints.ORDERS_ENDPOINT}",
                                       data=Ingredients.INVALID_INGREDIENTS_WITHOUT_DATA)

        assert order_response.status_code == 400 and \
               order_response.json()['message'] == 'Ingredient ids must be provided'

    def test_create_order_with_invalid_hash_ingredients_return_500(self):
        order_response = requests.post(f"{Helpers.BASE_URL}{Endpoints.ORDERS_ENDPOINT}",
                                       data=Ingredients.INVALID_INGREDIENTS_HASH_DATA)

        assert order_response.status_code == 500
