from flask import Flask
from flask_restful import Api,Resource
from flask_cors import CORS
from flask_jwt_extended import JWTManager
from db import db






app = Flask(__name__)

# connect the server to database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///data.db'
db.init_app(app)

app.config['SECRET_KEY']='kmfksdfkv;l3mkf4l4fl3'
#connect the server to api manager
api = Api(app)
CORS(app,resources={r"/*": {"origins": "*"}})

#configure token manager
jwt = JWTManager(app)

# create tables in the database
with app.app_context():
    db.create_all()


#routes
# api.add_resource(Store, '/store/<string:name>')
# api.add_resource(Item, '/item/<string:name>')
# api.add_resource(ItemList, '/items')
# api.add_resource(StoreList, '/stores')
# api.add_resource(UserRegister, '/register')


if __name__ == '__main__':
    app.run(debug=True,port=5000,host='0.0.0.0')