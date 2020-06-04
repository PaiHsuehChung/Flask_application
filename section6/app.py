from flask import Flask
from flask_restful import Api
from flask_jwt import JWT
from security_login import authenticate, identify
from model.user import UserModel
from resource.item import Item, ItemList
from resource.user import UserRegister
from resource.store import Store, StoreList
from db import db

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///test.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.secret_key = 'Eddie'
api = Api(app)
jwt = JWT(app, authenticate, identify)  #/auth

@app.before_first_request
def create_tables():
    db.create_all()

api.add_resource(StoreList, "/stores")
api.add_resource(Store, "/store/<string:name>")
api.add_resource(Item, "/item/<string:name>")
api.add_resource(ItemList, "/items")
api.add_resource(UserRegister, "/register")

if __name__ == '__main__':
    db.init_app(app)
    app.run()