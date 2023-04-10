from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource
from datetime import datetime

from model.facts import Facts

fact_api = Blueprint('fact_api', __name__,
                   url_prefix='/api/facts')


api = Api(fact_api)

class FactsAPI:        
    class _Create(Resource):
        def post(self):
            # get the data from frontend site
            body = request.get_json()
            
            # Avoid the data that is not correct
            industry = body.get('industry')
            if industry is None or len(industry) < 2:
                return {'message': f'industry is missing, or is less than 2 characters'}, 210
            car = body.get('car')
            if car is None or len(car) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210

            # set up the object
            uo = Facts(industry=industry, 
                      car=car)
            
            # .create creates the user in the database
            fact = uo.create()
            if fact:
                return jsonify(fact.read())
            return {'message': f'Processed {industry}, either a format error or User ID is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            facts = Facts.query.all() 
            json_ready = [fact.read() for fact in facts]  
            return jsonify(json_ready)  
        
    class _Delete(Resource):
        def delete(self):
            body = request.get_json()
            id = body.get('id')
            fact = Facts.query.filter_by(id=id).first()
            fact.delete()
            if fact:
                return jsonify(fact.read())

    # building RESTapi endpoint
    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')
    api.add_resource(_Delete, '/delete')