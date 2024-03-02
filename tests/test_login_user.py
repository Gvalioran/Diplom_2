import allure

import helpers
from data import DataTest


@allure.story('Тесты на логин пользователя')
class TestLoginUser:
    @allure.title('Тест возможности авторизации пользователя')
    def test_can_login_user(self, user):
        response = helpers.login_user(user["email"], user["password"])
        assert response.status_code == 200

    @allure.title('Тест запрета авторизации пользователя без логина')
    def test_login_user_without_login(self, user):
        response = helpers.login_user("", user["password"])
        assert response.status_code == 401
        assert response.json()["message"] == DataTest.ERROR_MESSAGE3

    @allure.title('Тест запрета авторизации пользователя без пароля')
    def test_login_user_without_password(self, user):
        response = helpers.login_user(user["email"], "")
        assert response.status_code == 401
        assert response.json()["message"] == DataTest.ERROR_MESSAGE3


