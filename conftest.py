import pytest

import helpers


@pytest.fixture
def user():
    user = helpers.register_new_user_and_return_test_data()
    yield user
    helpers.delete_user(user["json"]["accessToken"])


@pytest.fixture
def del_user():
    data = {}
    yield data
    helpers.delete_user(data["accessToken"])
