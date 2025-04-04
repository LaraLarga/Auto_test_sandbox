from selenium import webdriver
import pytest
from API_petshop.Shopping import PetsShop
import json
from copy import deepcopy


# service = Service(executable_path=ChromeDriverManager.install())
# driver = webdriver.Chrome(service=service)


@pytest.fixture
def browser(request, autouse=True):
    driver = webdriver.Chrome()
    request.cls.driver = driver
    yield
    driver.quit()


@pytest.fixture
def pet_shop(scope='test'):
    petzz = PetsShop()
    yield petzz

@pytest.fixture
def create_pet(pet_shop):
    new_pet = pet_shop.post_pet()
    yield new_pet
    pet_shop.delete_pet(new_pet["id"])
