import requests

from models.posts import Post
from utils.api.api_client import APIClient
from utils.api.auth import Auth


def test_api_login(api_client: APIClient):
    auth = Auth(api_client)
    auth.get_dashboard_data()

def test_api():
    post = Post(1, 101, "Stam", "bar")
    base_url = "https://jsonplaceholder.typicode.com/posts"
    header = {'Content-type': 'application/json; charset=UTF-8'}
    response = requests.post(url=base_url,
                  json=post.to_dict(),
                  headers=header)
    data = response.json()
    post_response = Post(data['user_id'], data['id'], data['title'], data['body'])

    post.title = "Stam something 12321"
    data = requests.put(url=f'{base_url}/{post.user_id}',
                            json=post.to_dict(),
                            headers=header).json()
    put_response = Post(data['user_id'], data['id'], data['title'], data['body'])

    get_user = requests.get(f'{base_url}?userId={post.user_id}')



