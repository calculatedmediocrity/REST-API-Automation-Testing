import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.new_requests import MyRequests


@allure.epic("User information retrieval case")
class TestUserGet(BaseCase):
    def setup(self):
        data = {
            "email": "testaa@example.com",
            "password": "secret_Password1"
        }
        response_login = MyRequests.post("/user/login", data=data)

        self.auth_sid = self.get_cookie(response_login, "auth_sid")
        self.token = self.get_token(response_login, "x-csrf-token")
        self.user_id = self.get_json_value(response_login, "user_id")

    @allure.description("This test get info about unauthorized user")
    def test_user_get_info_not_auth(self):
        response = MyRequests.get("/user/2")
        Assertions.assert_json_has_key(response, "username")
        Assertions.assert_json_has_not_key(response, "email")
        Assertions.assert_json_has_not_key(response, "firstName")
        Assertions.assert_json_has_not_key(response, "lastName")

    @allure.description("This test get info about authorized user")
    def test_user_get_info_auth_as_same_user(self):
        response = MyRequests.get(
            f"/user/{self.user_id}",
            headers={"x-csrf-token": self.token},
            cookies={"auth_sid": self.auth_sid}
        )
        expected_fields = ["username", "email", "firstName", "lastName"]
        Assertions.assert_json_has_keys(response, expected_fields)
