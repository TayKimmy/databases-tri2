from flask import Blueprint, jsonify  # jsonify creates an endpoint response object
from flask_restful import Api, Resource # used for REST API building
import requests  # used for testing 
import random

from model.games import *

game_api = Blueprint('game_api', __name__,
                   url_prefix='/api/game')

api = Api(game_api)

class QuestionsAPI:
    # not implemented
    class _Create(Resource):
        def post(self, car_f):
            pass
            
    # getJokes()
    class _Read(Resource):
        def get(self):
            return jsonify(getgame())

    # getJoke(id)
    class _ReadID(Resource):
        def get(self, id):
            return jsonify(getgame(id))
    
    # getRandomJoke()
    class _ReadCount(Resource):
        def get(self):
            count = countgames()
            countMsg = {'count': count}
            return jsonify(countMsg)

    api.add_resource(_Create, '/create/<string:joke>')
    api.add_resource(_Read, '/')
    api.add_resource(_ReadID, '/<int:id>')
    api.add_resource(_ReadRandom, '/random')
    api.add_resource(_ReadCount, '/count')

if __name__ == "__main__": 
    # server = "http://127.0.0.1:5000" # run local
    server = 'http://127.0.0.1:5000/' # run from web
    url = server + "/api/game"
    responses = []  # responses list

    count_response = requests.get(url+"/count")
    count_json = count_response.json()
    count = count_json['count']

    num = str(random.randint(0, count-1)) # test a random record
    responses.append(
        requests.get(url+"/"+num)  # read joke by id
        ) 
    
    responses.append(
        requests.get(url+"/random")  # read a random joke
        ) 

    # cycle through responses
    for response in responses:
        print(response)
        try:
            print(response.json())
        except:
            print("unknown error")