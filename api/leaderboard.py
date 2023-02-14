from flask import Blueprint, jsonify
from flask_restful import Api, Resource
import json

from model.leaderboards import *

leaderboard_api = Blueprint('leaderboard_api', __name__, url_prefix='/api/leaderboard')

api = Api(leaderboard_api)

class LeaderboardAPI:
    class _Create(Resource):
        def post(self, user, score):
            addScore(user, score)
            return jsonify(getLeaderboard())

    class _Read(Resource):
        def get(self):
            return jsonify(getLeaderboard())

    # building RESTapi resources/interfaces, these routes are added to Web Server
    api.add_resource(_Create, '/create/<string:user>/<int:score>')
    api.add_resource(_Read, '/')

if __name__ == "__main__":
    initleaderboard()
    print(json.dumps(getLeaderboard(), indent=4))
