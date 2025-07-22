
from locust import HttpUser, task, between

class ItemUser(HttpUser):
    wait_time = between(1, 3)

    @task(2)
    def list_items(self):
        self.client.get('/items')

    @task(1)
    def create_item(self):
        self.client.post('/items', json={'name': 'LoadTest', 'qty': 1})
