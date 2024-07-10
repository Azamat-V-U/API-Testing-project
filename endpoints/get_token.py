import requests
import os
from endpoints.base_endpoint import BaseEndpoint


class GetToken(BaseEndpoint):

    base_path = os.path.dirname(__file__)
    token_file = os.path.join(base_path, "token.txt")

    def __init__(self, token=None):
        super().__init__(token)
        self.token = token or self.get_stored_token() or self.add_new_token()

    def check_valid_token(self):
        status_code = self.get_token_status()
        if status_code != 200:
            print("Stored token isn't valid")
            self.add_new_token()

    def get_token_status(self):
        response = requests.get(
            f"{self.url}/authorize/{self.token}",
        )
        print(f"Session token: {response.status_code}")
        return response.status_code

    def get_stored_token(self):
        if os.path.exists(self.token_file):
            with open(self.token_file, "r") as file:
                token = file.read().strip()
                if token:
                    self.token = token
                    self.headers = {"Authorization": f"{self.token}"}
                    return token
        return None

    def add_new_token(self):
        payload = {"name": "Diego"}
        response = requests.post(
            f"{self.url}/authorize",
            json=payload,
        )
        json = response.json()
        self.token = json.get("token")
        self.headers = {"Authorization": f"{self.token}"}
        self.store_token()
        return self.token

    def store_token(self):
        with open(self.token_file, "w") as file:
            file.write(self.token)

    def add_other_user_token(self):
        payload = {"name": "Pablo"}
        response = requests.post(
            f"{self.url}/authorize",
            json=payload,
        )
        self.json = response.json()
        self.token = self.json.get("token")
        self.name = self.json.get("user")
        return self.json
