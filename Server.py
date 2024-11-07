from flask import Flask
from flask_restful import Api,Resource
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from db import db
from controllers.users import CreateUser
from controllers.login import Login 
from controllers.login import CheckAuth
from controllers.users import isAdmin





app = Flask(__name__)

# connect the server to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)
app.config['JWT_SECRET_KEY'] = 'kmfksdfkv;l3mkf4l4fl3'
app.config['SECRET_KEY']='kmfksdfkv;l3mkf4l4fl3'
#connect the server to api manager
api = Api(app)
CORS(app, resources={r"/*": {"origins": ["http://localhost:3000"]}})

#configure token manager
jwt = JWTManager(app)

# create tables in the database
with app.app_context():
    db.create_all()


#routes
api.add_resource(CreateUser, '/create_user')
api.add_resource(CheckAuth,'/check_token')
api.add_resource(Login, '/login')
api.add_resource(isAdmin,'/is_admin')


if __name__ == '__main__':
    app.run(debug=True,port=50000,host='0.0.0.0')