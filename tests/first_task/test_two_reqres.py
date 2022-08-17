import requests
import pytest

URL_CREATE_USER = 'https://reqres.in/api/users'

#Второй – создать пользователя (POST https://reqres.in/api/users) с данными из примера на сайте: подготовить тело запроса,
#отправить запрос, получить ответ сервера и проверить, что в ответе те же самые значения, что и в запросе.


@pytest.fixture
def payload():
    payload = {'id': 7,'email': 'emma.charls@reqres.in','first_name':'emma', 'last_name': 'charls', 'avatar': 'https://reqres.in/img/faces/7-image.jpg'}
    return payload

@pytest.fixture
def r_body(payload):
    r = requests.post(URL_CREATE_USER, data=payload)
    r_body = r.json()
    return r_body


def test_all_fields(payload, r_body):
    assert r_body['id'] == payload['id'], f'Invalid id {r_body["id"]} or type is string: {type(r_body["id"])}'
    assert r_body['email'] == payload['email'], 'invalid email'
    assert r_body['first_name'] == payload['first_name'], 'invalid first name'
    assert r_body['last_name'] == payload['last_name'], 'invalid last name'
    assert r_body['avatar'] == payload['avatar'], 'invalid avatar link'