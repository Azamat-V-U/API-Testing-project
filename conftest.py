import pytest
from endpoints.create_meme import CreateMeme
from endpoints.get_meme import GetOneMeme
from endpoints.get_meme import GetAllMemes
from endpoints.get_token import GetToken
from endpoints.update_meme import UpdateMeme
from endpoints.delete_meme import DeleteMeme
from endpoints.create_token import CreateToken
from endpoints.get_token_status import GetTokenStatus


@pytest.fixture(scope="session")
def authorization_token():
    base_endpoint = GetToken()
    base_endpoint.check_valid_token()
    print(f"Session token: {base_endpoint.headers}")
    return base_endpoint.token


@pytest.fixture(scope="session")
def new_user_authorization_token():
    base_endpoint = GetToken()
    base_endpoint.add_other_user_token()
    print(f"New session token: {base_endpoint.token}, user: {base_endpoint.name}")
    return base_endpoint.token, base_endpoint.name


@pytest.fixture(scope="session")
def new_meme_id_int(authorization_token):
    payload = {
        "text": "Sponge Bob",
        "url": "www.example.com",
        "tags": ["Some tag", "another tag"],
        "info": {"colors": ["green", "red"], "objects": ["text", "picture"]}
    }
    new_meme_instance = CreateMeme(authorization_token)
    json, response = new_meme_instance.create_meme(payload=payload)
    new_meme_id = json["id"]
    print(f"Session meme id: {type(new_meme_id)}, {new_meme_id}")
    yield new_meme_id
    delete_meme_instance = DeleteMeme(authorization_token)
    delete_meme_instance.delete_one_meme(new_meme_id)


@pytest.fixture(scope="session")
def new_meme_id_str(authorization_token):
    payload = {
        "text": "Sponge Bob",
        "url": "www.example.com",
        "tags": ["Some tag", "another tag"],
        "info": {"colors": ["green", "red"], "objects": ["text", "picture"]}
    }
    new_meme_instance = CreateMeme(authorization_token)
    json, response = new_meme_instance.create_meme(payload=payload)
    new_meme_id = json["id"]
    print(f"Session meme id str: {new_meme_id}")
    yield str(new_meme_id)
    delete_meme_instance = DeleteMeme(authorization_token)
    delete_meme_instance.delete_one_meme(new_meme_id)


@pytest.fixture(scope="session")
def meme_id_new_token(new_user_authorization_token):
    token, name = new_user_authorization_token
    payload = {
        "text": "Sponge Bob",
        "url": "www.example.com",
        "tags": ["Some tag", "another tag"],
        "info": {"colors": ["green", "red"], "objects": ["text", "picture"]}
    }
    new_meme_instance = CreateMeme(token)
    json, response = new_meme_instance.create_meme(payload=payload)
    new_meme_id = json["id"]
    print(f"Meme id with old token for delete method: {new_meme_id}, name: {name} new token: {token}")
    yield new_meme_id
    delete_meme_instance = DeleteMeme(new_user_authorization_token)
    delete_meme_instance.delete_one_meme(new_meme_id)


@pytest.fixture(scope="session")
def meme_id_old_token(authorization_token):
    token = authorization_token
    payload = {
        "text": "Sponge Bob",
        "url": "www.example.com",
        "tags": ["Some tag", "another tag"],
        "info": {"colors": ["green", "red"], "objects": ["text", "picture"]}
    }
    new_meme_instance = CreateMeme(authorization_token)
    json, response = new_meme_instance.create_meme(payload=payload)
    new_meme_id = json["id"]
    print(f"Meme id with new token for delete method: {new_meme_id}, old token: {token}")
    return new_meme_id



@pytest.fixture()
def get_all_memes_endpoint(authorization_token):
    return GetAllMemes(authorization_token)


@pytest.fixture()
def get_one_meme_endpoint(authorization_token):
    return GetOneMeme(authorization_token)


@pytest.fixture()
def create_meme_endpoint(authorization_token):
    yield CreateMeme(authorization_token)


@pytest.fixture()
def update_meme_endpoint(authorization_token):
    return UpdateMeme(authorization_token)


@pytest.fixture()
def delete_meme_endpoint(authorization_token):
    return DeleteMeme(authorization_token)


@pytest.fixture()
def create_token_endpoint():
    return CreateToken()


@pytest.fixture()
def get_token_status_endpoint(new_user_authorization_token):
    token, name = new_user_authorization_token
    endpoint = GetTokenStatus(token)
    endpoint.name = name
    return endpoint


@pytest.fixture()
def get_token_status_invalid_token():
    return GetTokenStatus()


@pytest.fixture()
def get_token_status_invalid_url_token(authorization_token):
    return GetTokenStatus(authorization_token)
