import requests
import allure
from bs4 import BeautifulSoup
import re
from endpoints.base_endpoint import BaseEndpoint


class DeleteMeme(BaseEndpoint):

    @allure.step("Send DELETE request to the 'BaseUrl/meme/<id>' endpoint with valid token")
    def delete_one_meme(self, meme_id=None):
        self.meme_id = meme_id
        self.response = requests.delete(
            f"{self.url}/meme/{meme_id}",
            headers=self.headers
        )
        print(f"Meme is deleted: meme_id {self.meme_id}:{self.response.status_code}")
        self.attach_response(self.response, is_json=False)
        return self.response

    @allure.step("Send DELETE request to the 'BaseUrl/meme' endpoint without meme_id")
    def delete_meme_url_empty_meme_id(self):
        self.response = requests.delete(
            f"{self.url}/meme",
            headers=self.headers
        )
        print(f"Meme isn't deleted: {self.meme_id}:{self.response.status_code}")
        self.attach_response(self.response, is_json=False)
        return self.response

    @allure.step("Send DELETE request to the 'BaseUrl/meme/<id>' endpoint with invalid headers")
    def delete_meme_invalid_headers(self, meme_id, headers=None):
        self.meme_id = meme_id
        self.response = requests.delete(
            f"{self.url}/meme/{meme_id}",
            headers=headers
        )
        print(f"Meme isn't deleted: {self.meme_id}:{self.response.status_code}")
        self.attach_response(self.response, is_json=False)
        return self.response

    @allure.step("Make sure that the response message is Not Found")
    def delete_response_message_ok(self):
        expected_message = f"Meme with id {self.meme_id} successfully deleted"
        assert expected_message in self.response.text, \
            f"Expected message '{expected_message} not found in response {self.response.text}'"

    @allure.step("Make sure that the response message is Forbidden")
    def forbidden_response_message_verification(self):

        expected_html_message = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title> 403 Forbidden </title>
        <h1> Forbidden </h1>
        <p> You are not the meme owner </p>
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
