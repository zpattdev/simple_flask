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

def update(note_id, note):
    existing = Note.query.get(note_id)

    if existing:
        update_note = note_schema.load(note, session=db.session)
        existing.content = update_note.content
        db.session.merge(existing)
        db.session.commit()
        return note_schema.dump(existing)
    else:
        abort(404, f"Note with ID {note_id} not found")

def delete(note_id):
    existing = Note.query.get(note_id)

    if existing:
        db.session.delete(existing)
        db.session.commit()
        return make_response(f"{note_id} successfully deleted", 204)
    else:
        abort(404, f"Note with ID {note_id} not found")