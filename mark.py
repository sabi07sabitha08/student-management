from flask import Flask,jsonify,request
from pymongo import MongoClient
from bson import ObjectId 



mark = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client['schools']
collection = db['marks']

@mark.route('/marks',methods=['POST'])
def add_mark():
    new_mark = request.get_json()
    collection.insert_one(new_mark) 
    return jsonify({"message":"Data added successfully"})

@mark.route("/getmark/<id>",methods=['GET'])
def getone_mark(id):
    sabitha = collection.find_one({'_id':ObjectId(id)})
    if sabitha:
        sabitha['_id']=str(sabitha['_id'])
        return jsonify(sabitha)

@mark.route("/mark/<id>",methods=['PUT'])
def update_mark(id):
    update_mark=request.get_json()
    collection.update_one({'_id':ObjectId(id)},{'$set':update_mark})
    return jsonify({"message":"Data updated successfully"})

@mark.route("/delete/<id>",methods=['DELETE'])
def delete_mark(id):
    collection.delete_one({'_id':ObjectId(id)})
    return jsonify({"message":"Data deleted successfully"})

if __name__=='__main__':
    mark.run(debug=True) 
    