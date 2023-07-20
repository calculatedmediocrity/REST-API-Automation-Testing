import requests

url = "https://playground.learnqa.ru/ajax/api/compare_query_type"

methods = ["GET", "POST", "PUT", "DELETE"]
for method in methods:
    for param in methods:
        payload = {"method": param}
        if method == "GET":
            response = requests.request(method, url, params=payload)
            print(
                f"{method} request with url {param} parameter:",
                response.text
            )
        else:
            response = requests.request(method, url, data=payload)
            print(
                f"{method} request with {param} method parameter:",
                response.text
            )
