import allure

from lib.base_case import BaseCase
from lib.assertions import Assertions
from lib.new_requests import MyRequests


@allure.epic("Edit user info cases")
class TestUserEdit(BaseCase):
    @allure.description("This test edit name of just created user")
    def test_edit_just_created_user(self):
        register_data = self.prepare_registration_data()
        response_create_user = MyRequests.post("/user", data=register_data)

        Assertions.assert_status_code(response_create_user, 200)
        Assertions.assert_json_has_key(response_create_user, "id")

        email = register_data["email"]
        password = register_data["password"]
        first_name = register_data["firstName"]
        user_id = self.get_json_value(response_create_user, "id")

        login_data = {
            "email": email,
            "password": password
        }

        response_login = MyRequests.post("/user/login", data=login_data)
        auth_sid = self.get_cookie(response_login, "auth_sid")
        token = self.get_token(response_login, "x-csrf-token")
        Assertions.assert_status_code(response_login, 200)

        new_name = "edited_name"
        response_edit = MyRequests.put(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid},
            data={"firstName": new_name}
        )
        Assertions.assert_status_code(response_edit, 200)

        response_check_edited_data = MyRequests.get(
            f"/user/{user_id}",
            headers={"x-csrf-token": token},
            cookies={"auth_sid": auth_sid}
        )
        Assertions.assert_status_code(response_check_edited_data, 200)
        Assertions.assert_json_value_by_name(
            response_check_edited_data,
            "firstName",
            new_name,
            f"Actual name {first_name} is not equal to actual name {new_name}"
        )
