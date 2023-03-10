from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource # used for REST API building
from datetime import datetime

from model.schemas import Schemas

schema_api = Blueprint('car_api', __name__,
                   url_prefix='/api/schemas')

# API docs https://flask-restful.readthedocs.io/en/latest/api.html
api = Api(schema_api)

class SchemasAPI:        
    class _Create(Resource):
        def post(self):
            ''' Read data for json body '''
            body = request.get_json()
            
            ''' Avoid garbage in, error checking '''
            car = body.get('car')
            if car is None or len(car) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            like = body.get('like')
            if like is None:
                return {'message': f'Number of likes are missing, or is less than 2 characters'}, 210
            
            ''' #1: Key code block, setup USER OBJECT '''
            uo = Schemas(car=car,like=like)
            
            ''' Additional garbage error checking '''
            
            ''' #2: Key Code block to add user to database '''
            # create user in database
            schema = uo.create()
            # success returns json of user
            if schema:
                return jsonify(schema.read())
            # failure returns error
            return {'message': f'Processed, either a format error or User ID is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            schemas = Schemas.query.all()    # read/extract all users from database
            json_ready = [schema.read() for schema in schemas]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    
    class _Update(Resource):
        def patch(self):
            body = request.get_json()
            id = body.get('id')
            like = body.get('like')
            uo = Schemas(id=id, like=like)
            schema = uo.update()
            if schema:
                return jsonify(schema.read())

    class _Delete(Resource):
        def delete(self):
            body = request.get_json()
            id = body.get('id')
            uo = Schemas(id=id)
            schema = uo.delete()
            if schema:
                return jsonify(schema.read())

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Update, '/update')
    api.add_resource(_Delete, '/delete')
