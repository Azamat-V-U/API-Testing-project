import allure
import json
from allure_commons.types import AttachmentType
from bs4 import BeautifulSoup
import re


class BaseEndpoint:

    url = "http://167.172.172.115:52355"
    response = None
    json = None
    meme_id = None
    payload = None
    name = None

    def __init__(self, token=None):
        self.token = token
        self.headers = {"Authorization": f"{self.token}"}

    @allure.step("Make sure that the response status code is correct")
    def status_code_verification(self, status_code):
        assert self.response.status_code == status_code, \
            f"The status code doesn't match: expected :{status_code} != actual: {self.response.status_code}"

    @allure.step("Make sure that the id in the request matches with the meme id in the response")
    def id_verification(self, meme_id):
        assert self.json.get("id") == meme_id, f"Response meme_id: {self.json.get("id")} != {self.meme_id}"

    @allure.step("Make sure that the payload parameters match with the parameters in the response json object")
    def payload_parameters_verification(self, payload):
        for key, value in payload.items():
            assert key in self.json, f"Key '{key} not found in response'"
            assert self.json[key] == value, (f"Value for key '{key}' doesn't match: Actual"
                                             f"{type(key)}{self.json[key]} != Expected: {type(value)}{value}")

    @allure.step("Check that the expected response message is Bad Request")
    def invalid_data_response_message_verification(self):

        expected_html_message = """
        <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
        <title> 400 Bad Request </title>
        <h1> Bad Request </h1>
        <p> Invalid parameters </p>
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

    @allure.step("Check that the expected response message is Not authorized")
    def unauthorized_response_message_verification(self):

        expected_html_message = """
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
            <title> 401 Unauthorized </title>
            <h1> Unauthorized </h1>
            <p> Not authorized </p>
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

    @allure.step("Check that the expected response message is NOT FOUND")
    def not_found_response_message_verification(self):
        expected_html_message = """
            <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
            <title> 404 Not Found </title>
            <h1> Not Found </h1>
            <p> The requested URL was not found on the server. 
            If you entered the URL manually please check your spelling and try again. </p>
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

    @allure.step("Check that the expected response message")
    def not_allowed_response_message_verification(self):

        expected_html_message = """
                <!DOCTYPE HTML PUBLIC "-//W3C//DTD HTML 3.2 Final//EN">
                <title> 405 Method Not Allowed </title>
                <h1> Method Not Allowed </h1>
                <p> The method is not allowed for the requested URL. </p>
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

    def attach_response(self, response, is_json=True):
        if is_json:
            response_body = json.dumps(response, indent=4)
            attachment_type = AttachmentType.JSON
        else:
            response_body = response.text
            attachment_type = AttachmentType.TEXT

        allure.attach(body=response_body, name="Api Response", attachment_type=attachment_type)
