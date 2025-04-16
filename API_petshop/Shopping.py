import json
import requests, random, pytest
from faker import Faker


class PetsShop:
    fake = Faker('en_US')
    BASE_PAGE = 'https://petstore.swagger.io'
    PET_NAME = random.choice(['dog', 'cat', 'bird', 'fish', 'shark', 'snake'])
    PET_ID = fake.random_int(1100, 1200)
    PET_STAT = 'available'
    NEW_STAT = None
    NEW_NAME = None

    def _create_pet_profile(self, pet_id=PET_ID, pet_name=PET_NAME, pet_stat=PET_STAT):
        with open('pet_account_template.json') as file:
            user_data = json.load(file)

        user_data["id"] = pet_id
        user_data["name"] = pet_name
        user_data["status"] = pet_stat

        return user_data


    # create and send pets profile with POST
    def post_pet(self, pet_id=PET_ID, pet_name=PET_NAME, pet_stat=PET_STAT):
        return requests.post(
            url=f'{self.BASE_PAGE}/v2/pet',
            headers={"api_key": "special-key"},
            json=self._create_pet_profile(pet_id, pet_name, pet_stat)
        )

    def put_pet(self, pet_id=PET_ID, pet_name=PET_NAME, pet_stat=PET_STAT):
        return requests.post(
            url=f'{self.BASE_PAGE}/v2/pet',
            headers={"api_key": "special-key"},
            json=self._create_pet_profile(pet_id, pet_name, pet_stat)
        )

    def get_pet(self):
        return requests.get(
            url=f'{self.BASE_PAGE}/v2/pet/{self.PET_ID}',
            headers={"api_key": "special-key"}
            )

    def delete_pet(self):
        return requests.delete(url=f'{self.BASE_PAGE}/v2/pet/{self.PET_ID}', headers={"api_key": "special-key"})


    def create_pet_and_return(self, pet_name=PET_NAME):
        post_resp = self._post_pet(pet_name) #try retry
        assert post_resp.status_code == 200
        try:
            pet_json = post_resp.json()
        except JSONDecodeError as JSON_error:
            print('Error JSON: ')
            raise JSON_error

        assert pet_json['name'] == pet_name
        return pet_json