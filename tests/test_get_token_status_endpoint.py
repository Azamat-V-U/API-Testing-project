import pytest
import allure
from endpoints.payloads import BasePayloads


payload = BasePayloads


@allure.feature("GET token status request")
@allure.story("Getting a token status")
@allure.title("Get valid token status")
@pytest.mark.critical
@pytest.mark.smoke
def test_get_token_status_valid_data(get_token_status_endpoint):
    get_token_status_endpoint.get_token_status()
    get_token_status_endpoint.status_code_verification(status_code=200)
    get_token_status_endpoint.token_found_response_message_verification(get_token_status_endpoint.name)


@allure.feature("GET token status request")
@allure.story("Getting a token status")
@allure.title("Get invalid token status")
@pytest.mark.critical
@pytest.mark.smoke
@pytest.mark.parametrize("invalid_test_token", payload.invalid_token)
def test_get_token_status_invalid_token(get_token_status_invalid_token, invalid_test_token):
    get_token_status_invalid_token.get_token_status_invalid_token(token=invalid_test_token)
    get_token_status_invalid_token.status_code_verification(status_code=404)
    get_token_status_invalid_token.token_not_found_response_message_verification()


@allure.feature("GET token status request")
@allure.story("Getting a token status")
@allure.title("Checking the response message without a token")
@pytest.mark.medium
@pytest.mark.regression
def test_get_token_status_empty_token(get_token_status_invalid_token):
    get_token_status_invalid_token.get_token_status_empty_token()
    get_token_status_invalid_token.status_code_verification(status_code=405)
    get_token_status_invalid_token.not_allowed_response_message_verification()


@allure.feature("GET token status request")
@allure.story("Getting a token status")
@allure.title("Checking the response message with a valid token and an incorrect url")
@pytest.mark.medium
@pytest.mark.extended
def test_get_token_status_invalid_url(get_token_status_endpoint):
    get_token_status_endpoint.get_token_status_invalid_url()
    get_token_status_endpoint.status_code_verification(status_code=404)
    get_token_status_endpoint.not_found_response_message_verification()
