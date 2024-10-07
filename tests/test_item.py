from fastapi.testclient import TestClient

def test_find_all(client_fixture: TestClient):
    response = client_fixture.get("/items")
    assert response.status_code == 200
    items = response.json()
    assert len(items) == 2

def test_find_by_id_normal(client_fixture: TestClient):
    response = client_fixture.get("/items/1")
    assert response.status_code == 200
    item = response.json()
    assert item["id"] == 1

def test_find_by_id_fail(client_fixture: TestClient):
    response = client_fixture.get("/items/10")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_find_by_name(client_fixture: TestClient):
    response = client_fixture.get("/items/?name=PC1")
    assert response.status_code == 200
    item = response.json()
    assert len(item) == 1
    assert item[0] ["name"] == "PC1"

def test_create(client_fixture: TestClient):
    response = client_fixture.post("/items", json={"name": "smartphone", "price": 30000, "user_id": 1})
    assert response.status_code == 201
    item = response.json()
    assert item["id"] == 3
    assert item["name"] == "smartphone"
    assert item["price"] == 30000

    response = client_fixture.get("/items")
    assert len(response.json()) == 3

def test_update_normal(client_fixture: TestClient):
    response = client_fixture.put("/items/1", json={"name": "phone", "price": 5000})
    assert response.status_code == 200
    item = response.json()
    assert item["name"] == "phone"
    assert item["price"] == 5000

def test_update_fail(client_fixture: TestClient):
    response = client_fixture.put("/items/10", json={"name": "phone", "price": 5000})
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"

def test_delete_normal(client_fixture: TestClient):
    response = client_fixture.delete("/items/1")
    assert response.status_code == 202
    response = client_fixture.get("/items")
    assert len(response.json()) == 1

def test_delete_fail(client_fixture: TestClient):
    response = client_fixture.delete("/items/10")
    assert response.status_code == 404
    assert response.json()["detail"] == "Item not found"