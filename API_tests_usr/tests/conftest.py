import pytest
from faker import Faker

fake = Faker('en_US')
BASE_URL_BRO = 'http://95.182.122.183'

@pytest.fixture
def fake_data():
    return {
        "name": fake.first_name(),
        "mail": fake.email(domain='test.test'),
        "password": fake.password(length=9) #, special_chars='#%_@*')
    }

@pytest.fixture
def api_url():
    return f'{BASE_URL_BRO}:8000/api/v1'

@pytest.fixture
def uri_token():
    return {
        "token": fake.password(length=15, special_chars='$#*!')
    }
