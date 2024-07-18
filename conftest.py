import pytest
from endpoints.create_meme import CreateMeme
from endpoints.get_meme import GetOneMeme
from endpoints.get_meme import GetAllMemes
from endpoints.get_token import GetToken
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.create_token import CreateToken
from endpoints.get_token_status import GetTokenStatus
from endpoints.payloads import PayloadCreateMeme


@pytest.fixture(scope="session")
def payload():
    return PayloadCreateMeme


@pytest.fixture(scope="session")
def user_1_auth_token():
    base_endpoint = GetToken()
    base_endpoint.check_valid_token()
    print(f"Session token: {base_endpoint.headers}")
    return base_endpoint.token


@pytest.fixture(scope="session")
def user_2_auth_token():
    base_endpoint = GetToken()
    base_endpoint.add_other_user_token()
    print(f"New session token: {base_endpoint.token}, user: {base_endpoint.name}")
    return base_endpoint.token, base_endpoint.name


@pytest.fixture(scope="session")
def new_meme_user_1_token(user_1_auth_token, payload, delete_meme_endpoint):
    new_meme_instance = CreateMeme(user_1_auth_token)
    json, response = new_meme_instance.create_meme(payload=payload.valid_data_one_payload)
    new_meme_id = json["id"]
    print(f"Session meme id: {type(new_meme_id)}, {new_meme_id}")
    yield new_meme_id
    delete_meme_endpoint.delete_one_meme(new_meme_id)


@pytest.fixture()
def get_all_memes_endpoint(user_1_auth_token):
    return GetAllMemes(user_1_auth_token)


@pytest.fixture()
def get_one_meme_endpoint(user_1_auth_token):
    return GetOneMeme(user_1_auth_token)


@pytest.fixture()
def create_meme_endpoint(user_1_auth_token):
    yield CreateMeme(user_1_auth_token)


@pytest.fixture()
def update_meme_endpoint(user_1_auth_token):
    return UpdateMeme(user_1_auth_token)


@pytest.fixture(scope="session")
def delete_meme_endpoint(user_1_auth_token):
    return DeleteMeme(user_1_auth_token)


@pytest.fixture(scope="session")
def new_meme_user_2_token(user_2_auth_token, payload):
    token, name = user_2_auth_token
    new_meme_instance = CreateMeme(token)
    json, response = new_meme_instance.create_meme(payload=payload.valid_data_one_payload)
    new_meme_id = json["id"]
    print(f"Meme id with the user_2 token: {new_meme_id}, name: {name} new token: {token}")
    yield new_meme_id
    delete_meme_instance = DeleteMeme(user_2_auth_token)
    delete_meme_instance.delete_one_meme(new_meme_id)


@pytest.fixture(scope="session")
def new_meme_user_1_token_for_delete_method(user_1_auth_token, payload):
    token = user_1_auth_token
    new_meme_instance = CreateMeme(user_1_auth_token)
    json, response = new_meme_instance.create_meme(payload=payload.valid_data_one_payload)
    new_meme_id = json["id"]
    print(f"Meme id with the user_1 token for delete method: {new_meme_id}, old token: {token}")
    return new_meme_id


@pytest.fixture()
def create_token_endpoint():
    return CreateToken()


@pytest.fixture()
def get_token_status_endpoint(user_2_auth_token):
    token, name = user_2_auth_token
    endpoint = GetTokenStatus(token)
    endpoint.name = name
    return endpoint


@pytest.fixture()
def get_token_status_invalid_token():
    return GetTokenStatus()
