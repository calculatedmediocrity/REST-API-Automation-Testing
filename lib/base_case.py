from requests import Response
import json
import datetime


class BaseCase:
    def get_cookie(self, response: Response, cookie_name):
        assert cookie_name in response.cookies, (
            f"Cannot find cookie with the name {cookie_name} in the response. {response.text}"
        )
        return response.cookies.get(cookie_name)

    def get_token(self, response: Response, token_name):
        assert token_name in response.headers, (
            f"Cannot find token with the name {token_name} in the response"
        )
        return response.headers.get(token_name)

    def get_json_value(self, response: Response, json_key):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON. Response text {response.text}"

        assert json_key in response_as_dict, (
            f"Cannot find JSON key {json_key} in the response"
        )
        return response_as_dict[json_key]

    def prepare_registration_data(self, email=None):
        if email is None:
            base_part = "test"
            random_part = datetime.datetime.now().strftime("%m%d%Y%H%M%S")
            domain = "example.com"
            email = f"{base_part}{random_part}@{domain}"
        data = {
            "username": "test_username",
            "firstName": "First name",
            "lastName": "Last name",
            "email": email,
            "password": "secret_Password1!",
        }
        return data

