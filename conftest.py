import pytest

import helpers


@pytest.fixture
def user():
    user = helpers.register_new_user_and_return_test_data()
    yield user
    helpers.delite_user(user["json"]["accessToken"])


@pytest.fixture
def del_user():
    user = {}
    yield user
    helpers.delite_user(user["json"]["accessToken"])
