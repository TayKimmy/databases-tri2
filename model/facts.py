from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Facts(db.Model):
    __tablename__ = 'facts'  # creaated a table for facts in sqlite DB

    # defined the columns for the table --> will use ID as primary key as will be unique
    id = db.Column(db.Integer, primary_key=True)
    _car = db.Column(db.String(255), unique=True, nullable=False)
    _industry = db.Column(db.String(255), unique=False, nullable=False)
    
    # Creating objects in the class to add to the table as rows
    def __init__(self, car, industry):

        self._industry = industry   # self predfix for the object name---> same name as column for better understanding
        self._car = car

    @property # getter for the industry fact about the electric car industry in general 
    def industry(self):
        return self._industry
    
    # a setter function, allows industry fact to be updated after initial object creation helps in the CRUD operations later
    @industry.setter
    def industry(self, industry):
        self._industry = industry

    
# getter for the car or company fact about the companies or cars in the electric car industry in general 
    @property 
    def car(self):
        return self._car
    
    # a setter function, allows car fact to be updated after initial object creation helps in CRUD functions later
    @car.setter
    def car(self, car):
        self._car = car

# This fucntion converts the objects into jason format and outputs jason formatted STRING
    def __str__(self): # 
        return json.dumps(self.read())

## CRUD function 1 --> Create 
    def create(self):
        try:
            # creates a fact and then adds it to the table facts.db through the class Facts
            db.session.add(self)  # prepares to persist fact object to Facts table
            db.session.commit()  # manual commit for SQLAlchemy to work
            return self 
        except IntegrityError: # checking for error and i there is taking "garbage" out. not allowing bad data to come in
            db.session.remove() # manual SQLAlchemy command to remove a created task 
            return None

    # CRUD fucntion 2 --> Read
    def read(self): # converts the table into dictionary with specified keys
        return {
            "id": self.id,
            "industry": self.industry,
            "car": self.car,
            
        }

    # CRUD function 3 --> Update
    
    def update(self, industry="", car=""): # update the industry and car facts
        """only updates values with length"""
        if len(industry) > 0:
            self.industry = industry
        if len(car) > 0:
            self.car = car
        db.session.commit()
        return self

    # CRUD fucntion 4 ---> Delete
    def delete(self): # USed to delete garbage data
        db.session.delete(self)
        db.session.commit()
        return None
    


def initFacts():

    # sample test data
    with app.app_context():
        # create table
        db.create_all()
        # test data to add to created table
        u1 = Facts( industry='Nearly half the EVs in the world are in China.', car='Tesla was originally named after Nikola Tesla, the inventor of alternating current.', )
        u2 = Facts( industry='Roughly 96 percent of EV owners would buy or lease another one', car='Tesla built its Gigafactory 3 in China to produce the Tesla Model 3 and Tesla Model Y for the Chinese market.', )
        u3 = Facts( industry='EVs are more efficient. Up to 80 percent of the battery energy powers the vehicle, compared to 14% to 26 percent of the energy from a gasoline-powered car.', car='Nio has innovative battery swap solutions for charging your EV.', )
        u4 = Facts( industry='Hybrid-Electric Vehicles (HEVs): HEVs combine a gas-powered engine with one (or more) electric motors. An HEV does not plug in; it collects energy through regenerative braking', car='Company name Rivian is inspired from CEO RJ Scaringes time growing up in Florida', )
        u5 = Facts( industry='Battery Electric Vehicles (BEVs): Also known as an all-electric car, it needs to be plugged in to recharge', car='Lucid air manufacturer Lucid motors was previously called Atieva', )

        # using lists to compile all the test cases to check for duplicates and other errors and also adding them as rows if no change
        facts = [u1, u2, u3, u4, u5]

        # check errors and duplicates
        for fact in facts:
            try:
                # Creating the rows 
                fact.create()
            except IntegrityError:
                # fail and print the error if error found
                db.session.remove()
                print("Records exist, duplicate email, or error:")