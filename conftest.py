import allure
import pytest
import requests

from helpers import Helpers, Endpoints


@allure.step('Создание тестового пользователя с последующим удалением')
@pytest.fixture
def create_user():
    payload = Helpers.UNIQUE_USER_DATA
    response = requests.post(f"{Helpers.BASE_URL}{Endpoints.REGISTER_ENDPOINT}", data=payload)
    yield payload, response
    token = response.json()["accessToken"]
    requests.delete(f"{Helpers.BASE_URL}{Endpoints.DELETE_ENDPOINT}", headers={"Authorization": token})
