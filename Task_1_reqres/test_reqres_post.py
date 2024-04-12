import json
import jsonpath
import requests

# Api url
url = 'https://reqres.in/api/login'

json_request = json.loads('{"email":"rakesh@gmail.com"}')

# make post request with json input body
response = requests.post(url, json_request)
print(response.content)
print(response.status_code)

# parse response to json format
json_response = json.loads(response.content)
print(json_response)

# pick error message json path
error_msg = jsonpath.jsonpath(json_response, 'error')[0]
print(error_msg)

# Validations
assert response.status_code == 400, "Expected and Actual status code is not matching"
assert error_msg == "Missing password", "Expected and Actual error message is not matching"
