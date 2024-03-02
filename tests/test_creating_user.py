import pytest
import requests
import allure

import helpers
from data import Url, DataTest


@allure.story('Тесты создания пользователя')
class TestCreatingUser:

    @allure.title('Тест успешного создания пользователя')
    def test_can_create_user(self, del_user):
        payload = {
            "email": f"{helpers.generate_string(10)}@yandex.ru",
            "password": helpers.generate_string(10),
            "name": helpers.generate_string(10)
        }
        response = requests.post(Url.CREATE_USER, data=payload)
        del_user.update(response.json())
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

    @pytest.mark.parametrize("test_email, test_password, test_name",
                             [["", helpers.generate_string(10), helpers.generate_string(10)],
                              [f"{helpers.generate_string(10)}@yandex.ru", "", helpers.generate_string(10)],
                              [f"{helpers.generate_string(10)}@yandex.ru", helpers.generate_string(10), ""]])
    @allure.title('Тест запрета создания пользователя без обязательных полей')
    def test_creating_user_without_email(self, test_email, test_password, test_name):
        payload = {
            "email": test_email,
            "password": test_password,
            "name": test_name
        }
        response = requests.post(Url.CREATE_USER, data=payload)
        assert response.status_code == 403
        assert response.json()["message"] == DataTest.ERROR_MESSAGE2
