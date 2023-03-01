from random import randrange
from datetime import date
import os, base64
import json

from __init__ import app, db
from sqlalchemy.exc import IntegrityError


class Stocks(db.Model):
    __tablename__ = 'Stocks' 

    id = db.Column(db.Integer, primary_key=True)
    _stock = db.Column(db.String(255), unique=True, nullable=False)
    _fact = db.Column(db.String(255), unique=True, nullable=False)
    def __init__(self, stock, fact):
        self._stock = stock   
        self._fact = fact

    @property
    def fact(self):
        return self._fact
    
    @fact.setter
    def chargetime(self, fact):
        self._fact = fact

    @property
    def stock(self):
        return self._stock

    @stock.setter
    def stock(self, stock):
        self._stock = stock

    def __str__(self):
        return json.dumps(self.read())

# CREATE

    def create(self):
        try:
            db.session.add(self)  
            db.session.commit()
            return self
        except IntegrityError:
            db.session.remove()
            return None

# READ

    def read(self):
        return {
            "id": self.id,
            "fact": self.fact,
            "stock": self.stock,
            
        }

# UPDATE

    def update(self, fact="", stock=""):
        if len(fact) > 0:
            self.fact = fact
        if len(stock) > 0:
            self.stock = stock
        db.session.commit()
        return self

# DELETE

    def delete(self):
        db.session.delete(self)
        db.session.commit()
        return None

def initStocks():
    with app.app_context():
        db.create_all()
        u1 = Stocks( fact='Creates your technology products, especially your cell phones', stock='Apple' )
        u2 = Stocks( fact='Creates computers, laptop software, and other products', stock='Microsoft' )
        u3 = Stocks( fact='Creates electric stock', stock='Tesla' )
        u4 = Stocks( fact='Creates American stock', stock='Ford' )
        u5 = Stocks( fact='Creates movies', stock='Disney' )

        stocks = [u1, u2, u3, u4, u5]

        for stock in stocks:
            try:
                stock.create()
            except IntegrityError:
                db.session.remove()
                print(f"Records exist, duplicate email, or error:")

    