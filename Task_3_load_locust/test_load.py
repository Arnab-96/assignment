from locust import HttpUser, task


class ReqResPost(HttpUser):
    host = "https://reqres.in"

    @task
    def create_user(self):
        response = self.client.post("/api/users", data='''{"name":"Rahul","job":"SDET"}''')
        print(response.status_code)
        print(response.text)
        print(response.headers)
