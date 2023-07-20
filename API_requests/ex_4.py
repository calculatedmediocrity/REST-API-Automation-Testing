import requests
import time

url = "https://playground.learnqa.ru/ajax/api/longtime_job"


def create_long_time_job():
    global url
    response = requests.get(url)
    token = response.json()["token"]
    seconds = response.json()["seconds"]
    print(f"Task created with token: {token} and {seconds} seconds to complete")
    return token, seconds


def check_long_time_job_status(token):
    global url
    response = requests.get(url, params={"token": token})
    status = response.json()["status"]
    print(f"Task status is {status}")
    return status


def wait_for_long_time_job(seconds):
    print(f"Waiting for {seconds} seconds")
    time.sleep(seconds)


def check_long_time_job_result(token):
    global url
    response = requests.get(url, params={"token": token})
    status = response.json()["status"]
    if status == "Job is NOT ready":
        print("Task is not ready yet")
    elif status == "Job is ready":
        result = response.json()["result"]
        print(f"Task result: {result}")
    else:
        print("Unknown status")


def solve_long_time_job():
    token, seconds = create_long_time_job()
    status = check_long_time_job_status(token)
    while status != "Job is ready":
        wait_for_long_time_job(seconds)
        status = check_long_time_job_status(token)
    check_long_time_job_result(token)


solve_long_time_job()
