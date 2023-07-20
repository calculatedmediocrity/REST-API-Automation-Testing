import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.new_requests import MyRequests


@allure.epic("Registration cases")
class TestUserRegister(BaseCase):
    @allure.description("This test successfully create user")
    def test_create_user_successfully(self):
        data = self.prepare_registration_data()
        response = MyRequests.post("/user", data=data)
        Assertions.assert_status_code(response, 200)
        Assertions.assert_json_has_key(response, "id")

    @allure.description("This test unsuccessful attempt to register a new user with an existing email address")
    def test_create_user_with_existing_email(self):
        existing_email = "testaa@example.com"
        data = self.prepare_registration_data(existing_email)
        response = MyRequests.post("/user", data=data)

        Assertions.assert_status_code(response, 400)

        assert response.content.decode("utf-8") == (
            f"Users with email '{existing_email}' already exists"), (
            f"Unexpected response content {response.content}"
        )
