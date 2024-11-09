from flask import Flask
from flask_socketio import emit
from flask_restful import Api,Resource
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from db import db
from controllers.users import CreateUser
from controllers.login import Login 
from controllers.login import CheckAuth
from controllers.users import isAdmin,isSinger
from hash_pass import hash_password
from socketio_instance import socketio  
from controllers.songs import GetSongs



app = Flask(__name__)

# connect the server to database
CORS(app, resources={r"/*": {"origins": "https://moveo-task-front-ly6e02p9l-shahars-projects-d7a43d16.vercel.app"}})
app.config['SQLALCHEMY_DATABASE_URI'] = 'mysql://root:OfszSEcPnycLQiTGJWxLVgFwloynFJmf@autorack.proxy.rlwy.net:24126/railway'
db.init_app(app)
app.config['JWT_SECRET_KEY'] = 'kmfksdfkv;l3mkf4l4fl3'
app.config['SECRET_KEY']='kmfksdfkv;l3mkf4l4fl3'
socketio.init_app(app, cors_allowed_origins="https://moveo-task-front-ly6e02p9l-shahars-projects-d7a43d16.vercel.app")

#connect the server to api manager
api = Api(app)
hash_password.init_app(app)

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
api.add_resource(GetSongs,'/get_songs')
api.add_resource(isSinger,'/is_singer')

if __name__ == '__main__':
    socketio.run(app, debug=True)