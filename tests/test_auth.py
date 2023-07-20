import pytest
import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.new_requests import MyRequests


@allure.epic("Authorization cases")
class TestApi(BaseCase):
    exclude_params = [
        ("no_cookie"),
        ("no_token")
    ]

    def setup(self):
        data = {
            "email": "testaa@example.com",
            "password": "secret_Password1"
        }

        auth_response = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(auth_response, "auth_sid")
        self.token = self.get_token(auth_response, "x-csrf-token")
        self.user_id = self.get_json_value(auth_response, "user_id")

    @allure.description("This test successfully authorize user by email and password")
    def test_positive_auth(self):
        check_auth_response = MyRequests.get(
            "/user/auth",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )

        Assertions.assert_json_value_by_name(
            check_auth_response,
            "user_id",
            self.user_id,
            "User id from check method is not equal to user id from auth method"
        )

    @allure.description("this test checks authorization status w/o sending auth cookie or token ")
    @pytest.mark.parametrize("condition", exclude_params)
    def test_negative_auth(self, condition):
        if condition == "no_cookie":
            check_auth_response = MyRequests.get(
                "/user/auth",
                headers={"x-csrf-token": self.token},
            )
        else:
            check_auth_response = MyRequests.get(
                "/user/auth",
                cookies={"auth_sid": self.auth_sid}
            )
        Assertions.assert_json_value_by_name(
            check_auth_response,
            "user_id",
            0,
            f"User is authorized with condition {condition}"
        )
