import pytest
from playwright.sync_api import sync_playwright, Browser

from config.config import Config
from utils.api.api_client import APIClient
from utils.api.auth import Auth


@pytest.fixture(scope="session")
def page():
    with sync_playwright() as p:
        browser = p.chromium.launch(headless=False)
        context = browser.new_context()
        page = context.new_page()
        yield page
        context.close()
        browser.close()

@pytest.fixture(scope="session")
def api_client():
    client = APIClient(Config.API_BASE_URL)
    auth = Auth(client)
    token = auth.login(Config.USERNAME, Config.PASSWORD)
    if not token:
        pytest.exit("Login failed")
    return client
