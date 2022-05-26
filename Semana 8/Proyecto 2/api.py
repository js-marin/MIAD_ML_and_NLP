from flask import Flask
from flask_restx import Api, Resource, fields
from proyecto_deployment import predict_genre

app = Flask(__name__)

api = Api(
    app, 
    version='1.0', 
    title='Movie Genre Classifier',
    description='Movie Genre Classifier')

ns = api.namespace('predict', 
     description='Movie Genre Classifier')
   
parser = api.parser()

parser.add_argument(
    'plot', 
    type=str, 
    required=True, 
    help='Movie Plot', 
    location='args')


resource_fields = api.model('Resource', {
    'result': fields.String,
})

@ns.route('/')
class GenreClassifier(Resource):

    @api.doc(parser=parser)
    @api.marshal_with(resource_fields)
    def get(self):
        args = parser.parse_args()
        
        return {
         "result": predict_genre(args['plot'])
        }, 200
    
    
if __name__ == '__main__':
    app.run(debug=True, use_reloader=False, host='0.0.0.0', port=8888)
