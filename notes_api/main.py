from fastapi import FastAPI, HTTPException
from pydantic import BaseModel, Field

class Note(BaseModel):
    id: int = Field(gt=0)
    title: str = Field(min_length=1, max_length=100)
    text: str = Field(max_length=1000, default="")

app = FastAPI()

notes = {1: Note(id = 1, title = "The World After The Fall", text = "Jaehwan"), 2: Note(id = 2, title = "Omniscient Reader's Viewpoint", text = "Kim Dokja")}

@app.get("/notes")
def get_notes() -> list[Note]:
    return list(notes.values())

@app.get("/notes/{note_id}")
def get_note(note_id: int) -> Note:
    if note_id not in notes:
        raise HTTPException(status_code = 404, detail = "Note not found")
    return notes[note_id]

@app.post("/notes", status_code = 201)
def add_note(note: Note) -> Note:
    if note.id in notes:
        raise HTTPException(status_code = 409, detail = "Note already exists")
    notes[note.id] = note
    return note

@app.delete("/notes/{note_id}", status_code = 204)
def del_note(note_id:int) -> None:
    if note_id not in notes:
        raise HTTPException(status_code = 404, detail = "Note not found")
    del notes[note_id]

@app.put("/notes/{note_id}")
def update_note(note_id:int, note: Note) -> Note:
    if note_id not in notes:
        raise HTTPException(status_code = 404, detail = "Note not found")
    if note.id != note_id:
        raise HTTPException(status_code = 400, detail = "ID in body does not match ID in path")
    notes[note.id] = note
    return note