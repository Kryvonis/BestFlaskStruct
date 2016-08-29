from flask_pymongo import PyMongo
from flask import jsonify
import json
from app import app
mongo = PyMongo(app)

def create_user():
    print(mongo)
    user = {"name":"Kolya"}
    users = [user for _ in range(5)]
    return mongo.db.users.insert({"users":json.dumps(users)})