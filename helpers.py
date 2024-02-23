import requests
import random
import string

from data import Url


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


def generate_string(length):
    letters = string.ascii_lowercase
    random_string = ''.join(random.choice(letters) for i in range(length))
    return random_string


def login_user(email, password):
    payload = {
        "email": email,
        "password": password,
    }

    response = requests.post(Url.LOGIN, data=payload)
    return response


def delite_user(access_token):
    headers = {'Authorization': access_token}
    response = requests.delete(Url.USER, headers=headers)
    return response.json()


def creating_order(ingredients, access_token=None):
    payload = {
        "ingredients": [ingredients]
    }
    headers = {'Authorization': access_token}
    response = requests.post(Url.ORDER, data=payload, headers=headers)
    return response


def get_order_list(access_token=None):
    headers = {'Authorization': access_token}
    response = requests.get(Url.ORDER, headers=headers)
    return response
