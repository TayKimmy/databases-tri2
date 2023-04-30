from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource 
from datetime import datetime

from model.schemas import Schemas

schema_api = Blueprint('car_api', __name__,
                   url_prefix='/api/schemas')

api = Api(schema_api)
 
class SchemasAPI:        
    class _Create(Resource):
        def post(self):
            body = request.get_json()
            car1 = body.get('car')
        #    if car is None or len(car) < 2:
        #        return {'message': f'Car is missing, or is less than 2 characters'}, 210
            reviews1 = body.get('reviews')
        #    if reviews is None:
        #        return {'message': f'Number of reviewss are missing, or is less than 2 characters'}, 210
            
            uo = Schemas(car=car1, 
                      reviews=reviews1)
            schema = uo.create()
            if schema:
                return jsonify(schema.read())
            # failure returns error
            return {'message': f'Processed {car1}, {uo}'}, 210

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
                reviews = body.get('reviews')
                schema.update(car=car, reviews=reviews)
                return jsonify(schema.read())
            except:
                print(f"error with {id}")

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete')
    api.add_resource(_Update, '/update')