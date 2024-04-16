import pytest
from models import UserRegistration

def test_valid_user_registration():
    user_data = {
        "username": "valid_username",
        "email": "valid_email@example.com",
        "password": "ValidPassword123"
    }
    user_registration = UserRegistration(**user_data)
    assert user_registration.username == user_data["username"]
    assert user_registration.email == user_data["email"]
    assert user_registration.password == user_data["password"]

def test_invalid_username():
    with pytest.raises(ValueError) as exc_info:
        UserRegistration(username="us", email="valid_email@example.com", password="ValidPassword123")
    assert str(exc_info.value) == "Username must be between 3 and 50 characters"

def test_invalid_user_registration():
    user_data = {
        "username": "valid_username",
        "email": "valid_email@example.com",
        "password": "validPassword123"
    }
    user_registration = UserRegistration(**user_data)
    assert user_registration.username == user_data["username"]
    assert user_registration.email == user_data["email"]
    assert user_registration.password == user_data["password"]

# def test_invalid_email():
#     with pytest.raises(ValueError) as exc_info:
#         UserRegistration(username="valid_username", email="invalid_email", password="ValidPassword123")
#     assert str(exc_info.value) == "Invalid email format"

# def test_invalid_password_no_uppercase():
#     with pytest.raises(ValueError) as exc_info:
#         UserRegistration(username="valid_username", email="valid_email@example.com", password="invalidpassword")
#     assert str(exc_info.value) == "Password must contain at least one uppercase letter"

# def test_invalid_password_no_lowercase():
#     with pytest.raises(ValueError) as exc_info:
#         UserRegistration(username="valid_username", email="valid_email@example.com", password="INVALIDPASSWORD")
#     assert str(exc_info.value) == "Password must contain at least one lowercase letter"

# def test_invalid_password_no_digit():
#     with pytest.raises(ValueError) as exc_info:
#         UserRegistration(username="valid_username", email="valid_email@example.com", password="InvalidPassword")
#     assert str(exc_info.value) == "Password must contain at least one digit"

# # Add more test cases as needed
