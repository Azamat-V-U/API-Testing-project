import allure
import pytest
from endpoints.payloads import BasePayloads

payload = BasePayloads


# Positive tests


@allure.feature("DELETE meme request")
@allure.story("Deleting a meme")
@allure.title("Delete a meme with valid data")
@pytest.mark.critical
def test_delete_meme_valid_data(new_meme_user_1_token_for_delete_method, delete_meme_endpoint):
    delete_meme_endpoint.delete_one_meme(meme_id=new_meme_user_1_token_for_delete_method)
    delete_meme_endpoint.status_code_verification(status_code=200)
    delete_meme_endpoint.delete_response_message_ok()


# Negative tests


@allure.feature("DELETE meme request")
@allure.story("Deleting a meme")
@allure.title("Delete a meme with other user token")
@pytest.mark.critical
def test_delete_meme_with_other_user_token(new_meme_user_2_token, delete_meme_endpoint):
    delete_meme_endpoint.delete_one_meme(meme_id=new_meme_user_2_token)
    delete_meme_endpoint.status_code_verification(status_code=403)
    delete_meme_endpoint.forbidden_response_message_verification()


@allure.feature("DELETE meme request")
@allure.story("Deleting a meme")
@allure.title("Delete a meme with a non-existing meme_id")
@pytest.mark.medium
def test_delete_meme_url_meme_id_none(delete_meme_endpoint):
    delete_meme_endpoint.delete_one_meme(meme_id=None)
    delete_meme_endpoint.status_code_verification(status_code=404)
    delete_meme_endpoint.not_found_response_message_verification()


@allure.feature("DELETE meme request")
@allure.story("Deleting a meme")
@allure.title("Delete a meme without meme_id in the url")
@pytest.mark.medium
def test_delete_meme_url_empty_meme_id(delete_meme_endpoint):
    delete_meme_endpoint.delete_meme_url_empty_meme_id()
    delete_meme_endpoint.status_code_verification(status_code=405)
    delete_meme_endpoint.not_allowed_response_message_verification()


@allure.feature("DELETE meme request")
@allure.story("Deleting a meme")
@allure.title("Delete a meme with invalid headers")
@pytest.mark.critical
@pytest.mark.parametrize("invalid_test_headers", payload.invalid_headers)
def test_delete_meme_invalid_headers(delete_meme_endpoint, new_meme_user_1_token, invalid_test_headers):
    delete_meme_endpoint.delete_meme_invalid_headers(meme_id=new_meme_user_1_token, headers=invalid_test_headers)
    delete_meme_endpoint.status_code_verification(status_code=401)
    delete_meme_endpoint.unauthorized_response_message_verification()
