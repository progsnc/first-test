import requests
from models import Post


new_post = Post(userId=1, title='Qwerty', body='Zxcvb')
base_url = 'https://jsonplaceholder.typicode.com'

def check_status_code_success(response):
    assert response.status_code == 200, f'Status code is not 200, it is {response.status_code}'

def check_status_code_created(response):
    assert response.status_code == 201, f'Status code is not 201, it is {response.status_code}'

def check_type_list(response):
    assert isinstance(response.json(), list), f'Type is not list, it is {type(response.json())}'

def check_post_struct():
    assert 'userId' in requests.get(f'{base_url}/posts').json()[0] and 'id' in requests.get(f'{base_url}/posts').json()[0] and 'title' in requests.get(f'{base_url}/posts').json()[0] and 'body' in requests.get(f'{base_url}/posts').json()[0], f'Item is not in {requests.get(f"{base_url}/posts").json()[0]}'

def check_post_created(response):
    assert 'id' in response.json() and response.json()['userId'] == new_post.userId and response.json()['title'] == new_post.title and response.json()['body'] == new_post.body, 'Data does not exist'

def check_post_changed(response):
    assert response.json()['title'] == 'Qwerty' and response.json()['body'] == 'Zxcvb' and 'userId' in response.json(), f'Data has not been updated, {response.json()}'