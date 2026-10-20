from dataclasses import asdict, dataclass,field
import json

@dataclass
class Note:
    id: int
    title: str
    text: str = ""
    tags: list[str] = field(default_factory=list)

notes = [
    Note(1, "Первая", "текст", ["python"]),
    Note(2, "Вторая"),
    Note(3, "Третья", tags=["a", "b"]),
]

with open("notes.json", "w", encoding = "utf-8") as f:
    json.dump([asdict(n) for n in notes], f, ensure_ascii = False, indent = 2)

with open("notes.json", "r", encoding = "utf-8") as f:
    loaded_data = json.load(f)

loaded = [Note(**d) for d in loaded_data]

