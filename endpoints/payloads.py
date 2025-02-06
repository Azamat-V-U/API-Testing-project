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
            "tags": [46896, "Cartoon", "some tag"],
            "info": {"colors": ["yellow", "brown", "red"]}
        },
        {
            "text": "Sponge Bob",
            "url": "www.example.com",
            "tags": [8792, "Cartoon", "some text", "some tag"],
            "info": {"colors": ["yellow", 89167, "red", "black"]}
        }
    ]

    invalid_data_create_meme = [
        {
            "text": "Sponge Bob"
        },
        {
            "text": "Sponge Bob",
            "url": "www.example.com"
        },
        {
            "text": "Sponge Bob",
            "url": "www.example.com",
            "tags": ["Sponge Bob", "Cartoon"]
        },
        {
            "text": 1687,
            "url": "www.example.com",
            "tags": ["Sponge Bob", "Cartoon"],
            "info": {"colors": ["yellow", "brown"]}
        },
        {
            "text": "Sponge Bob",
            "url": 8946,
            "tags": ["Sponge Bob", "Cartoon"],
            "info": {"colors": ["yellow", "brown"]}
        },
        {
            "text": "Sponge Bob",
            "url": "www.example.by",
            "tags": 4972,
            "info": {"colors": ["yellow", "brown"]}
        },
        {
            "text": "Sponge Bob",
            "url": "www.example.by",
            "tags": ["Sponge Bob", "Cartoon"],
            "info": 9712
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
        {
            "id": None,
            "text": "",
            "url": "",
            "tags": ["Sponge Bob", "Cartoon"],
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
        {"name": "B"},
        {"name": f"{'b' * 125}"},
        {"name": f"{'B' * 256}"}
    ]
    invalid_data_create_token = [
        {"name": ""},
        {},
        {"name": 30},
        {"name": 0.30},
        {"name": "c" * 257},
        {"name": "@%&"}
    ]
