# people.py

from flask import abort, make_response

from config import db
from models import Person, people_schema, person_schema


def read_all():
    people = Person.query.all()
    return people_schema.dump(people)

def create(person):
    lname = person.get("lname")
    existing = Person.query.filter(Person.lname == lname).one_or_none()

    if not existing:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()
        return person_schema.dump(new_person), 201
    else:
        abort(406, f"Person with last name {lname} already exists")

def read_one(lname):
    person = Person.query.filter(Person.lname == lname).one_or_none()

    if Person:
        return person_schema.dump(person)
    else:
        abort(404, f"Person with last name {lname} not found")

def update(lname, person):
    existing = Person.query.filter(Person.lname == lname).one_or_none()

    if existing:
        update_person = person_schema.load(person, session=db.session)
        existing.fname = update_person.fname
        db.session.merge(existing)
        db.session.commit()
        return person_schema.dump(existing), 201
    else:
        abort(404, f"Person with last name {lname} not found")

def delete(lname):
    existing = Person.query.filter(Person.lname == lname).one_or_none()

    if existing:
        db.session.delete(existing)
        db.session.commit()
        return make_response(f"{lname} successfully deleted"), 200
    else:
        abort(404, f"Person with last name {lname} not found")
