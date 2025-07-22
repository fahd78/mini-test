import pytest


# SQL injection payloads
@pytest.mark.parametrize('payload', ["' OR '1'='1", '1; DROP TABLE items;'])
def test_sql_injection(client, payload):
    resp = client.post('/items', json={'name': payload, 'qty': 1})
    # should be sanitized or rejected
    assert resp.status_code in (201, 400)

# XSS payload
def test_xss(client):
    payload = '<script>alert(1)</script>'
    resp = client.post('/items', json={'name': payload, 'qty': 1})
    data = resp.get_json()
    assert '<' not in data['name'] or resp.status_code == 400