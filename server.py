from flask import Flask
from flask_socketio import emit
from flask_restful import Api, Resource
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from db import db
from controllers.users import CreateUser, Check
from controllers.login import Login, CheckAuth
from controllers.users import isAdmin, isSinger
from hash_pass import hash_password
from socketio_instance import socketio
from controllers.songs import GetSongs
import os

app = Flask(__name__)

# CORS setup
CORS(app, resources={r"/*": {"origins": "*"}})  # Adjust origins as needed

# Database configuration (use environment variable for security)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get('DATABASE_URL', 'sqlite:///db.sqlite3')

# JWT and app secret configuration
app.config['JWT_SECRET_KEY'] = os.environ.get('JWT_SECRET_KEY', 'default_jwt_secret')
app.config['SECRET_KEY'] = os.environ.get('SECRET_KEY', 'default_secret_key')

# Initialize extensions
db.init_app(app)
socketio.init_app(app, cors_allowed_origins="*")  # Adjust as needed
hash_password.init_app(app)
jwt = JWTManager(app)

# Create tables in the database
with app.app_context():
    db.create_all()

# API routes
api = Api(app)
api.add_resource(CreateUser, '/create_user')
api.add_resource(Check, '/')
api.add_resource(CheckAuth, '/check_token')
api.add_resource(Login, '/login')
api.add_resource(isAdmin, '/is_admin')
api.add_resource(GetSongs, '/get_songs')
api.add_resource(isSinger, '/is_singer')

if __name__ == '__main__':
    port = int(os.environ.get("PORT", 5000))
    socketio.run(app, host="0.0.0.0", port=port, debug=True)