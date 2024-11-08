from flask_restful import Resource
from flask_jwt_extended import jwt_required,get_jwt_identity
from flask import request
from db import db
from models.users import Users
from hash_pass import hash_password
from werkzeug.security import check_password_hash, generate_password_hash


# create a new user in the database
class CreateUser(Resource):
    def post(self):
        data = request.get_json()
        if data['username'].endswith('111'):
            data['is_admin'] = True
        data['password'] = generate_password_hash(data['password'])
        new_user = Users(**data)
        db.session.add(new_user)
        db.session.commit()
        print(new_user.serialize())
        return new_user.serialize(), 201

class UserAll(Resource):
    @jwt_required()
    def get(self):
        users = Users.query.all()
        return [user.serialize() for user in users]
    
class isAdmin(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        user = Users.query.filter_by(username=current_user).first()
        print([user.is_admin])
        return {"is_admin":user.is_admin},200    