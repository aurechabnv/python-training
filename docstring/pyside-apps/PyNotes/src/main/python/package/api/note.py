from glob import glob
import json
from pathlib import Path
from uuid import uuid4

from package.api.constants import NOTES_DIR

def get_notes():
    notes = []
    files = glob(f"{NOTES_DIR}/*.json")
    for file in files:
        with open(file, "r", encoding="utf-8") as f:
            note_data = json.load(f)
        note_uuid = Path(file).name.split(".")[0]
        note_title, note_content = note_data.get("title"), note_data.get("content")
        note = Note(uuid=note_uuid, title=note_title, content=note_content)
        notes.append(note)
    return notes


class Note:
    def __init__(self, title="", content="", uuid=None):
        if uuid:
            self.uuid = uuid
        else:
            self.uuid = str(uuid4())

        self.title = title
        self.content = content

    def __repr__(self):
        return f"{self.title} ({self.uuid})"

    def __str__(self):
        return self.title

    @property
    def path(self):
        return NOTES_DIR / f"{self.uuid}.json"

    @property
    def content(self):
        return self._content

    @content.setter
    def content(self, value):
        if isinstance(value, str):
            self._content = value
        else:
            raise TypeError("Valeur invalide (besoin d'une chaîne de caractères)")

    def save(self):
        Path(NOTES_DIR).mkdir(parents=True, exist_ok=True)
        data = { "title": self.title, "content": self.content }
        with open(self.path, "w") as f:
            json.dump(data, f, indent=4)

    def delete(self):
        Path(self.path).unlink()
        if Path(self.path).exists():
            return False
        return True


if __name__ == '__main__':
    notes = get_notes()
    print(notes)