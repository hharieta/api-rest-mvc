#from datetime import datetime
from flask import abort, make_response
from config import db
from models.models import Person, person_schema, people_schema

# /people GET
def read_all():
    # people variable contains a list of database items.
    people = Person.query.all()
    # serialize the Python objects with .dump() 
    # and return the data of all the people as 
    # a response to the REST API call.
    return people_schema.dump(people)


# /people/{lname} GET
def read_one(lname):
    person = Person.query.filter(Person.lname == lname).one_or_none()

    # If a person is found, then person contains a Person object 
    # and you return the serialized object
    if person is not None:
        return person_schema.dump(person)
    else:
        abort(
            404, f'Person with last name {lname} not found'
        )


# /people POST
def create(person):
    lname = person.get("lname")
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person is None:
        new_person = person_schema.load(person, session=db.session)
        db.session.add(new_person)
        db.session.commit()

        return person_schema.dump(new_person), 201
    else:
        abort(
            406,
            f'Person with last name {lname} already exists',
        )

# /people/{lname} PUT
def update(lname, person):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        update_person = person_schema.load(person, session=db.session)
        existing_person.fname = update_person.fname
        existing_person.lname = update_person.lname
        db.session.merge(existing_person)
        db.session.commit()
        
        return person_schema.dump(existing_person), 201 
    else:
        abort(
            404,
            f'Person with last name {lname} not found'
        )


# /people/{lname} DELETE
def delete(lname):
    existing_person = Person.query.filter(Person.lname == lname).one_or_none()

    if existing_person:
        db.session.delete(existing_person)
        db.session.commit()

        return make_response(
            f'{lname} succesfully deleted', 200
        )
    else:
        abort(
            404,
            f'Person with last name {lname} not found'
        )