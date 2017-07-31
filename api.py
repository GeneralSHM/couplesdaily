import configparser
from flask import Flask
from flask_restful import Resource, Api
from resources.user.user import User
from flask.ext.sqlalchemy import SQLAlchemy
from resources.user.model import User

app = Flask(__name__)
api = Api(app)

config = configparser.ConfigParser()
config.read('config.conf')

app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://' + config.get('DB', 'user') + ':' + config.get('DB', 'password') + \
                                        '@' + config.get('DB', 'host') + '/' + config.get('DB', 'db')
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = True

mysql = SQLAlchemy()
class HelloWorld(Resource):
    def get(self):
        print(config)

api.add_resource(HelloWorld, '/')
api.add_resource(User, '/user')

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=4200,debug=True)
