import requests
import allure
from endpoints.base_endpoint import BaseEndpoint


class UpdateMeme(BaseEndpoint):

    @allure.step("Send PUT request to the 'BaseUrl/meme/<id>' endpoint")
    def update_meme(self, meme_id=None, payload=None):

        self.response = requests.put(
            f"{self.url}/meme/{meme_id}",
            json=payload,
            headers=self.headers

        )
        if self.response.status_code == 200:
            self.json = self.response.json()
            self.meme_id = self.json["id"]
        else:
            self.json = None
        print(f"Meme is updated: {type(self.meme_id)}: {self.meme_id}")
        return self.json, self.response

    @allure.step("Send PUT request to the 'BaseUrl/meme/<id>' endpoint without meme id in the url")
    def update_meme_url_empty_meme_id(self, payload=None):
        self.response = requests.put(
            f"{self.url}/meme",
            json=payload,
            headers=self.headers

        )
        return self.response

    @allure.step("Send PUT request to the 'BaseUrl/meme/<id>' endpoint without payload data")
    def update_meme_empty_payload_data(self, meme_id=None):
        self.response = requests.put(
            f"{self.url}/meme/{meme_id}",
            json=self.payload,
            headers=self.headers

        )
        return self.response

    @allure.step("Send PUT request to the 'BaseUrl/meme/<id>' endpoint with invalid headers")
    def update_meme_invalid_headers(self, meme_id=None, headers=None):
        self.response = requests.put(
            f"{self.url}/meme/{meme_id}",
            json=self.payload,
            headers=headers

        )
        return self.response
