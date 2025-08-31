from locust import HttpUser, task, between

class WebsiteUser(HttpUser):
    wait_time = between(1, 3)  

    @task(3)
    def homepage(self):
        self.client.get("/")  

    @task(1)
    def about_page(self):
        self.client.get("/about") 
