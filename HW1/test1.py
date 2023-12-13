import pytest

from HW1.task2 import check_title, new_post


# def test_post(get_token):
#     assert get_token in check_post(get_token)['data']

def test_id(get_title, get_token):
    assert get_title in check_title(get_token), 'title отсутствует'


def test_post(get_description, get_token):
    assert get_description in new_post(get_token), 'description отсутствует'

if __name__ == "__main__":
    pytest.main(["-vv"])