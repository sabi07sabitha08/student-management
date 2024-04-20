from flask import Flask,jsonify,request
from pymongo import MongoClient
from bson  import ObjectId

app = Flask(__name__)

client = MongoClient("mongodb://localhost:27017/")
db = client['schools']
collection = db['students']

#create
@app.route('/student',methods=['POST'])
def add_item():
    new_item = request.get_json()
    collection.insert_one(new_item) 
    return jsonify({"message":"Data added successfully"})

#read
@app.route('/getstudent/<id>', methods=['GET'])
def getone_student(id):
    sabitha = collection.find_one({'_id':ObjectId(id)})
    if sabitha:
        sabitha['_id'] = str(sabitha['_id'])
        return jsonify(sabitha)
    
#update
@app.route('/student/<id>',methods=['PUT'])
def update_student(id):
    update_student=request.get_json()
    collection.update_one({'_id':ObjectId(id)},{'$set':update_student})
    return jsonify({"message":"Data updated successfully"})

#delete
@app.route('/delete/<id>',methods=['DELETE'])
def delete_student(id):
    collection.delete_one({'_id':ObjectId(id)})
    return jsonify({"message":"Data Deleted Successfully"})

if __name__=='__main__':
    app.run(debug=True)