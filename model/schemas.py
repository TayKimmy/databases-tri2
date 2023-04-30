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
    _car = db.Column(db.String(255), unique=True, nullable=False)
    _reviews = db.Column(db.String(255), unique=False, nullable=False)
    
    def __init__(self, reviews, car):
        self._car = car
        self._reviews = reviews   

    @property
    def car(self):
        return self._car
    
    @car.setter
    def car(self, car):
        self._car = car
    
    @property
    def reviews(self):
        return self._reviews
    
    @reviews.setter
    def reviews(self, reviews):
        self._reviews = reviews

    def __str__(self):
        return json.dumps(self.read())

    def create(self):
        try:
            db.session.add(self)  
            db.session.commit()  
            return self
        except IntegrityError:
            db.session.remove()
            return None

    # CRUD read converts self to dictionary
    # returns dictionary
    def read(self):
        return {
            "id": self.id,
            "car": self.car,
            "reviews": self.reviews,

        }

    def update(self, car="", reviews=""):
        """only updates values with length"""
        if len(car) > 0:
            self.car = car
        if len(reviews) > 0:
            self.reviews = reviews
        db.session.commit()
        return self

    # CRUD delete: remove self
    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

def initSchemas():
    with app.app_context():
        """Create database and tables"""
        db.create_all()
        """Tester data for table""" 
        u1 = Schemas( car='Tesla Model Y', reviews = "", )
        u2 = Schemas( car='NIO ET7', reviews = "", )
        u3 = Schemas( car='Rivian R1S', reviews = "", )
        u4 = Schemas( car='Lucid Air Grand Touring', reviews = "", )
        u5 = Schemas( car='Tesla Roadster', reviews = "", )

        schemas = [u1, u2, u3, u4, u5]

        """Builds sample user/note(s) data"""
        for schema in schemas:
            try:
                
                schema.create()
            except IntegrityError:
                '''fails with bad or duplicate data'''
                db.session.remove()
                print(f"Records exist, duplicate email, or error:")