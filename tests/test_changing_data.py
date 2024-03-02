import allure
import pytest
import requests

import helpers
from data import DataTest, Url


@allure.story('Тесты на изменение данных пользователя')
class TestChangingData:

    @allure.title(f'Тест возможности смены данных пользователя')
    @pytest.mark.parametrize("test_data", ["email", "name"])
    def test_changing_data_user(self, user, test_data):
        payload = {test_data: helpers.generate_string(10)}
        response = requests.patch(Url.USER, data=payload, headers={'Authorization': f'{user["json"]["accessToken"]}'})
        assert response.status_code == 200
        assert response.json()["user"][test_data] == payload[test_data]

    @allure.title(f'Тест запрета возможности смены данных пользователя без авторизации')
    @pytest.mark.parametrize("test_data", ["email", "name"])
    def test_error_changing_data_user_not_authorization(self, user, test_data):
        payload = {test_data: helpers.generate_string(10)}
        response = requests.patch(Url.USER, data=payload)
        assert response.status_code == 401
        assert response.json()["message"] == DataTest.ERROR_MESSAGE4
