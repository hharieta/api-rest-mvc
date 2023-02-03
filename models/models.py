"""
SQLAlchemy is a big project and provides a lot of functionality 
to work with databases using Python. One of the features that it provides 
is an object-relational mapper (ORM). This ORM enables you to interact with 
the person database table in a more Pythonic way by mapping a row of fields 
from the database table to a Python object.
"""

from datetime import datetime
from marshmallow_sqlalchemy import fields
from config import db, ma

class Note(db.Model):
    __tablename__ = "note"
    id = db.Column(db.Integer, primary_key=True)
    person_id = db.Column(db.Integer, db.ForeignKey("person.id"))
    content = db.Column(db.String, nullable=False)
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )

# Inheriting from db.Model gives Person the SQLAlchemy features 
# to connect to the database and access its tables
class Person(db.Model):
    __tablename__ = "person"
    id = db.Column(db.Integer, primary_key=True)
    lname = db.Column(db.String(32), unique=True)
    fname = db.Column(db.String(32))

    """
    default=datetime.utcnow parameter defaults the timestamp 
    value to the current utcnow value when a record is created. 
    The onupdate=datetime.utcnow parameter updates the timestamp 
    with the current utcnow value when the record is updated
    """
    timestamp = db.Column(
        db.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow
    )
    notes = db.relationship(
        Note,
        backref = "person",
        cascade = "all, delete, delete-orphan",
        single_parent = True,
        order_by = "desc(Note.timestamp)"
    )


"""
You’re using a database as persistent data storage. 
With SQLAlchemy, you can comfortably communicate with your database 
from within your Python program. However, 
there are two challenges that you need to solve:

1 - Your REST API works with JSON instead of Python objects.
2 - You must make sure that the data that you’re adding to the database is valid.

That’s where the Marshmallow module comes into play!

Marshmallow helps you to create a PersonSchema class, 
which is like the SQLAlchemy Person class you just created. 
The PersonSchema class defines how the attributes of a class 
will be converted into JSON-friendly formats. 
Marshmallow also makes sure that all attributes are present 
and contain the expected data type.
"""

class NoteSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Note
        load_instance = True
        sqla_session = db.session
        include_fk = True


class NoteSchemaPerson(NoteSchema):
    person = fields.Nested("PersonSchema")


class PersonSchema(ma.SQLAlchemyAutoSchema):
    class Meta:
        model = Person
        load_instance = True
        include_relationships = True
        sqla_session = db.session

    """
    Although you’re working with SQLAlchemyAutoSchema, 
    you have to explicitly create the notes field in PersonSchema. 
    Otherwise Marshmallow doesn’t receive all the information 
    it needs to work with the Notes data
    """
    notes = fields.Nested(NoteSchema, many=True)


person_schema = PersonSchema()
note_schema = NoteSchema()
# parameter many=True tells to PersonSchema
# to expect an iterable to serialize
people_schema = PersonSchema(many=True)
note_person_schema = NoteSchemaPerson(many=True)
