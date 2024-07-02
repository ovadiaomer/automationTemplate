import requests


class APIClient:
    def __init__(self, base_url):
        self.base_url = base_url
        self.session = requests.Session()

    def get(self, endpoint, params=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.get(url, params=params, headers=headers)
        response.raise_for_status()
        return response.json()

    def post(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.post(url, data=data, json=json, headers=headers)
        response.raise_for_status()
        return response.json()

    def put(self, endpoint, data=None, json=None, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.put(url, data=data, json=json, headers=headers)
        response.raise_for_status()
        return response.json()

    def delete(self, endpoint, headers=None):
        url = f"{self.base_url}/{endpoint}"
        response = self.session.delete(url, headers=headers)
        response.raise_for_status()
        return response.json()
