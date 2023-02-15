import threading

# import "packages" from flask
from flask import render_template  # import render_template from "public" flask libraries

# import "packages" from "this" project
from __init__ import app  # Definitions initialization
from model.jokes import initJokes
from model.users import initUsers
from model.rankings import initRankings
from model.generaters import initfact
from model.facts import initFacts
from model.schemas import initSchemas
from model.carbuilderapi import initcarbuilder
from model.leaderboards import initleaderboard

# setup APIs
from api.covid import covid_api # Blueprint import api definition
from api.joke import joke_api # Blueprint import api definition
from api.user import user_api # Blueprint import api definition
from api.ranking import ranking_api
from api.generate import generate_api
from api.fact import fact_api
from api.schema import schema_api
from api.carbuild import build_api
from api.leaderboard import leaderboard_api

# setup App pages
from projects.projects import app_projects # Blueprint directory import projects definition

# register URIs
app.register_blueprint(joke_api) # register api routes
app.register_blueprint(covid_api) # register api routes
app.register_blueprint(user_api) # register api routes
app.register_blueprint(ranking_api)
app.register_blueprint(generate_api)
app.register_blueprint(leaderboard_api)
app.register_blueprint(fact_api)
app.register_blueprint(schema_api)
app.register_blueprint(build_api)
app.register_blueprint(app_projects) # register app pages


@app.errorhandler(404)  # catch for URL not found
def page_not_found(e):
    # note that we set the 404 status explicitly
    return render_template('404.html'), 404

@app.route('/')  # connects default URL to index() function
def index():
    return render_template("index.html")

@app.route('/stub/')  # connects /stub/ URL to stub() function
def stub():
    return render_template("stub.html")

@app.before_first_request
def activate_job():
    initJokes()
    initSchemas()
    initUsers()
    initFacts()


# this runs the application on the development server
if __name__ == "__main__":
    # change name for testing
    from flask_cors import CORS
    cors = CORS(app)
    app.run(debug=True, host="0.0.0.0", port="8086")