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
            car = body.get('car')
            if car is None or len(car) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            like = body.get('like')
            if like is None:
                return {'message': f'Number of likes are missing, or is less than 2 characters'}, 210
            
            uo = Schemas(car=car, 
                      like=like)
            # create user in database
            schema = uo.create()
            # success returns json of user
            if schema:
                return jsonify(schema.read())
            # failure returns error
            return {'message': f'Processed {car}, either a format error or User ID is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            schemas = Schemas.query.all()    # read/extract all users from database
            json_ready = [schema.read() for schema in schemas]  # prepare output in json
            return jsonify(json_ready)  # jsonify creates Flask response object, more specific to APIs than json.dumps
    
    class _Delete(Resource):
        def delete(self):
            body = request.get_json()
            id = body.get('id')
            schema = Schemas.query.filter_by(id=id).first()
            schema.delete()
            if schema:
                return jsonify(schema.read())
            
    class _Update(Resource):
        def patch(self):
            body = request.get_json()
            id = body.get('id')
            schema = Schemas.query.filter_by(id=id).first()
            try:
                car = body.get('car')
                like = body.get('like')
                schema.update(car=car, like=like)
                return jsonify(schema.read())
            except:
                print(f"error with {id}")

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete')
    api.add_resource(_Update, '/update')