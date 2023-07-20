import requests


class TestApi:
    def test_headers(self):
        url = "https://playground.learnqa.ru/api/homework_header"
        expected_headers = {
            'Date': 'Sat, 15 Jul 2023 12:06:46 GMT',
            'Content-Type': 'application/json',
            'Content-Length': '15',
            'Connection': 'keep-alive',
            'Keep-Alive': 'timeout=10',
            'Server': 'Apache',
            'x-secret-homework-header': 'Some secret value',
            'Cache-Control': 'max-age=0',
            'Expires': 'Sat, 15 Jul 2023 12:06:46 GMT'
        }

        response = requests.get(url)
        actual_headers = response.headers
        assert expected_headers.keys() == actual_headers.keys(), "Headers are not equal"

        actual_hw_header_value = actual_headers.get('x-secret-homework-header')
        assert actual_hw_header_value == expected_headers['x-secret-homework-header'], (
            f"HW header value is not {expected_headers['x-secret-homework-header']}"
        )
