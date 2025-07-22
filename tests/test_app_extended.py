import pytest
from app import app, db
from models import Item

@pytest.fixture
def client(tmp_path, monkeypatch):
    # use a temporary SQLite database
    db_file = tmp_path / 'test.db'
    app.config['SQLALCHEMY_DATABASE_URI'] = f'sqlite:///{db_file}'
    with app.test_client() as c:
        with app.app_context():
            db.create_all()
        yield c


def test_get_nonexistent(client):
    resp = client.get('/items/999')
    assert resp.status_code == 404


def test_update_item(client):
    # create
    post = client.post('/items', json={'name': 'Old', 'qty': 1})
    item_id = post.get_json()['id']
    # update
    resp = client.put(f'/items/{item_id}', json={'name': 'New', 'qty': 10})
    data = resp.get_json()
    assert resp.status_code == 200
    assert data['name'] == 'New'
    assert data['qty'] == 10


def test_delete_item(client):
    post = client.post('/items', json={'name': 'ToDelete', 'qty': 2})
    item_id = post.get_json()['id']
    del_resp = client.delete(f'/items/{item_id}')
    assert del_resp.status_code == 204
    get_resp = client.get(f'/items/{item_id}')
    assert get_resp.status_code == 404