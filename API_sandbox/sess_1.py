import requests
from faker import Faker
import pytest

fake = Faker('en_US')

BASE_PAGE = 'https://jsonplaceholder.typicode.com'

@pytest.fixture
def data_new_user():
    response = requests.get(f'{BASE_PAGE}/users')
    max_id = max(response.json(), key=lambda item: int(item['id']))['id']
    print(max_id)
    return dict(
        {'id': max_id + 1,
        'name': fake.name(),
        'username': fake.user_name(),
        'email': fake.email(domain='test.test'),
        'address': {'street': fake.street_name(), 'suite': 'Apt. 556', 'city': fake.city(), 'zipcode': '92998-3874',
                    'geo': {'lat': '-37.3159', 'lng': '81.1496'}}, 'phone': fake.phone_number(),
        'website': 'hildegard.org',
        'company': {'name': 'Romaguera-Crona', 'catchPhrase': 'Multi-layered client-server neural-net',
                    'bs': 'harness real-time e-markets'}})


def test_put_new_user(data_new_user):
    response = requests.post(f'{BASE_PAGE}/users')
    print(response)