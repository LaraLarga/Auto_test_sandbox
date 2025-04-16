import pytest, requests

"""DOCUMENTATION
http://84.***.***.53:5000


GET URL/parcels
PUT URL/parcel
Request body:
{
    "city_of_destination": "MSK",
    "city_of_origin": "СПБ",
    "comment": "Some comment",
    "weight": "3.5"
}
POST URL/parcel/<parcel_id>

DELETE URL/parcel/<parcel_id>
"""

@pytest.mark.parametrize("param_to_change, val", [("weight", 21), ("city_of_origin", "NY")])
@pytest.mark.parametrize("param_to_change_2, val_2", [("weight", "NC"), ("city_of_origin", "1234")])
def test_create_upd_del_parcels(fake_data_parcel, api_u, param_to_change, val, param_to_change_2, val_2):
    """Тест на проверку создания, изменения и удаления отправления"""
    put_response = requests.put(
        url=f'{api_u}/parcel',
        json=fake_data_parcel)
    assert put_response.status_code == 201
    assert 'id' in put_response.json()
    ids = put_response.json()['id']
    assert ids in [parcel['id'] for parcel in requests.get(url=f'{api_u}/parcels').json()], f'Expected ID {ids} in Parcels'
    post_resp = requests.post(
        url=f'{api_u}/parcel/{ids}',
        json={param_to_change: val}
    )
    assert post_resp.status_code == 200
    del_response = requests.delete(url=f'{api_u}/parcel/{ids}')
    assert del_response.status_code == 200
    assert ids not in [parcel['id'] for parcel in requests.get(url=f'{api_u}/parcels').json()], f'Expected delete ID {ids} in Parcels'


def test_check_upd_id(fake_data_parcel, api_u):
    """Тест на проверку неизменяемости ID"""
    put_response = requests.put(
        url=f'{api_u}/parcel',
        json=fake_data_parcel)
    assert put_response.status_code == 201
    assert 'id' in put_response.json()
    ids = put_response.json()['id']
    assert ids in [parcel['id'] for parcel in requests.get(url=f'{api_u}/parcels').json()], f'Expected ID {ids} in Parcels'
    post_resp = requests.post(
        url=f'{api_u}/parcel/{ids}',
        json={'id': '1234567890'}
    )
    assert post_resp.status_code == 500
    del_response = requests.delete(url=f'{api_u}/parcel/{ids}')
    assert del_response.status_code == 200
    assert ids not in [parcel['id'] for parcel in requests.get(url=f'{api_u}/parcels').json()], f'Expected delete ID {ids} in Parcels'

