# Pytest - Generate Allure Reports for API Testing with Python requests

## Tools

- pytest 
- requests 
- allure-pytest


## Running tests

* To download and install `pytest`, run this command from the terminal : `pip install pytest`
* To download and install `requests`, run this command from the terminal : `pip install requests`

To ensure all dependencies are resolved in a CI environment, in one go, add them to a `requirements.txt` file.
* Then run the following command : `pip install -r requirements.txt`

By default pytest only identifies the file names starting with `test_` or ending with `_test` as the test files.

Pytest requires the test method names to start with `test`. All other method names will be ignored even if we explicitly ask to run those methods.

A sample test below :

```python
    @allure.description("This test verifies the attempt to register a new user with an existing email address.")
    def test_create_user_with_existing_email(self):
        existing_email = "testaa@example.com"
        data = self.prepare_registration_data(existing_email)
        response = MyRequests.post("/user", data=data)

        Assertions.assert_status_code(response, 400)

        assert response.content.decode("utf-8") == (
            f"Users with email '{existing_email}' already exists"), (
            f"Unexpected response content {response.content}"
        )


```

If your tests are contained inside a folder 'Tests', then run the following command : `pytest Tests` 

To generate xml results, run the following command : `pytest Tests --junitxml="result.xml"`


## Generating Allure Reports

To generate Allure reports for your tests, follow these steps:

* Install Allure command-line tool by following the instructions here.
* Run your tests with the following command: 'pytest --alluredir=<pytest --alluredir=test_results /tests>'
* Navigate to the directory where the Allure results were generated and run the following command: allure serve test_results.

The Allure report will open in your default web browser.
