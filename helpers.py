import allure
import requests
import random
import string

from data import Url


@allure.step(f'Регистрация пользователя и получение тестовых данных')
def register_new_user_and_return_test_data():
    name = generate_string(10)
    password = generate_string(10)
    email = f"{name}@yandex.ru"

    payload = {
        "email": email,
        "password": password,
        "name": name
    }

    response = requests.post(Url.CREATE_USER, data=payload)

    test_data = {
        "email": email,
        "name": name,
        "password": password,
        "json": response.json()
    }

    return test_data


@allure.step(f'Генерация случайной строки')
def generate_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


@allure.step(f'Вход в аккаунт')
def login_user(email, password):
    payload = {
        "email": email,
        "password": password,
    }

    response = requests.post(Url.LOGIN, data=payload)
    return response


@allure.step(f'Удаление пользователя')
def delete_user(access_token):
    headers = {'Authorization': access_token}
    requests.delete(Url.USER, headers=headers)


@allure.step(f'Создать заказ')
def creating_order(ingredients, access_token=None):
    payload = {
        "ingredients": [ingredients]
    }
    headers = {'Authorization': access_token}
    response = requests.post(Url.ORDER, data=payload, headers=headers)
    return response


@allure.step(f'Получение списка заказов')
def get_order_list(access_token=None):
    headers = {'Authorization': access_token}
    response = requests.get(Url.ORDER, headers=headers)
    return response
