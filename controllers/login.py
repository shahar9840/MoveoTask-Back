from db import db
from flask_restful import Resource
from flask import request,jsonify
from datetime import datetime,timedelta
from controllers.users import Users
from flask_jwt_extended import create_access_token,create_refresh_token,jwt_required,get_jwt_identity


class Login(Resource):
    def post(self):
        data = request.get_json()
        username = data.get("username")
        password = data.get("password")
        user = Users.query.filter_by(username=username).first()
        if user and user.password == password:
            access_token = create_access_token(identity=username)
            refresh_token = create_refresh_token(identity=username)
            return {"access_token":access_token,"refresh_token":refresh_token},200
        return {"message":"Invalid username or password"},401

class CheckAuth(Resource):
    @jwt_required()
    def get(self):
        current_user = get_jwt_identity()
        print("current_user",current_user)
        return {"user":current_user},200