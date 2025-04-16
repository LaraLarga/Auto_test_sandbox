import pytest
import requests


@pytest.mark.user_registration
def test_positive_registration(api_url, fake_data):
    test_data = {
        'username': fake_data['name'],
        'email': fake_data['mail'],
        'password': fake_data['password']
    }

    response = requests.post(url=f'{api_url}/users/', json=test_data)

    assert response.status_code == 201
    assert 'id' in response.json()
    assert response.json()['username'] == test_data['username']
    assert response.json()['email'] == test_data['email']

@pytest.mark.user_registration
def test_registration_one_name(api_url, fake_data):
    test_data = {
        'username': 'q',
        'email': fake_data['mail'],
        'password': fake_data['password']
    }

    response = requests.post(url=f'{api_url}/users/', json=test_data)

    assert response.status_code == 201
    assert 'id' in response.json()
    assert response.json()['username'] == test_data['username']
    assert response.json()['email'] == test_data['email']


# NAME_TEST
def test_registration_max_name(api_url, fake_data):
    test_data = {
        'username': 'q' * 255,
        'email': fake_data['mail'],
        'password': fake_data['password']
    }

    response = requests.post(url=f'{api_url}/users/', json=test_data)

    assert response.status_code == 201
    assert 'id' in response.json()
    assert response.json()['username'] == test_data['username']
    assert response.json()['email'] == test_data['email']


def test_registration_empty_name(api_url, fake_data):
    test_data = {
        'username': '',
        'email': fake_data['mail'],
        'password': fake_data['password']
    }

    response = requests.post(url=f'{api_url}/users/', json=test_data)

    assert response.status_code == 400
    assert response.json()['username'][0] == 'This field may not be blank.'


def test_registration_large_name(api_url, fake_data):
    test_data = {
        'username': 'w' * 256,
        'email': fake_data['mail'],
        'password': fake_data['password']
    }

    response = requests.post(url=f'{api_url}/users/', json=test_data)

    assert response.status_code == 400
    assert response.json()['username'][0] == 'Ensure this field has no more than 255 characters.'


# E-MAIL_TESTS
def test_registration_one_symb_email(api_url, fake_data):
    test_data = {
        'username': fake_data['name'],
        'email': 'p',
        'password': fake_data['password']
    }

    response = requests.post(url=f'{api_url}/users/', json=test_data)

    assert response.status_code == 400
    assert response.json()['email'][0] == 'Enter a valid email address.'


def test_registration_one_one_symb_email(api_url, fake_data):
    test_data = {
        'username': fake_data['name'],
        'email': 'p@p.q',
        'password': fake_data['password']
    }

    response = requests.post(url=f'{api_url}/users/', json=test_data)

    assert response.status_code == 400
    assert response.json()['email'][0] == 'Enter a valid email address.'


def test_registration_space_email(api_url, fake_data):
    test_data = {
        'username': fake_data['name'],
        'email': f"{fake_data['mail'][:-10]} {fake_data['mail'][-10:]}",
        'password': fake_data['password']
    }

    response = requests.post(url=f'{api_url}/users/', json=test_data)

    assert response.status_code == 400
    assert response.json()['email'][0] == 'Enter a valid email address.'


def test_registration_max_email(api_url, fake_data):
    test_data = {
        'username': fake_data['name'],
        'email': f"{fake_data['mail'][:5] * 8}@test.test",
        'password': fake_data['password']
    }

    response = requests.post(url=f'{api_url}/users/', json=test_data)

    assert response.status_code == 201
    assert 'id' in response.json()
    assert response.json()['username'] == test_data['username']
    assert response.json()['email'] == test_data['email']


def test_registration_empty_email(api_url, fake_data):
    test_data = {
        'username': fake_data['name'],
        'email': '',
        'password': fake_data['password']
    }

    response = requests.post(url=f'{api_url}/users/', json=test_data)

    assert response.status_code == 400
    assert response.json()['email'][0] == 'This field may not be blank.'


def test_registration_large_email(api_url, fake_data):
    test_data = {
        'username': fake_data['name'],
        'email': f"{fake_data['mail'][:5] * 10}@test.test",
        'password': fake_data['password']
    }

    response = requests.post(url=f'{api_url}/users/', json=test_data)

    assert response.status_code == 400
    assert response.json()['email'][0] == 'Ensure this field has no more than 50 characters.'


def test_registration_empty_password(api_url, fake_data):
    test_data = {
        'username': fake_data['name'],
        'email': fake_data['mail'],
        'password': ''
    }

    response = requests.post(url=f'{api_url}/users/', json=test_data)

    assert response.status_code == 400
    assert response.json()['password'][0] == 'This field may not be blank.'
