from flask import Flask, jsonify, request
from pymongo import MongoClient
from bson import ObjectId

course = Flask(__name__)

# Connect to MongoDB
client = MongoClient("mongodb://localhost:27017/")
db = client['schools']
collection = db['courses']

# Create
@course.route('/course', methods=['POST'])
def add_course():
    new_course = request.get_json()
    collection.insert_one(new_course)
    return jsonify({"message": "Course added successfully"}) 

#Read
@course.route('/getcourse/<id>',methods=['GET'])
def getone_data(id):
    student = collection.find_one({'_id':ObjectId(id)})
    if student:
        student['_id']=str(student['_id'])
        return jsonify(student)
    
#Update
@course.route("/course/<id>",methods=['PUT'])
def update_course(id):
    update_course=request.get_json()
    collection.update_one({'_id':ObjectId(id)},{'$set':update_course})
    return jsonify({"message":"Data updated successfully"})    

#Delete
@course.route("/delete/<id>",methods=['DELETE'])
def delete_course(id):
    collection.delete_one({'_id':ObjectId(id)})
    return jsonify({"message":"Data deleted successfully"})


if __name__=='__main__':
    course.run(debug=True)