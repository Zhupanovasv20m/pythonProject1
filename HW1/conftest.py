import pytest
import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)

url_login = data["url_login"]
login = data["login"]
passwd = data["passwd"]
title = data['title']
url_post = data['url_post']


@pytest.fixture
def get_token():
    result = requests.post(url=url_login, data={"username": login, "password": passwd})
    token = result.json()["token"]
    return token


@pytest.fixture
def get_title():
    return title

@pytest.fixture
def get_description():
    return "iiffk"