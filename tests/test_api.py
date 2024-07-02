from utils.api.api_client import APIClient
from utils.api.auth import Auth


def test_api_login(api_client: APIClient):
    auth = Auth(api_client)
    auth.get_dashboard_data()
    pass