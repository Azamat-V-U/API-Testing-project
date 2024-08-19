import pytest
import allure
from endpoints.payloads import PayloadCreateMeme


payload = PayloadCreateMeme

# Positive tests


@allure.feature("Post meme request")
@allure.story("Meme creation")
@allure.title("Create meme with valid data")
@pytest.mark.critical
@pytest.mark.parametrize("valid_test_data", payload.valid_data_create_meme)
def test_create_meme_valid_data(create_meme_endpoint, delete_meme_endpoint, valid_test_data):
    create_meme_endpoint.create_meme(payload=valid_test_data)
    create_meme_endpoint.status_code_verification(status_code=200)
    create_meme_endpoint.id_verification(meme_id=create_meme_endpoint.meme_id)
    create_meme_endpoint.payload_parameters_verification(payload=valid_test_data)
    delete_meme_endpoint.delete_one_meme(meme_id=create_meme_endpoint.meme_id)


# Negative tests


@allure.feature("POST meme request")
@allure.story("Meme creation")
@allure.title("Create meme with invalid data")
@pytest.mark.critical
@pytest.mark.parametrize("invalid_test_data", payload.invalid_data_create_meme)
def test_create_meme_invalid_data(create_meme_endpoint, invalid_test_data):
    create_meme_endpoint.create_meme(payload=invalid_test_data)
    create_meme_endpoint.status_code_verification(status_code=400)
    create_meme_endpoint.invalid_data_response_message_verification()


@allure.feature("POST meme request")
@allure.story("Meme creation")
@allure.title("Create meme with the invalid json object")
@pytest.mark.medium
def test_create_meme_invalid_json(create_meme_endpoint):
    create_meme_endpoint.create_meme(payload=payload.invalid_json_payload)
    create_meme_endpoint.status_code_verification(status_code=400)
    create_meme_endpoint.invalid_data_response_message_verification()


@allure.feature("POST meme request")
@allure.story("Meme creation")
@allure.title("Create meme with the invalid headers")
@pytest.mark.critical
@pytest.mark.parametrize("invalid_test_headers", payload.invalid_headers)
def test_create_meme_invalid_headers(create_meme_endpoint, invalid_test_headers):
    create_meme_endpoint.create_meme_invalid_headers(
        payload=payload.valid_data_create_meme, headers=invalid_test_headers
    )
    create_meme_endpoint.status_code_verification(status_code=401)
    create_meme_endpoint.unauthorized_response_message_verification()
