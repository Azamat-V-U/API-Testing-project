import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class CreateMeme(BaseEndpoint):

    @allure.step("Send POST request to the 'BaseUrl/meme' endpoint")
    def create_meme(self, payload=None):
        self.response = requests.post(
            f"{self.url}/meme",
            json=payload,
            headers=self.headers

        )
        if self.response.status_code == 200:
            self.json = self.response.json()
            self.meme_id = self.json.get("id")
            print(f"Meme is created: {self.meme_id}, headers: {self.headers}")
            self.attach_response(self.json, is_json=True)
            return self.json, self.response
        else:
            self.json = None
            self.attach_response(self.response, is_json=False)
            return self.response, self.response.text

    @allure.step("Send POST request to the 'BaseUrl/meme' endpoint with invalid headers")
    def create_meme_invalid_headers(self, payload=None, headers=None):
        self.response = requests.post(
            f"{self.url}/meme",
            json=payload,
            headers=headers

        )
        if self.response.status_code == 200:
            self.json = self.response.json()
            self.meme_id = self.json["id"]
            print(f"Meme is created: {self.json["id"]}, headers: {self.headers}")
        else:
            self.json = None
        return self.json, self.response
