import pytest
import allure
from endpoints.payloads import PayloadUpdateMeme

payload = PayloadUpdateMeme()


# Positive tests


@allure.feature("UPDATE meme request")
@allure.story("Updating a meme")
@allure.title("Updating meme with valid data")
@pytest.mark.critical
@pytest.mark.smoke
@pytest.mark.parametrize("valid_test_data", payload.valid_data_update_meme)
def test_update_meme_valid_data(update_meme_endpoint, new_meme_user_1_token, valid_test_data):
    payload_copy = valid_test_data.copy()
    payload_copy["id"] = new_meme_user_1_token
    update_meme_endpoint.update_meme(meme_id=new_meme_user_1_token, payload=payload_copy)
    update_meme_endpoint.status_code_verification(status_code=200)
    update_meme_endpoint.payload_parameters_verification(payload_copy)
    update_meme_endpoint.id_verification(meme_id=new_meme_user_1_token)


# Negative tests


@allure.feature("UPDATE meme request")
@allure.story("Updating a meme")
@allure.title("Updating meme with invalid data")
@pytest.mark.critical
@pytest.mark.regression
@pytest.mark.parametrize("invalid_test_data", payload.invalid_data_update_meme)
def test_update_meme_payload_invalid_data(update_meme_endpoint, new_meme_user_1_token, invalid_test_data):
    update_meme_endpoint.update_meme(meme_id=new_meme_user_1_token, payload=invalid_test_data)
    update_meme_endpoint.status_code_verification(status_code=400)
    update_meme_endpoint.invalid_data_response_message_verification()


@allure.feature("UPDATE meme request")
@allure.story("Updating a meme")
@allure.title("Updating meme with invalid meme_id in payload")
@pytest.mark.critical
@pytest.mark.regression
def test_update_meme_meme_id_str(update_meme_endpoint, new_meme_user_1_token):
    payload_copy = payload.valid_data_one_payload.copy()
    payload_copy["id"] = str(new_meme_user_1_token)
    update_meme_endpoint.update_meme(meme_id=new_meme_user_1_token, payload=payload_copy)
    update_meme_endpoint.status_code_verification(status_code=400)
    update_meme_endpoint.invalid_data_response_message_verification()


@allure.feature("UPDATE meme request")
@allure.story("Updating a meme")
@allure.title("Updating meme with invalid payload json")
@pytest.mark.medium
@pytest.mark.regression
def test_update_meme_payload_invalid_json(update_meme_endpoint, new_meme_user_1_token):
    update_meme_endpoint.update_meme(meme_id=new_meme_user_1_token, payload=payload.invalid_json_payload)
    update_meme_endpoint.status_code_verification(status_code=400)
    update_meme_endpoint.invalid_data_response_message_verification()


@allure.feature("UPDATE meme request")
@allure.story("Updating a meme")
@allure.title("Updating meme with empty payload")
@pytest.mark.critical
@pytest.mark.extended
def test_update_meme_payload_empty(update_meme_endpoint, new_meme_user_1_token):
    update_meme_endpoint.update_meme_empty_payload_data(new_meme_user_1_token)
    update_meme_endpoint.status_code_verification(status_code=400)
    update_meme_endpoint.invalid_data_response_message_verification()


@allure.feature("UPDATE meme request")
@allure.story("Updating a meme")
@allure.title("Updating meme with incorrect meme_id in url")
@pytest.mark.medium
@pytest.mark.extended
def test_update_meme_url_meme_id_none(update_meme_endpoint, new_meme_user_1_token):
    payload_copy = payload.valid_data_one_payload.copy()
    payload_copy["id"] = new_meme_user_1_token
    update_meme_endpoint.update_meme(meme_id=None, payload=payload_copy)
    update_meme_endpoint.status_code_verification(status_code=404)
    update_meme_endpoint.not_found_response_message_verification()


@allure.feature("UPDATE meme request")
@allure.story("Updating a meme")
@allure.title("Updating meme with empty meme_id in url")
@pytest.mark.extended
def test_update_meme_url_meme_id_empty(update_meme_endpoint, new_meme_user_1_token):
    payload_copy = payload.valid_data_one_payload.copy()
    payload_copy["id"] = new_meme_user_1_token
    update_meme_endpoint.update_meme_url_empty_meme_id(payload=payload_copy)
    update_meme_endpoint.status_code_verification(status_code=405)
    update_meme_endpoint.not_allowed_response_message_verification()


@allure.feature("UPDATE meme request")
@allure.story("Updating a meme")
@allure.title("Updating meme with invalid headers")
@pytest.mark.critical
@pytest.mark.extended
@pytest.mark.parametrize("invalid_test_headers", payload.invalid_headers)
def test_update_meme_invalid_headers(update_meme_endpoint, new_meme_user_1_token, invalid_test_headers):
    update_meme_endpoint.update_meme_invalid_headers(meme_id=new_meme_user_1_token, headers=invalid_test_headers)
    update_meme_endpoint.status_code_verification(status_code=401)
    update_meme_endpoint.unauthorized_response_message_verification()
