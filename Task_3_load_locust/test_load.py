from locust import HttpUser, constant, task


class MyReqRes(HttpUser):
    host = "https://reqres.in"
    wait_time = constant(1)

    @task
    def get_user(self):
        response = self.client.get("/api/users/2")
        print(response.status_code)
        print(response.text)
        print(response.headers)

    @task
    def create_user(self):
        response = self.client.post("/api/users", data='''{"name":"Rahul","job":"SDET"}''')
        print(response.status_code)
        print(response.text)
        print(response.headers)
