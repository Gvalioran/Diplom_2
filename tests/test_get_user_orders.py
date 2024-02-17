import allure

import helpers
from data import DataTest


@allure.story('Тесты получения заказов пользователя')
class TestGetUserOrders:

    @allure.title(f'Тест получения списка заказов авторизованным пользователем')
    def test_orders_authorization_user(self, user):
        helpers.creating_order(DataTest.INGREDIENTS_lIST, user["json"]["accessToken"])
        helpers.creating_order(DataTest.INGREDIENTS_lIST, user["json"]["accessToken"])
        response = helpers.get_order_list(user["json"]["accessToken"])
        assert response.status_code == 200
        assert len(response.json()["orders"]) == 2

    @allure.title(f'Тест получения списка заказов  не авторизованным пользователем')
    def test_orders_not_authorization_user(self, user):
        helpers.creating_order(DataTest.INGREDIENTS_lIST)
        helpers.creating_order(DataTest.INGREDIENTS_lIST)
        response = helpers.get_order_list()
        assert response.status_code == 401
        assert response.json()["message"] == DataTest.ERROR_MESSAGE7
