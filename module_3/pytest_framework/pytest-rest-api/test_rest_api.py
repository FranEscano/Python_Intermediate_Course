import pytest
import requests

def test_get_todo_by_id():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.get(url)

    # Verify status code
    assert response.status_code == 200

    # Verify content-type
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    # Verify response structure
    data = response.json()
    assert isinstance(data, dict)
    assert "id" in data
    assert "title" in data
    assert "userId" in data
    assert "completed" in data

def test_create_book():
    url = "https://jsonplaceholder.typicode.com/todos"
    new_todo = {"userId": 1, "id": 1, "title": "todo1", "completed": False} 
    response = requests.post(url, json=new_todo)

    assert response.status_code == 201
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()
    assert "id" in data
    assert data["title"] == "todo1"
    assert data["completed"] == False

def test_update_book():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    updated_todo = {"title": "NewTodoFromUpdate"}
    response = requests.put(url, json=updated_todo)

    assert response.status_code == 200
    assert response.headers["Content-Type"] == "application/json; charset=utf-8"

    data = response.json()
    assert data["id"] == 1
    assert data["title"] == updated_todo["title"]

def test_delete_book():
    url = "https://jsonplaceholder.typicode.com/todos/1"
    response = requests.delete(url)

    assert response.status_code == 200
    assert response.text == '{}'

@pytest.mark.parametrize("id, status_code", [
    (1, 200),
    (999, 404),
])
def test_get_todos_various_ids(id, status_code):
    url = f"https://jsonplaceholder.typicode.com/todos/{id}"
    response = requests.get(url)
    assert response.status_code == status_code