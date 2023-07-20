from requests import Response
import json


class Assertions:
    @staticmethod
    def assert_status_code(response: Response, expected_status_code):
        assert response.status_code == expected_status_code, (
            f"Unexpected status code {response.status_code}! Expected - {expected_status_code}"
        )

    @staticmethod
    def assert_json_value_by_name(response: Response, json_key, expected_value, error_message):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON. Response text {response.text}"

        assert json_key in response_as_dict, (
            f"Cannot find JSON key {json_key} in the response"
        )
        actual_value = response_as_dict[json_key]
        assert actual_value == expected_value, error_message

    @staticmethod
    def assert_json_has_key(response: Response, json_key):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON. Response text {response.text}"

        assert json_key in response_as_dict, (
            f"Cannot find JSON key {json_key} in the response"
        )

    @staticmethod
    def assert_json_has_not_key(response: Response, json_key):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON. Response text {response.text}"

        assert json_key not in response_as_dict, (
            f"JSON Response should not have key {json_key}"
        )

    @staticmethod
    def assert_json_has_keys(response: Response, json_keys: list):
        try:
            response_as_dict = response.json()
        except json.decoder.JSONDecodeError:
            assert False, f"Response is not in JSON. Response text {response.text}"
        for json_key in json_keys:
            assert json_key in response_as_dict, (
                f"Cannot find JSON key {json_key} in the response"
            )
