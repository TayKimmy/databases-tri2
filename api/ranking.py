from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model.rankings import *

ranking_api = Blueprint('ranking_api', __name__,
                   url_prefix='/api/rankings')

api = Api(ranking_api)

class RankingAPI:
    class _Create(Resource):
        def post(self, car):
            pass
            
    class _Read(Resource):
        def get(self):
            return jsonify(getCars())

    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getCar(id))

    class _ReadRandom(Resource):
        def get(self):
            return jsonify(getRandomCar())
    
    class _ReadCount(Resource):
        def get(self):
            count = countCars()
            countMsg = {'count': count}
            return jsonify(countMsg)

    class _UpdateLike(Resource):
        def put(self, id):
            addCarLike(id)
            return jsonify(getCar(id))

    class _UpdateDislike(Resource):
        def put(self, id):
            addCarDislike(id)
            return jsonify(getCar(id))

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create/<string:car>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')
    api.add_resource(_UpdateLike, '/like/<int:id>')
    api.add_resource(_UpdateDislike, '/dislike/<int:id>')
    
if __name__ == "__main__": 
    server = "http://172.21.215.122:8086" # run local
    url = server + "/api/rankings"
    responses = []  # responses list

    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    # update likes/dislikes test sequence
    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num) 
        ) 
    responses.append(
        requests.put(url+"/like/"+num) 
        ) 
    responses.append(
        requests.put(url+"/dislike/"+num) 
        ) 

    responses.append(
        requests.get(url+"/random")  
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")