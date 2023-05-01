from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime
from model.facts import Facts


fact_api = Blueprint('fact_api', __name__,
                   url_prefix='/api/facts')
api = Api(fact_api)

class FactsAPI:    
## function to display certain data on the frontend, basically get and push all the data
    class _Read(Resource):
        def get(self):
            body = Facts.query.all() 
            json_ready = [fact.read() for fact in body]  
            return jsonify(json_ready) 
## ducntion to create a new row on the database. 
    class _Create(Resource):
        def post(self):
            # request a "get" data from the frontend when the function is run
            body = request.get_json()
            # Delete garbage data. selective processing
            industry = body.get('industry')
            if industry is None or len(industry) < 2:
                return {'message': f'industry is missing, or is less than 2 characters'}, 210
            car = body.get('car')
            if car is None or len(car) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210
            # make the recived data into an object
            uo = Facts(industry=industry, 
                      car=car)
            # .create() defined in the facts file in model directory, creates a row in the database
            fact = uo.create()\
            # if success then print the new data or dict in json format
            if fact:
                return jsonify(fact.read())
            return {'message': f'Processed {industry}, either a format error or User ID is duplicate'}, 210
## fucntion to delete certain data on the database
    class _Delete(Resource):
        def delete(self):
            body = request.get_json()
            id = body.get('id')
            fact = Facts.query.filter_by(id=id).first()
            fact.delete()
            if fact:
                return jsonify(fact.read())
## function to update the database
    class _Update(Resource):
        def patch(self):
            body = request.get_json()
            id = body.get('id')
            fact = Facts.query.filter_by(id=id).first()
            try:
                industry = body.get('industry')
                car = body.get  ('car')
                fact.update(car=car, industry=industry)
                return jsonify(fact.read())
            except:
                print(f"error with {id}")
# endpoing is being built here
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete')
    api.add_resource(_Update, '/update')