

import requests
import yaml

from conftest import url_login, login, passwd

with open('config.yaml') as f:
    data = yaml.safe_load(f)

def get_token():
    result = requests.post(url=url_login, data={"username": login, "password": passwd})
    token = result.json()["token"]
    return token


url_post = data["url_post"]
res_get = requests.get(url=url_post, headers={"X-Auth-Token": get_token()}, params={"owner": "notMe"})
print(res_get.json())

url_post = data["url_post"]
res_post = requests.post(url=url_post, headers={"X-Auth-Token": get_token()},
                         data={'title': 'New post', 'description': 'iiffk', 'content': 'fhsjhfsj111'})
print(res_post.json())
