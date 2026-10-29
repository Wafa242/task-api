from app import app
import pytest

@pytest.fixture
def client():
    app.config["TESTING"] = True
    with app.test_client() as client:
        yield client

def test_health_check(client):
    response = client.get("/health")
    assert response.status_code == 200
    assert response.get_json() == {"status": "healthy"}

def test_add_and_get_tasks(client):
    # Test getting initially empty tasks
    response = client.get("/tasks")
    assert response.status_code == 200
    assert response.get_json() == []

    # Test adding a task
    response = client.post("/tasks", json={"title": "Learn Docker and CI/CD"})
    assert response.status_code == 201
    data = response.get_json()
    assert data["title"] == "Learn Docker and CI/CD"
    assert data["completed"] is False

