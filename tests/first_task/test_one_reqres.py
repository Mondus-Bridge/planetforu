import requests
import pytest
import re


URL_GET_LIST_USERS = 'https://reqres.in/api/users?page=2'

#Первый – получить список пользователей (GET https://reqres.in/api/users?page=2) и проверить,
# что все поля пришли, также провалидировать поле email.
@pytest.fixture(autouse=True)
def data():
    r = requests.get(URL_GET_LIST_USERS)
    data = r.json()
    return data


def test_all_fields(data):
    assert data['page'] == 2, f"Invalid page: {data['page']}"
    assert data['per_page'] == 6, f"Invalid per page {['per_page']}"
    assert data['total'] == 12, f"Invalid total page {data['total']}"
    assert data['total_pages'] == 2, f"Invalid total pages {data['total_pages']}"


def test_validate_each_email_in_page(data):
    regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
    for i in data['data']:
        if re.fullmatch(regex, i['email']):
            continue
        assert re.fullmatch(regex, i['email']), "invalid mail"
        # print(f"Invalid email: {i['email']}")