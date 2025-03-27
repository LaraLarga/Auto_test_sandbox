import requests, random, pytest
from faker import Faker
import time


fake = Faker('en_US')

BASE_PAGE = 'https://petstore.swagger.io'
PET_NAME = random.choice(['dog', 'cat', 'bird', 'fish', 'shark', 'snake'])
PET_ID = fake.random_int(250, 300)
PET_STAT = 'available'
NEW_STAT = 'reserve'
NEW_NAME = 'Biba'

# @pytest.fixture
# def data_new_post():
#     response = requests.get(f'{BASE_PAGE}/posts')
#     #max_id = max(response.json(), key=lambda item: int(item['id']))['id']
#     return dict(
#         {
#             'user_id': fake.random_int(1, 10),
#             'id': max_id + 1,
#             'title': fake.user_name(),
#             'body': fake.text()
#         })

#func JSON
def create_pet_profile(id, name, stat):
    return dict({"id": id,
      "category": {
        "id": 0,
        "name": "string"
        },
      "name": name,
      "photoUrls": [
        "string"
      ],
      "tags": [
        {
          "id": 0,
          "name": "string"
        }
      ],
      "status": stat
    })

# create and send pets profile with POST
def post_pet(pet_id=PET_ID, pet_name=PET_NAME, pet_stat=PET_STAT):
    return requests.post(
    url=f'{BASE_PAGE}/v2/pet',
    headers={"api_key": "special-key"},
    json=create_pet_profile(pet_id, pet_name, pet_stat)
    ).json()

def put_pet(pet_id=PET_ID, pet_name=PET_NAME, pet_stat=PET_STAT):
    return requests.post(
    url=f'{BASE_PAGE}/v2/pet',
    headers={"api_key": "special-key"},
    json=create_pet_profile(pet_id, pet_name, pet_stat)
    ).json()

def get_pet():
    return requests.get(
        url=f'{BASE_PAGE}/v2/pet/{PET_ID}',
        headers={"api_key": "special-key"}
        )


def test_check_get_create():
    post_response = post_pet()
    time.sleep(10) # change with Wait
    get_resp = get_pet().json()
    assert post_response == get_resp

def test_check_upd():
    put_response = put_pet(pet_name=NEW_NAME, pet_stat=NEW_STAT)
    time.sleep(25) # change with Wait
    get_upd_resp = get_pet().json()
    assert put_response == get_upd_resp

def test_check_del():
    requests.delete(url=f'{BASE_PAGE}/v2/pet/{PET_ID}', headers={"api_key": "special-key"})
    time.sleep(25) # change with Wait
    assert get_pet() != 200

# test_check_get_create()
# test_check_upd()
# test_check_del()