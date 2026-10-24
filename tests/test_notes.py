from fastapi.testclient import TestClient
from notes_api.main import app, notes, Note
import pytest

client = TestClient(app)

@pytest.fixture(autouse = True)
def reset_notes():
    notes.clear()
    notes.update({1: Note(id = 1, title = "The World After The Fall", text = "Jaehwan"), 2: Note(id = 2, title = "Omniscient Reader's Viewpoint", text = "Kim Dokja")})

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

def test_create_note_with_same_id():
    response = client.post("/notes", json = {"id": 4, "title":"BS"})
    assert response.status_code == 201
    another_post = client.post("/notes", json = {"id":4, "title": "BS2"})
    assert another_post.status_code == 409