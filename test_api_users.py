import pytest
import requests
from models import Post
from asserts import *


base_url = 'https://jsonplaceholder.typicode.com'
new_post = Post(userId=1, title='Qwerty', body='Zxcvb')

def test_get():
    response_get = requests.get(f'{base_url}/posts')
    check_status_code_success(response_get)
    check_type_list(response_get)
    check_post_struct(response_get)

def test_post():
    response_post = requests.post(f'{base_url}/posts', json=new_post.model_dump())
    check_status_code_created(response_post)
    check_post_created(response_post, new_post)

def test_put():
    response_put = requests.put(f'{base_url}/posts/1', data=new_post.model_dump())
    check_status_code_success(response_put)
    check_post_changed(response_put)

def test_delete():
    response_delete = requests.delete(f'{base_url}/posts/1')
    check_status_code_success(response_delete)
