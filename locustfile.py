from locust import HttpUser as HUser, between, task


class HttpUser(HUser):
    """
    This is a simple Locust test script that simulates user behavior on a website.
    """

    wait_time = between(0.5, 10)

    @task(3)
    def login(self):
        self.wait_time = 5
        self.client.post("/login")

    @task
    def profile(self):
        self.client.post("/profile")
