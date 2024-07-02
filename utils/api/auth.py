from utils.api.api_client import APIClient

class Auth:
    def __init__(self, api_client: APIClient):
        self.api_client = api_client

    def login(self, username, password):
        response = self.api_client.post("api/login", json={"email": username, "password": password})
        token = response.get("token")
        if token:
            self.api_client.session.headers.update({"Authorization": f"Bearer {token}"})
        return token

    def get_dashboard_data(self):
        response = self.api_client.get("dashboard")
        return response
