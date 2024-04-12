# Task-1
## Objective:
Select a POST request endpoint from 'https://reqres.in' to practise sending JSON payloads as per the endpoint's specifications
and test the response received from a POST request.
## Test Step:
- **Required Modules** - requests, json, jsonpath
- **API endpoint** - 'https://reqres.in/api/login'
- **Payload for the API** - {"email":"rakesh@gmail.com"}
- **Response from the API** -
    - {"error":"Missing password"}'
    - status_code - 400
- **Validations** - Validated status_code, error_msg of the response received from the API post request with the expected values.
- **Execution** - To execute this code, import all the packages listed in the Required Modules section and run the file using the IDE.
The expected output will appear in the console.

# Task-2
## Objective:
Write basic automation test script to validate the API response of POST requests with JSON payloads using ROBOT framework with Python.
## Test Step:
- **Required Libraries** - RequestsLibrary, Collections
- **API endpoint** - 'https://reqres.in/api/users'
- **Payload for the API** - {"name":"John","job":"SDET"}
- **Response from the API** -
    - {"name":"John","job":"SDET","id":"296","createdAt":"2024-04-11T07:13:53.019Z"}
    - status_code - 201
- **Validations** - Validated status_code and content of the response received from the API with the expected values using robot framework validations.
- **Execution** -
    - To execute this, download the file or copy the contents of the "test_robot_post_request.robot " file from the "Task_2_robot" folder
      and paste it into a file having ".robot" extension.
    - Place the file in a folder and open a terminal in that folder. To execute, use the command: robot <file_name>.
    - Example: robot test_robot_post_request.robot

# Task-3
## Objective:
Conduct basic load testing on the API endpoint handling POST requests with JSON data using Locust framework.
## Test Step:
- **Required Modules** - HttpUser, task from locust
- **API endpoint** - 'https://reqres.in/api/users'
- **Payload for the API** - {"name":"Rahul","job":"SDET"}
- **UI used** - Locust web UI to test the API under load
- **Execution** -
    - Set up a session using HttpUser, and then execute the code in the terminal with the locust command.
    - To run the Python file, use the command: locust -f <file_name> (Example: locust -f test_load.py).
    - It will establish a local session on a specific port, and the URL will be displayed in the terminal.
    - Click on the link to go to the Locust web UI.
    - Next, we need to choose: a) the number of users, b) the number of users per second (Ramp up), and c) Under Advanced options, specify
      the duration for conducting the test.
    - In the web UI, you can view CHARTS, FAILURES, LOGS and other metrics to check the API's stability under load.
    - After termination, you can view all of this in the console.
    - If you print any messages, they will appear in the console.
    - You can stop the execution manually either in the web UI or by pressing "Ctrl+C" in the console.
