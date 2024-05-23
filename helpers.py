from random import randint


class Helpers:

    BASE_URL = 'https://stellarburgers.nomoreparties.site/api'  # Ссылка на тестируемое приложение
    # Данные для регистрации уникального пользователя
    UNIQUE_USER_DATA = {
        "email": f"unique_user{randint(1, 1000)}@domain.com",
        "password": "123456",
        "name": "Testik"
    }
    # Данные зарегистрированного пользователя
    NON_UNIQUE_USER_DATA = {
        "email": "non_unique_user@yandex.ru",
        "password": "password",
        "name": "Testik"
    }
    # Данные без обязательного поля – пароля
    DATA_WITHOUT_PASSWORD_FOR_REGISTER_ENDPOINT = {
        "email": f"unique_user{randint(1, 1000)}@domain.com",
        "name": "Testik"
    }
    # Данные без обязательного поля – имени
    DATA_WITHOUT_NAME_FOR_REGISTER_ENDPOINT = {
        "email": f"unique_user{randint(1, 1000)}@domain.com",
        "password": "123456"
    }
    # Данные без обязательного поля – имейла
    DATA_WITHOUT_EMAIL_FOR_REGISTER_ENDPOINT = {
        "password": "123456",
        "name": "Testik"
    }
    # Данные для успешной авторизации пользователя
    DATA_FOR_SUCCESS_AUTHORIZATION = {
        "email": f"{NON_UNIQUE_USER_DATA['email']}",
        "password": f"{NON_UNIQUE_USER_DATA['password']}"
    }
    # Данные для авторизации с невалидным паролем
    DATA_FOR_AUTHORIZATION_WITH_INVALID_PASSWORD = {
        "email": f"{NON_UNIQUE_USER_DATA['email']}",
        "password": "invalid_password"
    }
    # Данные для авторизации с уникальным, незарегистрированным имейлом
    DATA_FOR_AUTHORIZATION_WITH_INVALID_EMAIL = {
        "email": f"{UNIQUE_USER_DATA['email']}",
        "password": f"{NON_UNIQUE_USER_DATA['password']}"
    }
    UPDATED_NAME_FIELD = {
        "name": "Updated Testik"
    }
    UPDATED_EMAIL_FIELD = {
        "email": "updated_email@domain.com"
    }


class Endpoints:

    REGISTER_ENDPOINT = '/auth/register'  # Эндпоинт для регистрации пользователя
    AUTHORIZATION_ENDPOINT = '/auth/login'  # Эндпоинт для авторизации пользователя
    DELETE_ENDPOINT = '/auth/user'  # Эндпоинт для удаления пользователя, вызывать с методом DELETE
    UPDATE_USER_DATA_ENDPOINT = '/auth/user'  # Эндпоинт для удаления пользователя, вызывать с методом PATCH
    ORDERS_ENDPOINT = '/orders'  # Эндпоинт для работы с заказами: для создания нового заказа вызывать с методом POST,
    # для получения заказов конкрнетного пользователя вызывать с методом GET и передавать в заголовках Bearer токен


class Ingredients:

    #  Данные для корректного заказа
    CORRECT_INGREDIENTS_DATA = {
        "ingredients": ["61c0c5a71d1f82001bdaaa7a", "61c0c5a71d1f82001bdaaa6f", "61c0c5a71d1f82001bdaaa6d"]
    }

    #  Данные для заказа с невалидными хешами ингредиентов
    INVALID_INGREDIENTS_HASH_DATA = {
        "ingredients": ["61c0c5a71d1f82001bdaaa", "61c0c5a71d1f82001bdaaa", "61c0c5a71d1f82001bdaa"]
    }

    #  Невалидные данные для заказа без хешей ингредиентов
    INVALID_INGREDIENTS_WITHOUT_DATA = {
        "ingredients": []
    }
