import allure
import requests
import re
from endpoints.base_endpoint import BaseEndpoint
from bs4 import BeautifulSoup


class CreateToken(BaseEndpoint):

    @allure.step("Send POST request to the 'BaseUrl/authorize' endpoint")
    def create_token_valid_data(self, payload=None):
        self.response = requests.post(
            f"{self.url}/authorize",
            json=payload
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
            print(self.json)
        else:
            self.json = None
        return self.json, self.response

    @allure.step("Send POST request to the 'BaseUrl/authorize' endpoint with invalid payload data")
    def create_token_invalid_data(self, payload=None):
        self.response = requests.post(
            f"{self.url}/authorize",
            json=payload
        )
        return self.response

    @allure.step("Check the returned json object and the payload name = user")
    def authorization_response_json_object_verification(self, payload):
        assert "token" in self.response.json(), f"Token not found in the json object"
        assert "user" in self.response.json(), f"User not found in the json object"
        assert self.response.json()["user"] == payload["name"], f"Payload name doesn't match with the user name "

    @allure.step("Check that the expected response message is Bad Request")
    def invalid_json_response_message(self):

        expected_html_message = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title> 400 Bad Request </title>
        <h1> Bad Request </h1>
        <p> The browser (or proxy) sent a request that this server could not understand. </p>
        """

        if expected_html_message:
            soup = BeautifulSoup(self.response.text, "html.parser")
            actual_html_message = soup.prettify()

            actual_html_message = re.sub(r'\s+', ' ', actual_html_message.strip())
            print(actual_html_message)
            expected_html_message = re.sub(r'\s+', ' ', expected_html_message.strip())
            print(f"expected message: {expected_html_message}")

            assert actual_html_message == expected_html_message, \
                (f"Expected HTML message does not match. \nExpected:\n{expected_html_message}\n\n"
                 f"Got:\n{actual_html_message}")
