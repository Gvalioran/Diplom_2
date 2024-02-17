import requests
import allure

import helpers
from data import Url, DataTest


@allure.story('Тесты создания пользователя')
class TestCreatingUser:

    @allure.title('Тест успешного создания пользователя')
    def test_can_create_user(self):
        payload = {
            "email": f"{helpers.generate_random_string(10)}@yandex.ru",
            "password": helpers.generate_random_string(10),
            "name": helpers.generate_random_string(10)
        }
        response = requests.post(Url.CREATE_USER, data=payload)
        assert response.status_code == 200

    @allure.title('Тест запрета создания одинаковых пользователей')
    def test_cannot_create_two_identical_user(self, user):
        payload = {
            "email": user["email"],
            "password": user["password"],
            "name": user["name"]
        }
        response = requests.post(Url.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.json()["message"] == DataTest.ERROR_MESSAGE1

    @allure.title('Тест запрета создания пользователя без заполнения почты')
    def test_creating_user_without_email(self):
        payload = {
            "email": "",
            "password": helpers.generate_random_string(10),
            "name": helpers.generate_random_string(10)
        }
        response = requests.post(Url.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.json()["message"] == DataTest.ERROR_MESSAGE2

    @allure.title('Тест запрета создания пользователя без заполнения пароля')
    def test_creating_user_without_password(self):
        payload = {
            "email": f"{helpers.generate_random_string(10)}@yandex.ru",
            "password": "",
            "name": helpers.generate_random_string(10)
        }
        response = requests.post(Url.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.json()["message"] == DataTest.ERROR_MESSAGE2

    @allure.title('Тест запрета создания пользователя без заполнения имени')
    def test_creating_user_without_name(self):
        payload = {
            "email": f"{helpers.generate_random_string(10)}@yandex.ru",
            "password": helpers.generate_random_string(10),
            "name": ""
        }
        response = requests.post(Url.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.json()["message"] == DataTest.ERROR_MESSAGE2
