import requests
import allure
from bs4 import BeautifulSoup
import re
from endpoints.base_endpoint import BaseEndpoint


class GetTokenStatus(BaseEndpoint):
    @allure.step("Send GET request to the 'BaseUrl/authorize/<token>' endpoint with valid token")
    def get_token_status(self):
        self.response = requests.get(
            f"{self.url}/authorize/{self.token}",
        )
        print(f"{self.url}/authorize/{self.token}")
        print(f"Response message: {self.response.text}, token: {self.token}")
        return self.response

    @allure.step("Send GET request to the 'BaseUrl/authorize/<token>' endpoint with invalid token")
    def get_token_status_invalid_token(self, token=None):
        self.token = token
        self.response = requests.get(
            f"{self.url}/authorize/{self.token}",
        )
        print(f"{self.url}/authorize/{self.token}")
        print(f"Response message: {self.response.text}, token: {self.token}")
        return self.response

    @allure.step("Send GET request to the 'BaseUrl/authorize' endpoint without a token")
    def get_token_status_empty_token(self):
        self.response = requests.get(
            f"{self.url}/authorize",
        )
        print(f"Response message: {self.response.text}, The session token is: {self.token}")
        return self.response

    @allure.step("Send GET request to the 'BaseUrl/<token>' endpoint with valid token")
    def get_token_status_invalid_url(self):
        self.response = requests.get(
            f"{self.url}/{self.token}",
        )
        print(f"Response message: {self.response.text}, The session token is: {self.token}")
        return self.response

    @allure.step("Make sure that the response message is correct and contains correct username")
    def get_token_status_response_message_ok(self, name):
        expected_message = f"Token is alive. Username is {name}"
        assert expected_message in self.response.text, \
            f"Expected message '{expected_message} not found in response {self.response.text}'"

    @allure.step("Make sure that the response message is 'NOT FOUND'")
    def token_not_found_response_message_verification(self):
        expected_html_message = """
                <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
                <title> 404 Not Found </title>
                <h1> Not Found </h1>
                <p> Token not found </p>
                """

        if expected_html_message:
            soup = BeautifulSoup(self.response.text, "html.parser")
            actual_html_message = soup.prettify()

            actual_html_message = re.sub(r'\s+', ' ', actual_html_message.strip())
            print(actual_html_message)
            expected_html_message = re.sub(r'\s+', ' ', expected_html_message.strip())
            print(expected_html_message)

            assert actual_html_message == expected_html_message, \
                (f"Expected HTML message does not match. \nExpected:\n{expected_html_message}\n\n"
                 f"Got:\n{actual_html_message}")
