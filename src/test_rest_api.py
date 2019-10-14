import requests


def test_get_placeholder():
    """Test REST GET request to placeholder API"""
    response = requests.get("https://jsonplaceholder.typicode.com/todos/1")

    assert response.status_code == 200

    todo = response.json() or {}
    todo_fields = sorted(todo.keys())

    assert todo_fields == [
        'completed',
        'id',
        'title',
        'userId',
    ]
