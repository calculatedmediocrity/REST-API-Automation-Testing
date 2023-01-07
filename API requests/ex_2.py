import requests

resp = requests.get("https://playground.learnqa.ru/api/long_redirect", allow_redirects=True)

print(f"Redirects count - {len(resp.history)}")

print("History of redirects:")
for resp in resp.history:
    print(resp.status_code, resp.url)

print("Final URL after redirection:")
print(resp.status_code, resp.url)
