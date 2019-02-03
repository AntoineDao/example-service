import pytest
import json


def test_empty_db(client):
    """Start with a blank database."""

    resp = client.get('/example/')
    data = json.loads(resp.data)
    assert data == {'data': []}

def test_post(client):
    resp = client.post('/example/', json={
        'email': 'somerandom@email.com',
        'username': 'myFunkyUser',
        'password': 'secret'
        })
    data = json.loads(resp.data)
    assert data['email'] == 'somerandom@email.com'
    assert data['username'] == 'myFunkyUser'
    assert resp.status_code == 201

def test_headers(client):
    resp = client.post('/example/', json={
        'email': 'somerandom@email.com',
        'username': 'myFunkyUser',
        'password': 'secret'
        },
        headers={
            'stuff': 'things'
        })
    data = json.loads(resp.data)
    assert resp.status_code == 200