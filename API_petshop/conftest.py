from selenium import webdriver
import pytest, time
from API_petshop.Shopping import PetsShop
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


@pytest.fixture
def check_pet_get_time(pet_shop, timeout=120, check_interval=10):
    start_time = time.time()
    while time.time() - start_time < timeout:
        print()
        print(pet_shop.get_pet().status_code)
        if pet_shop.get_pet().status_code == 200:
            return True
        time.sleep(check_interval)
    return False

@pytest.fixture
def check_pet_get_attempt(pet_shop, timeout=30, attempt=5):
    while attempt != 0:
        print()
        print(pet_shop.get_pet().status_code)
        if pet_shop.get_pet().status_code == 200:
            return True
        time.sleep(timeout)
        attempt -= 1
    return False

@pytest.fixture
def check_pet_del(pet_shop, timeout=30, attempt=10):
    while attempt != 0:
        print()
        print(pet_shop.get_pet().status_code)
        if pet_shop.get_pet().status_code == 400:
            return True
        time.sleep(timeout)
        attempt -= 1
    return False
