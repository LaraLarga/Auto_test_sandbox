import time


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

# Создание нового питомца и проверка его в БД
def test_create_and_check(pet_shop):
    post_response = pet_shop.post_pet()
    time.sleep(50)  # change with Wait
    get_resp = pet_shop.get_pet().json()
    print(post_response.json())
    assert post_response.status_code == 200
    assert post_response.json() == get_resp


# Изменение Имени и статуса, и проверка изменений в БД
def test_check_upd(pet_shop):
    put_response = pet_shop.put_pet(pet_name='Bonny', pet_stat='reserve')
    time.sleep(40)  # change with Wait
    get_upd_resp = pet_shop.get_pet().json()
    print(put_response.json())
    print(get_upd_resp)
    assert put_response.status_code == 200
    assert put_response.json() == get_upd_resp


def test_check_del(pet_shop):
    pet_shop.delete_pet()
    time.sleep(50)  # change with Wait
    assert pet_shop.get_pet().status_code == 404
