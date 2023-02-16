from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.charges import charges

charge_api = Blueprint('charge_api', __name__,
                   url_prefix='/api/charges')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(charge_api)

class ChargesAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            # validate chargetime
            chargetime = body.get('chargetime')
            if chargetime is None or len(chargetime) < 2:
                return {'message': f'chargetime is missing, or is less than 2 characters'}, 210
            # validate uid
            car = body.get('car')
            if car is None or len(car) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # look for knew and dob

            ''' #1: Key code block, setup USER OBJECT '''
            uo = charges(chargetime=chargetime, 
                      car=car)
            
            ''' Additional garbage error checking '''
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            charge = uo.create()
            # success returns json of user
            if charge:
                return jsonify(charge.read())
            # failure returns error
            return {'message': f'Processed {chargetime}, either a format error or User ID is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            charges = charges.query.all()    # read/extract all users from database
            json_ready = [charge.read() for charge in charges]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')