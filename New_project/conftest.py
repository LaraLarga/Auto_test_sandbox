from faker import Faker
import pytest

fake = Faker('en_US')
BASE_URL = 'http://84.***.***.53:5000'

@pytest.fixture
def fake_data_parcel():
    test_data = {
        "weight": fake.random_number(),
        "city_of_destination": fake.city(),
        "city_of_origin": fake.city(),
        "comment": "Handle with care"
    }
    return test_data

@pytest.fixture
def api_u():
    return BASE_URL