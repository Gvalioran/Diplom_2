class Url:
    BASE_URL = "https://stellarburgers.nomoreparties.site/api"
    CREATE_USER = BASE_URL + "/auth/register"
    LOGIN = BASE_URL + "/auth/login"
    USER = BASE_URL + "/auth/user"
    ORDER = BASE_URL + "/orders"


class DataTest:
    ERROR_MESSAGE1 = "User already exists"
    ERROR_MESSAGE2 = "Email, password and name are required fields"
    ERROR_MESSAGE3 = "email or password are incorrect"
    ERROR_MESSAGE4 = "You should be authorised"
    ERROR_MESSAGE5 = "Ingredient ids must be provided"
    ERROR_MESSAGE6 = "One or more ids provided are incorrect"
    ERROR_MESSAGE7 = "You should be authorised"
    INGREDIENTS_lIST = "61c0c5a71d1f82001bdaaa6d", "61c0c5a71d1f82001bdaaa6c", "61c0c5a71d1f82001bdaaa71"
    INCORRECT_INGREDIENTS_lIST = "61c0c6a71d1f82001bdaaa6d", "61c0c5a80d1f82001bdaaa6c", "61c0c5a71d1f82551bdaaa71"

