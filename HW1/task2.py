import requests
import yaml

with open('config.yaml') as f:
    data = yaml.safe_load(f)


def check_post(token):
    url_post = data["url_post"]
    res_get = requests.get(url=url_post, headers={"X-Auth-Token": token}, params={"owner": "notMe"})
    return res_get.json()


def check_title(token):
    url_post = data["url_post"]
    res_get = requests.get(url=url_post, headers={"X-Auth-Token": token}, params={"owner": "notMe"}).json()
    dat = res_get['data']
    list = []
    for i in range(len(dat)):
        list.append(dat[i]['title'])
    return list


def new_post(token):
    url_post = data["url_post"]
    res_post = requests.post(url=url_post, headers={"X-Auth-Token": token},
                             data={'title': 'New post', 'description': 'iiffk', 'content': 'fhsjhfsj111'})
    return res_post.json()['description']
