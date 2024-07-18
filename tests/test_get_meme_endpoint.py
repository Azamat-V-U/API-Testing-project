import pytest
import allure
from endpoints.payloads import BasePayloads


payload = BasePayloads


# Positive tests


@allure.feature("GET meme request")
@allure.story("Getting a meme")
@allure.title("Get one meme by id")
@pytest.mark.critical
def test_get_meme_by_valid_id(get_one_meme_endpoint, new_meme_user_1_token):
    get_one_meme_endpoint.get_meme(meme_id=new_meme_user_1_token)
    get_one_meme_endpoint.status_code_verification(status_code=200)
    get_one_meme_endpoint.required_value_data_types_verification()
    get_one_meme_endpoint.id_verification(new_meme_user_1_token)
    get_one_meme_endpoint.required_fields_verification()
    get_one_meme_endpoint.optional_fields_verification()


# Negative tests


@allure.feature("GET meme request")
@allure.story("Getting a meme")
@allure.title("Get meme with invalid meme id")
@pytest.mark.critical
def test_get_meme_by_not_existing_id(get_one_meme_endpoint):
    get_one_meme_endpoint.get_meme(meme_id=0)
    get_one_meme_endpoint.status_code_verification(status_code=404)
    get_one_meme_endpoint.not_found_response_message_verification()


@allure.feature("GET meme request")
@allure.story("Getting a meme")
@allure.title("Get meme with invalid headers")
@pytest.mark.medium
@pytest.mark.parametrize("test_data", payload.invalid_headers)
def test_get_meme_invalid_headers(get_one_meme_endpoint, new_meme_user_1_token, test_data):
    get_one_meme_endpoint.get_meme_with_invalid_headers(meme_id=new_meme_user_1_token, headers=test_data)
    get_one_meme_endpoint.status_code_verification(status_code=401)
    get_one_meme_endpoint.unauthorized_response_message_verification()


# Positive tests


@allure.feature("GET all memes request")
@allure.story("Getting a list of memes")
@allure.title("Get all memes with valid data")
@pytest.mark.critical
def test_get_all_memes(get_all_memes_endpoint):
    get_all_memes_endpoint.get_all_memes()
    get_all_memes_endpoint.status_code_verification(status_code=200)
    get_all_memes_endpoint.json_objects_verification()


# Negative tests


@allure.feature("GET all memes request")
@allure.story("Getting a list of memes")
@allure.title("Get all memes with invalid headers")
@pytest.mark.medium
@pytest.mark.parametrize("invalid_test_data", payload.invalid_headers)
def test_get_all_memes_invalid_headers(get_all_memes_endpoint, invalid_test_data):
    get_all_memes_endpoint.get_all_memes_with_invalid_token(headers=invalid_test_data)
    get_all_memes_endpoint.status_code_verification(status_code=401)
    get_all_memes_endpoint.unauthorized_response_message_verification()
