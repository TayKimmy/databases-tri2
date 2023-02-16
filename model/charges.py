from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Charges(db.Model):
    __tablechargetime__ = 'Charges'  # table chargetime is plural, class chargetime is singular

    # Define the User schema with "vars" from object
    id = db.Column(db.Integer, primary_key=True)
    _car = db.Column(db.String(255), unique=False, nullable=False)
    _chargetime = db.Column(db.String(255), unique=False, nullable=False)
    # Defines a relationship between User record and Notes table, one-to-many (one user to many notes)
    # constructor of a User object, initializes the instance variables within object (self)
    def __init__(self, car, chargetime):

        self._chargetime = chargetime   # variables with self prefix become part of the object, 
        self._car = car

    @property
    def chargetime(self):
        return self._chargetime
    
    # a setter function, allows chargetime to be updated after initial object creation
    @chargetime.setter
    def chargetime(self, chargetime):
        self._chargetime = chargetime

    

    @property
    def car(self):
        return self._car
    
    # a setter function, allows chargetime to be updated after initial object creation
    @car.setter
    def chargetime(self, car):
        self._car = car

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
            "chargetime": self.chargetime,
            "car": self.car,
            
        }

    # CRUD update: updates user chargetime, knew, phone
    # returns self
    def update(self, chargetime="", car=""):
        """only updates values with length"""
        if len(chargetime) > 0:
            self.chargetime = chargetime
        if len(car) > 0:
            self.car = car
        db.session.commit()
        return self

    # CRUD delete: remove self
    # None
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None
"""CRUD DONE"""

def initCharges():
    with app.app_context():
        """Create database and tables"""
        db.init_app(app)
        db.create_all()
        u1 = Charges( chargetime='Around 10 Hours', car='Lucid Air' )
        u2 = Charges( chargetime='Around 7 Hours', car='Tesla Model X' )
        u3 = Charges( chargetime='Around 7 Hours', car='Tesla Model S' )
        u4 = Charges( chargetime='Around 18 Hours', car='Rivian R1T' )
        u5 = Charges( chargetime='Around 11 Hours', car='NIO ET5' )

        Charges = [u1, u2, u3, u4, u5]

        for fact in Charges:
            try:
                '''add a few 1 to 4 notes per user'''
              
                '''add user/post data to table'''
                fact.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error: {fact.uid}")

    """Builds sample user/note(s) data"""
    