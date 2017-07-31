from flask_restful import Resource

class User(Resource):
    def get(self):
        return {'shusha': 'npm lover'}
    def post(self):
        pass

