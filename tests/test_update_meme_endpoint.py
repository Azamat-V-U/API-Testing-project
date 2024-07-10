import pytest
import allure


valid_meme_payload = [
    {
        "id": None,
        "text": "Sponge Bob",
        "url": "www.example.com",
        "tags": ["Sponge Bob", "Cartoon", "some tags"],
        "info": {"colors": ["yellow", "brown", "red"]}
    },
    {
        "id": None,
        "text": "Mister Bin",
        "url": "www.example.com",
        "tags": ["Mister Bin", "Cartoon", "some tag"],
        "info": {"colors": ["yellow", "brown", "red", "black"]}
    },
    {
        "id": None,
        "text": "Simpsons",
        "url": "www.example.com",
        "tags": ["Simpsons", "Cartoon", "some tag", "some tag"],
        "info": {"colors": ["yellow", "brown", "black", "green", "red"]}
    }
]

invalid_meme_payload = [
    {
        "id": None,
        "text": "Mister Bin",
        "url": "www.example.com",
        "tags": ["Mister Bin", "Cartoon"],
        "info": {"colors": ["yellow", "brown"]}
    },
    {
        "text": "Sponge Bob",
        "url": "www.example.com",
        "tags": ["Sponge Bob", "Cartoon"],
        "info": {"colors": ["yellow", "brown"]}
    },
    {
        "id": None,
        "text": "",
        "url": "",
        "tags": [],
        "info": {}
    },
    {}
]
payload = {
    "id": None,
    "info": {"colors": ["yellow", "brown", "green"]},
    "tags": ["Sponge Bob", "Cartoon"],
    "text": "Sponge Bob",
    "url": "www.example.com"
}

payload_invalid_json = '{"name": "John"'
invalid_headers = [
    {"Authorization": "92NzL2mMwGayfyQ"},
    {"Authorization": ""},
    {}
]

# Positive tests


@allure.feature("UPDATE request")
@allure.story("Updating a meme")
@allure.title("Update meme with valid data")
@pytest.mark.critical
@pytest.mark.parametrize("valid_test_data", valid_meme_payload)
def test_update_meme_valid_data(update_meme_endpoint, new_meme_id_int, valid_test_data):
    payload_copy = valid_test_data.copy()
    payload_copy["id"] = new_meme_id_int
    update_meme_endpoint.update_meme(meme_id=new_meme_id_int, payload=payload_copy)
    update_meme_endpoint.status_code_verification(status_code=200)
    update_meme_endpoint.payload_parameters_verification(payload_copy)
    update_meme_endpoint.id_verification(meme_id=new_meme_id_int)


# Negative tests

@allure.feature("UPDATE request")
@allure.story("Updating a meme")
@allure.title("Update meme with invalid data")
@pytest.mark.critical
@pytest.mark.parametrize("invalid_test_data", invalid_meme_payload)
def test_update_meme_payload_invalid_data(update_meme_endpoint, new_meme_id_int, invalid_test_data):
    update_meme_endpoint.update_meme(meme_id=new_meme_id_int, payload=invalid_test_data)
    update_meme_endpoint.status_code_verification(status_code=400)
    update_meme_endpoint.invalid_data_response_message()


@allure.feature("UPDATE request")
@allure.story("Updating a meme")
@allure.title("Update meme with invalid meme_id")
@pytest.mark.critical
def test_update_meme_meme_id_str(update_meme_endpoint, new_meme_id_str):
    payload_copy = payload.copy()
    payload_copy["id"] = new_meme_id_str
    update_meme_endpoint.update_meme(meme_id=new_meme_id_str, payload=payload_copy)
    update_meme_endpoint.status_code_verification(status_code=400)
    update_meme_endpoint.invalid_data_response_message()


@allure.feature("UPDATE request")
@allure.story("Updating a meme")
@allure.title("Update meme with invalid payload json")
@pytest.mark.critical
def test_update_meme_payload_invalid_json(update_meme_endpoint, new_meme_id_int):
    update_meme_endpoint.update_meme(meme_id=new_meme_id_int, payload=payload_invalid_json)
    update_meme_endpoint.status_code_verification(status_code=400)
    update_meme_endpoint.invalid_data_response_message()


@allure.feature("UPDATE request")
@allure.story("Updating a meme")
@allure.title("Update meme with empty payload")
@pytest.mark.medium
def test_update_meme_payload_empty(update_meme_endpoint, new_meme_id_int):
    update_meme_endpoint.update_meme_empty_payload_data(new_meme_id_int)
    update_meme_endpoint.status_code_verification(status_code=400)
    update_meme_endpoint.invalid_data_response_message()


@allure.feature("UPDATE request")
@allure.story("Updating a meme")
@pytest.mark.medium
def test_update_meme_url_meme_id_none(update_meme_endpoint, new_meme_id_int):
    payload_copy = payload.copy()
    payload_copy["id"] = new_meme_id_int
    update_meme_endpoint.update_meme(meme_id=None, payload=payload_copy)
    update_meme_endpoint.status_code_verification(status_code=404)
    update_meme_endpoint.not_found_response_message_verification()


@allure.feature("UPDATE request")
@allure.story("Updating a meme")
@pytest.mark.medium
def test_update_meme_url_meme_id_empty(update_meme_endpoint, new_meme_id_int):
    payload_copy = payload.copy()
    payload_copy["id"] = new_meme_id_int
    update_meme_endpoint.update_meme_url_empty_meme_id(payload=payload_copy)
    update_meme_endpoint.status_code_verification(status_code=405)
    update_meme_endpoint.not_allowed_response_message()


@allure.feature("UPDATE request")
@allure.story("Updating a meme")
@pytest.mark.medium
@pytest.mark.parametrize("invalid_test_headers", invalid_headers)
def test_update_meme_invalid_headers(update_meme_endpoint, new_meme_id_int, invalid_test_headers):
    update_meme_endpoint.update_meme_invalid_headers(meme_id=new_meme_id_int, headers=invalid_test_headers)
    update_meme_endpoint.status_code_verification(status_code=401)
    update_meme_endpoint.unauthorized_response_message()
