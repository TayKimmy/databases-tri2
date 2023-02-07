from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError

class Schemas(db.Model):
    __tablename__ = 'schema'  # table name is plural, class name is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _car = db.Column(db.String(255), unique=False, nullable=False)
    _like = db.Column(db.Integer, unique=False, nullable=False)
    _dislike = db.Column(db.Integer, unique = False, nullable = False)
    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, like, car, id, dislike):
        self.id = id
        self._car = car
        self._like = like   
        self._dislike = dislike

    @property
    def like(self):
        return self._like
    
    # a setter function, allows name to be updated after initial object creation
    @like.setter
    def like(self, like):
        self._like = like

    @property
    def dislike(self):
        return self._dislike
    
    # a setter function, allows name to be updated after initial object creation
    @dislike.setter
    def dislike(self, dislike):
        self._dislike = dislike

    @property
    def car(self):
        return self._car
    
    # a setter function, allows name to be updated after initial object creation
    @car.setter
    def car(self, car):
        self._name = car

    def __str__(self):
        return json.dumps(self.read())

    def create(self):
        try:
            # creates a person object from User(db.Model) class, passes initializers
            db.session.add(self)  # add prepares to persist person object to Users table
            db.session.commit()  # SqlAlchemy "unit of work pattern" requires a manual commit
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "like": self.like,
            "car": self.car,
            "dislike": self.dislike,
        }

    # CRUD update: updates user name, password, phone
    # returns self
    def update(self, car="", like="", dislike=""):
        """only updates values with length"""
        if len(car) > 0:
            self.car = car
        if len(like) > 0:
            self.like = like
        if len(dislike) > 0:
            self.dislike = dislike
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
"""CRUD DONE"""

def initSchemas():
    """Create database and tables"""
    db.create_all()
    """Tester data for table"""
    u1 = Schemas(id = 1, car='Tesla Model Y', like = 0, dislike = 0)
    u2 = Schemas(id = 2, car='NIO ET7', like = 0, dislike = 0)
    u3 = Schemas(id = 3, car='Rivian R1S', like = 0, dislike = 0)
    u4 = Schemas(id = 4, car='Lucid Air Grand Touring', like = 0, dislike = 0)
    u5 = Schemas(id = 5, car='Tesla Roadster', like = 0, dislike = 0)

    schemas = [u1, u2, u3, u4, u5]

    for schema in schemas:
        try:
            schema.create()
        except IntegrityError:
            db.session.remove()
            print(f"Records exist, duplicate email, or error: {schema.id}")

    """Builds sample user/note(s) data"""