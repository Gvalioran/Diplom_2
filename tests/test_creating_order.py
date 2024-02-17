import allure

import helpers
from data import DataTest


@allure.story('Тесты создания заказа')
class TestCreatingOrder:

    @allure.title(f'Тест создания заказа c авторизацией и ингредиентами')
    def test_creating_order_authorization(self, user):
        response = helpers.creating_order(DataTest.INGREDIENTS_lIST, user["json"]["accessToken"])
        assert response.status_code == 200
        assert response.json()["order"]["owner"]["name"] == user["name"]

    @allure.title(f'Тест создания заказа без авторизации и ингредиентами')
    def test_creating_order_not_authorization(self):
        response = helpers.creating_order(DataTest.INGREDIENTS_lIST)
        assert response.status_code == 200
        assert 'order' and 'name' in response.json()

    @allure.title(f'Тест создания заказа без ингредиентов')
    def test_creating_not_ingredients(self):
        response = helpers.creating_order("")
        assert response.status_code == 400
        assert response.json()["message"] == DataTest.ERROR_MESSAGE5

    @allure.title(f'Тест создания заказа с неверными хешами ингредиентов')
    def test_creating_order_incorrect_ingredients(self):
        response = helpers.creating_order(DataTest.INCORRECT_INGREDIENTS_lIST)
        assert response.status_code == 400
        assert response.json()["message"] == DataTest.ERROR_MESSAGE6




