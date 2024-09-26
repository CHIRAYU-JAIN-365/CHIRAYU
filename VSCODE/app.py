from flask import Flask, request, jsonify
from flask_pymongo import PyMongo
from flask_cors import CORS
from blockchain import Blockchain  # Assuming the blockchain code is in blockchain.py

app = Flask(_name_)
CORS(app)

# MongoDB Configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/healthcare"
mongo = PyMongo(app)

# Initialize Blockchain
blockchain = Blockchain()

@app.route('/add_record', methods=['POST'])
def add_record():
    data = request.json
    patient_id = data.get('patient_id')
    medical_record = data.get('medical_record')

    # Store in MongoDB
    mongo.db.records.insert_one({
        'patient_id': patient_id,
        'medical_record': medical_record
    })

    # Add record to blockchain
    blockchain.add_record({
        'patient_id': patient_id,
        'medical_record': medical_record
    })

    return jsonify({"message": "Record added successfully!"}), 201

@app.route('/get_chain', methods=['GET'])
def get_chain():
    return jsonify(blockchain.get_chain()), 200

@app.route('/records', methods=['GET'])
def get_records():
    records = mongo.db.records.find()
    return jsonify([record for record in records]), 200

if _name_ == '_main_':
    app.run(debug=True)