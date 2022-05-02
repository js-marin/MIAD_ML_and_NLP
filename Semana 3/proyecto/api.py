#!/usr/bin/python
from flask import Flask
from flask_restx import Api, Resource, fields
from proyecto_model_deployment import predict_price

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Car Prices Prediction',
    description='Car Prices Prediction')

ns = api.namespace('predict', 
     description='Car Prices Regressor')
   
parser = api.parser()

parser.add_argument(
    'Year', 
    type=int, 
    required=True, 
    help='Year', 
    location='args')

parser.add_argument(
    'Mileage', 
    type=int, 
    required=True, 
    help='Mileage', 
    location='args')

parser.add_argument(
    'State', 
    type=str, 
    required=True, 
    help='State', 
    location='args')

parser.add_argument(
    'Make', 
    type=str, 
    required=True, 
    help='Make', 
    location='args')

parser.add_argument(
    'Model', 
    type=str, 
    required=True, 
    help='Model', 
    location='args')

resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class CarPrices(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result": predict_price(args['Year'], args['Mileage'], args['Model'])
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)
