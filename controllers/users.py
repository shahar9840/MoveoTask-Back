from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask import request
from db import db
from models.users import Users

from werkzeug.security import  generate_password_hash


# create a new user in the database
class CreateUser(Resource):
    def post(self):
        data = request.get_json()
        if data['username']== "shahar":
            data['is_admin'] = True
        data['password'] = generate_password_hash(data['password'])
        new_user = Users(**data)
        db.session.add(new_user)
        db.session.commit()

        return new_user.serialize(), {'message':"user created"}

# get all users from the database
class UserAll(Resource):
    @jwt_required()
    def get(self):
        users = Users.query.all()
        return [user.serialize() for user in users],200

# check if user is admin 
class isAdmin(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = Users.query.filter_by(username=current_user).first()

        return {"is_admin":user.is_admin},200     
# check if user is singer
class isSinger(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = Users.query.filter_by(username=current_user).first()

        return user.instrument == "Singer",200
    
class Check(Resource):
    def get(self):
        return "hello"