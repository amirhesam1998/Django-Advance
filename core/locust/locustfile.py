from locust import HttpUser, task, between


class QuickstartUser(HttpUser):
    
    def on_start(self):
        response = self.client.post("/accounts/api/v2/jwt/create/" ,data={
            "email": "admin@admin.com","password": "a/@1234567"}).json()
        
        self.client.headers = {'Authorization': f"Bearer {response.get('access' , None)}"}
    
    @task
    def post_list(self):
        self.client.get("/blog/api/v1/post")
        
    @task
    def category_list(self):
        self.client.get("/blog/api/v1/category")