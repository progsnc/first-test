import pytest
import requests

def tests_get():
    response = requests.get('https://jsonplaceholder.typicode.com/posts')
    user = response.json()[0]
    assert response.status_code == 200, f'Status code is not 200, it is {response.status_code}'
    assert isinstance(response.json(), list), f'Type is not list, it is {response.json()}'
    assert 'userId' in user and 'id' in user and 'title' in user and 'body' in user, f'Item is not in {user}'

def tests_post():
    add_user = {'userId':1,'title':'Qwerty','body':'Zxcvb'}
    response_post = requests.post('https://jsonplaceholder.typicode.com/posts', json=add_user)
    user = response_post.json()
    #response_get = requests.get(f'https://jsonplaceholder.typicode.com/posts/{response_post.json()["id"]}')
    assert response_post.status_code == 201, f'Status code is not 201, it is {response_post.status_code}'
    #assert user == response_get.json(), 'User is not in json'
    assert 'id' in user and user['userId'] == 1 and user['title'] == 'Qwerty' and user['body'] == 'Zxcvb', 'Data does not exist'

def tests_put():
    response_put = requests.put('https://jsonplaceholder.typicode.com/posts/1', data={'userId': 11, 'id':11, 'title': 'QweQwe', 'body': 'RtyRty'})
    user = response_put.json()
    assert  response_put.status_code == 200, f'Status code is not 200, it is {response_put.status_code}'
    assert user['title'] == 'QweQwe' and user['id'] == 1 and user['body'] == 'RtyRty' and 'userId' in user, f'Data has not been updated, {user}'

def tests_delete():
    response_delete = requests.delete('https://jsonplaceholder.typicode.com/posts/1')
    assert response_delete.status_code == 200, f'Status code is not 200, it is {response_delete.status_code}'
