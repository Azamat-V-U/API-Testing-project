import pytest
import allure


invalid_token = [None, "NzL2mMwGayfyQ"]


@allure.feature("GET request")
@allure.story("Getting a token status")
@allure.title("Get valid token status")
@pytest.mark.critical
def test_get_token_status(get_token_status_endpoint):
    get_token_status_endpoint.get_token_status()
    get_token_status_endpoint.status_code_verification(status_code=200)
    get_token_status_endpoint.get_token_status_response_message_ok(get_token_status_endpoint.name)


@allure.feature("GET request")
@allure.story("Getting a token status")
@allure.title("Get invalid token status")
@pytest.mark.critical
@pytest.mark.parametrize("invalid_test_token", invalid_token)
def test_get_token_status_invalid_token(get_token_status_invalid_token, invalid_test_token):
    get_token_status_invalid_token.get_token_status_invalid_token(token=invalid_test_token)
    get_token_status_invalid_token.status_code_verification(status_code=404)
    get_token_status_invalid_token.token_not_found_response_message_verification()


@allure.feature("GET request")
@allure.story("Getting a token status")
@allure.title("Check the response message without a token")
@pytest.mark.medium
def test_get_token_status_empty_token(get_token_status_invalid_token):
    get_token_status_invalid_token.get_token_status_empty_token()
    get_token_status_invalid_token.status_code_verification(status_code=405)
    get_token_status_invalid_token.not_allowed_response_message()


@allure.feature("GET request")
@allure.story("Getting a token status")
@allure.title("Check the response message with a valid token and an incorrect url")
@pytest.mark.medium
def test_get_token_status_invalid_url(get_token_status_endpoint):
    get_token_status_endpoint.get_token_status_invalid_url()
    get_token_status_endpoint.status_code_verification(status_code=404)
    get_token_status_endpoint.not_found_response_message_verification()
