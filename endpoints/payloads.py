from faker import Faker


fake = Faker()


class BasePayloads:

    invalid_json_payload = '{"name": "John"'
    invalid_headers = [
        {"Authorization": "jFsj8svr55XDbjw"},
        {"Authorization": ""},
        {}

    ]
    invalid_token = [None, "NzL2mMwGayfyQ"]


class PayloadCreateMeme(BasePayloads):

    valid_data_create_meme = [
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

    invalid_data_create_meme = [
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

    valid_data_one_payload = {
        "text": "Sponge Bob",
        "url": "www.example.com",
        "tags": ["Some tag", "another tag"],
        "info": {"colors": ["green", "red"], "objects": ["text", "picture"]}
    }


class PayloadUpdateMeme(BasePayloads):

    valid_data_update_meme = [
        {
            "id": None,
            "text": fake.name(),
            "url": fake.url(),
            "tags": ["Sponge Bob", "Cartoon", "some tags"],
            "info": {"colors": ["yellow", "brown", "red"]}
        },
        {
            "id": None,
            "text": fake.name(),
            "url": fake.url(),
            "tags": ["Mister Bin", "Cartoon", "some tag"],
            "info": {"colors": ["yellow", "brown", "red", "black"]}
        },
        {
            "id": None,
            "text": fake.name(),
            "url": fake.url(),
            "tags": ["Simpsons", "Cartoon", "some tag", "some tag"],
            "info": {"colors": ["yellow", "brown", "black", "green", "red"]}
        }
    ]

    invalid_data_update_meme = [
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
    valid_data_one_payload = {
        "id": None,
        "info": {"colors": ["yellow", "brown", "green"]},
        "tags": ["Sponge Bob", "Cartoon"],
        "text": "Sponge Bob",
        "url": "www.example.com"
    }


class PayloadCreateToken(BasePayloads):

    valid_data_create_token = [
        {"name": fake.name()},
        {"name": fake.name()},
        {"name": fake.name()}
    ]
    invalid_data_create_token = [
        {"name": ""},
        {},
        {"name": 30},
        {"name": "c" * 256},
        {"name": "#@%&"}
    ]
