from flask import Flask, jsonify
from flask_cors import CORS
from database import collection

app = Flask(__name__)
CORS(app)  # CORS enable kiya

# Home route
@app.route('/')
def home():
    return "Flask API is Running!"

# API endpoint to get data from MongoDB
@app.route('/data', methods=['GET'])
def get_data():
    data = list(collection.find({}, {'_id': 0}))  # `_id` remove kar diya hai JSON response me
    return jsonify(data)

if __name__ == '__main__':
    app.run(debug=True)
