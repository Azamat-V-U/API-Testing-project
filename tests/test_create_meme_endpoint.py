import pytest
import allure


valid_meme_payload = [
    {
        "text": "Sponge Bob",
        "url": "www.example.by",
        "tags": ["Sponge Bob", "Cartoon"],
        "info": {"colors": ["yellow", "brown"]}
    },
    {
        "text": "Mister Bin",
        "url": "www.example.by",
        "tags": ["Sponge Bob", "Cartoon", "some tag"],
        "info": {"colors": ["yellow", "brown", "red"]}
    },
    {
        "text": "Sponge Bob",
        "url": "www.example.com",
        "tags": ["Sponge Bob", "Cartoon", "some text", "some tag"],
        "info": {"colors": ["yellow", "brown", "red", "black"]}
    }
]

invalid_meme_payload = [
    {
        "text": "Sponge Bob"
    },
    {
        "text": "",
        "url": "",
        "tags": [],
        "info": {}
    },
    {}
]

invalid_json_payload = '{"name": "John"'
invalid_headers = [
    {"Authorization": "jFsj8svr55XDbjw"},
    {"Authorization": ""},
    {}

]

# Positive tests


@allure.feature("Post request")
@allure.story("Meme creation")
@allure.title("Create meme with valid data")
@pytest.mark.critical
@pytest.mark.parametrize("valid_test_data", valid_meme_payload)
def test_create_meme_valid_data(create_meme_endpoint, delete_meme_endpoint, valid_test_data):
    create_meme_endpoint.create_meme(payload=valid_test_data)
    create_meme_endpoint.status_code_verification(status_code=200)
    create_meme_endpoint.id_verification(meme_id=create_meme_endpoint.meme_id)
    create_meme_endpoint.payload_parameters_verification(payload=valid_test_data)
    delete_meme_endpoint.delete_one_meme(meme_id=create_meme_endpoint.meme_id)

# Negative tests


@allure.feature("POST request")
@allure.story("Meme creation")
@allure.title("Create meme with invalid data")
@pytest.mark.critical
@pytest.mark.parametrize("invalid_test_data", invalid_meme_payload)
def test_create_meme_invalid_data(create_meme_endpoint, invalid_test_data):
    create_meme_endpoint.create_meme(payload=invalid_test_data)
    create_meme_endpoint.status_code_verification(status_code=400)
    create_meme_endpoint.invalid_data_response_message()


@allure.feature("POST request")
@allure.story("Meme creation")
@allure.title("Create meme with the invalid json object")
@pytest.mark.medium
def test_create_meme_invalid_json(create_meme_endpoint):
    create_meme_endpoint.create_meme(payload=invalid_json_payload)
    create_meme_endpoint.status_code_verification(status_code=400)
    create_meme_endpoint.invalid_data_response_message()


@allure.feature("POST request")
@allure.story("Meme creation")
@allure.title("Create meme with the invalid headers")
@pytest.mark.critical
@pytest.mark.parametrize("invalid_test_headers", invalid_headers)
def test_create_meme_invalid_headers(create_meme_endpoint, invalid_test_headers):
    create_meme_endpoint.create_meme_invalid_headers(payload=valid_meme_payload, headers=invalid_test_headers)
    create_meme_endpoint.status_code_verification(status_code=401)
    create_meme_endpoint.unauthorized_response_message()
