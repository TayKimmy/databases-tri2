from flask import Blueprint, request, jsonify
from flask_restful import Api, Resource 
from datetime import datetime

from model.stocks import Stocks

stock_api = Blueprint('stock_api', __name__,
                   url_prefix='/api/stocks')


api = Api(stock_api)

class StocksAPI:        
    class _Create(Resource):
        def post(self):
            body = request.get_json()
            
            fact = body.get('fact')
            if fact is None or len(fact) < 2:
                return {'message': f'fact is missing, or is less than 2 characters'}, 210
            stock = body.get('car')
            if stock is None or len(stock) < 2:
                return {'message': f'User ID is missing, or is less than 2 characters'}, 210

            uo = Stocks(fact=fact, 
                      stock=stock)
            
            stock = uo.create()
   
            if stock:
                return jsonify(stock.read())
            return {'message': f'Processed {fact}, either a format error or User ID is duplicate'}, 210

    class _Read(Resource):
        def get(self):
            stocks = Stocks.query.all()  
            json_ready = [stock.read() for stock in stocks]  
            return jsonify(json_ready)  

    api.add_resource(_Create, '/create')
    api.add_resource(_Read, '/')