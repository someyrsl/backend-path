from fastapi.testclient import TestClient
from notes_api.main import app

client = TestClient(app)

def test_get_notes():
    response = client.get("/notes")
    assert response.status_code == 200
    notes_list = response.json()
    assert type(notes_list) == list
    for note in notes_list:
        assert "id" in note
        assert "title" in note
        assert "text" in note

def test_get_note_not_found():
    response = client.get("/notes/99")
    assert response.status_code == 404

def test_create_note_invalid_id():
    response = client.post("/notes", json = {"id": 0, "title": "TWATF"})
    assert response.status_code == 422