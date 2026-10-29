import pytest
from app import app, tasks

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        tasks.clear()
        yield client

def test_health(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_add_and_get_tasks(client):
    res = client.post("/tasks", json={"title": "Test Task"})
    assert res.status_code == 201
    
    res = client.get("/tasks")
    assert res.status_code == 200
    data = res.get_json()
    assert len(data) == 1
    assert data[0]["title"] == "Test Task"

def test_update_task(client):
    client.post("/tasks", json={"title": "Old Title"})
    res = client.put("/tasks/1", json={"title": "New Title", "completed": True})
    assert res.status_code == 200
    data = res.get_json()
    assert data["title"] == "New Title"
    assert data["completed"] is True

def test_delete_task(client):
    client.post("/tasks", json={"title": "To Be Deleted"})
    res = client.delete("/tasks/1")
    assert res.status_code == 200
    
    res = client.get("/tasks")
    assert len(res.get_json()) == 0
