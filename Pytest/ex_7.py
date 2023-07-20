import requests


class TestApi:
    def test_get_homework_cookie(self):
        url = "https://playground.learnqa.ru/api/homework_cookie"
        expected_cookie_name = "HomeWork"
        expected_cookie_value = "hw_value"

        response = requests.get(url)

        assert expected_cookie_name in response.cookies, (
            f"Response doesn't contain {expected_cookie_name} cookie"
        )

        actual_cookie_value = response.cookies.get(expected_cookie_name)
        assert actual_cookie_value == expected_cookie_value, (
            f"Unexpected value '{actual_cookie_value}' for cookie '{expected_cookie_name}', "
            f"expected '{expected_cookie_value}'"
        )

        print(f"The cookie '{expected_cookie_name}' has value '{actual_cookie_value}'")
