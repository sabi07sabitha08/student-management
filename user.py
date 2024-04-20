from flask import Flask,jsonify,request
from pymongo import MongoClient
from bson import ObjectId 



user = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client['user']
collection = db['reglog']


#Login
@user.route('/user', methods=['POST'])
def add_login():
    data = request.get_json()
    username= data.get('username')
    password = data.get('password')
    
    if not username or not password:
        return jsonify({"Error":"username and password are required"})
    
    if collection.username.find_one({"username":username}):
        return jsonify({"Error":"Username is already exists"})
    
    if collection.username.insert_one({"username":username, "password":password}):
        return jsonify({"message":"user registered successfully"})
       

if __name__=='__main__':
    user.run(debug=True)