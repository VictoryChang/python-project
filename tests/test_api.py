def test_health(client):
    response = client.get_health()
    assert response.status_code == 200
    assert response.json() == {"status": "healthy"}


def test_sum(client):
    response = client.get_sum(a=1, b=2)
    assert response.status_code == 200
    assert response.json() == {"result": 3}


def test_double_sum(client):
    response = client.get_double_sum(a=1, b=2)
    assert response.status_code == 200
    assert response.json() == {"result": 6}
