# notes.py

from flask import abort, make_response

from config import db
from models import Note, note_schema


def read_one(note_id):
    note = Note.query.get(note_id)

    if note is not None:
        return note_schema.dump(note)
    else:
        abort(404, f"Note with ID {note_id} not found")