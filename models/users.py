from db import db 

# create table in the of users in database
class Users(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    password = db.Column(db.String(80), nullable=False)
    name = db.Column(db.String(80), nullable=False)
    is_admin = db.Column(db.Boolean, default=False)
    instrument = db.Column(db.String(80), nullable=False)
    
#present the user in a json format
    def serialize(self):
        return {
            "id": self.id,
            "username": self.username,
            "password": self.password,
            "name": self.name,
            "is_admin": self.is_admin,
            "instrument": self.instrument
        }
    
