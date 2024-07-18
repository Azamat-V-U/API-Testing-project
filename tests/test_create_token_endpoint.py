import pytest
import allure
from endpoints.payloads import PayloadCreateToken


payload = PayloadCreateToken


@allure.feature("Post token request")
@allure.story("User authorization")
@allure.title("Create token with valid data")
@pytest.mark.critical
@pytest.mark.parametrize("valid_test_data", payload.valid_data_create_token)
def test_authorization_with_valid_data(create_token_endpoint, valid_test_data):
    create_token_endpoint.create_token_valid_data(payload=valid_test_data)
    create_token_endpoint.status_code_verification(status_code=200)
    create_token_endpoint.response_json_object_verification(valid_test_data)


# Negative test cases


@allure.feature("POST token request")
@allure.story("User authorization")
@allure.title("Create token with invalid data")
@pytest.mark.critical
@pytest.mark.parametrize("invalid_test_data", payload.invalid_data_create_token)
def test_authorization_invalid_data(create_token_endpoint, invalid_test_data):
    create_token_endpoint.create_token_invalid_data(payload=invalid_test_data)
    create_token_endpoint.status_code_verification(status_code=400)
    create_token_endpoint.invalid_data_response_message_verification()


@allure.feature("POST token request")
@allure.story("User authorization")
@allure.title("Create token with invalid json object")
@pytest.mark.medium
def test_authorization_with_invalid_json(create_token_endpoint):
    create_token_endpoint.create_token_invalid_data(payload=payload.invalid_json_payload)
    create_token_endpoint.status_code_verification(status_code=400)
    create_token_endpoint.invalid_json_response_message_verification()
