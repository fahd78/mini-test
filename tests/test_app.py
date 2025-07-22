
import pytest



def test_create_item(client):
    resp = client.post('/items', json={'name': 'Widget', 'qty': 5})
    assert resp.status_code == 201
    data = resp.get_json()
    assert data['id'] == 1
    assert data['name'] == 'Widget'


def test_list_items(client):
    # create another item
    client.post('/items', json={'name': 'Gadget', 'qty': 2})
    resp = client.get('/items')
    assert resp.status_code == 200
    data = resp.get_json()
    assert isinstance(data, list)
    assert any(item['name'] == 'Gadget' for item in data)