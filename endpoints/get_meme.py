import requests
import allure
from pydantic import BaseModel, ValidationError, Field
from typing import List, Union, Optional
from endpoints.base_endpoint import BaseEndpoint
from bs4 import BeautifulSoup
import re


class MemeInfo(BaseModel):
    colors: Optional[List[Union[str, int]]] = Field(None, description="List of objects")
    objects: Optional[List[Union[str, int]]] = Field(None, description="List of objects")


class Meme(BaseModel):
    id: int
    info: MemeInfo
    tags: List[str]
    text: str
    updated_by: str
    url: str


class GetAllMemes(BaseEndpoint):

    @allure.step("Send GET request to the 'BaseUrl/meme' endpoint with valid token")
    def get_all_memes(self):
        self.response = requests.get(
            f"{self.url}/meme",
            headers=self.headers
        )
        self.json = self.response.json()
        print(f"Status code: {self.response.status_code}")
        return self.json, self.response

    @allure.step("Send GET request to the 'BaseUrl/meme' endpoint with invalid token")
    def get_all_memes_with_invalid_token(self, headers=None):
        self.response = requests.get(
            f"{self.url}/meme",
            headers=headers
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
        else:
            self.json = None
        print(f"Status code: {self.response.status_code}")
        return self.json, self.response

    @allure.step("Make sure that the response body contains a JSON object with an array of memes")
    def json_objects_verification(self):
        try:
            assert isinstance(self.json, dict), "Json object isn't returned"
            assert isinstance(self.json["data"], list), "'data' field should be an array"
        except ValueError as e:
            assert False, f"Response is not valid JSON. ValueError: {e}"


class GetOneMeme(BaseEndpoint):

    @allure.step("Send GET request to the 'BaseUrl/meme/<id>' url with valid token")
    def get_meme(self, meme_id=None):
        self.response = requests.get(
            f"{self.url}/meme/{meme_id}",
            headers=self.headers
        )
        if self.response.status_code == 200:
            self.json = self.response.json()
        else:
            self.json = None
        print(f"Status code: {self.response.status_code}, json: {self.json}")
        return self.json, self.response

    @allure.step("Send GET request to the 'BaseUrl/meme/<id>' url with invalid headers")
    def get_meme_with_invalid_headers(self, meme_id=None, headers=None):
        self.response = requests.get(
            f"{self.url}/meme/{meme_id}",
            headers=headers
        )
        print(f"Status code: {self.response.status_code}, message: {self.response.text}")
        return self.response

    @allure.step("Check that the required fields in the response json object")
    def required_fields_verification(self):
        assert "info" in self.json, "'info' field is missing in the response"
        assert "tags" in self.json, "'tags' field is missing in the response"
        assert "text" in self.json, "'text' field is missing in the response"
        assert "url" in self.json, "'url' field is missing in the response"
        assert isinstance(self.json["info"], dict), "'info' field should be an object"
        assert isinstance(self.json["tags"], list), "'tags' field should be an array"

    @allure.step("Check that the optional fields in the response json object")
    def optional_fields_verification(self):
        info = self.json["info"]
        assert "colors" in info, "'colors' field is missing in the 'info' object"
        assert "objects" in info, "'objects' field is missing in the 'info' object"
        assert isinstance(info["colors"], list), "'colors' field should be an array"
        assert isinstance(info["objects"], list), "'objects' field should be an array"

    def validate_json_object(self, response_json, model):
        try:
            model_instance = model(**response_json)
            return model_instance
        except ValidationError as e:
            assert False, f"JSON validation error: {e}"

    @allure.step("Check that the required data types in the values of a returned json object")
    def required_value_data_types_verification(self):
        assert self.validate_json_object(self.json, Meme), f"Json object isn't correct"

    @allure.step("Check the expected response message")
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
            expected_html_message = re.sub(r'\s+', ' ', expected_html_message.strip())

            assert actual_html_message == expected_html_message, \
                (f"Expected HTML message does not match. \nExpected:\n{expected_html_message}\n\n"
                 f"Got:\n{actual_html_message}")
