import json
import jsonpath
import requests

# Api url
url = 'https://reqres.in/api/users'

json_request = json.loads('{"name":"Akash","job":"QA"}')

# make post request with json input body
response = requests.post(url, json_request)
print(response.content)
print(response.status_code)

# parse response to json format
json_response = json.loads(response.content)
print(json_response)

# pick name and job using json path
name = jsonpath.jsonpath(json_response, 'name')[0]
print(name)
job = jsonpath.jsonpath(json_response, 'job')[0]
print(job)

# Validations
assert response.status_code == 201, "Expected and Actual status code is not matching"
assert name == "Akash", "Expected and Actual name is not matching"
assert job == "QA", "Expected and Actual job is not matching"
