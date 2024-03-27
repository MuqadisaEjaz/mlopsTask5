from flask import Flask, request,jsonify  
from pymongo import MongoClient

app = Flask(__name__)

# MongoDB connection
client = MongoClient("mongodb://localhost:27017")
db = client["mydatabase"]
collection = db["userdata"]

@app.route('/submit', methods=['POST'])
def submit_data():
    data = request.json
    name = data.get('name')
    email = data.get('email')
    print(email)

    # Inserting data into MongoDB
    collection.insert_one({'name': name, 'email': email})

    return 'Data received and stored successfully!'


@app.route('/get', methods=['GET'])
def get_data():
    # Fetching data from MongoDB
    stored_data = collection.find({}, {'_id': 0})  # Exclude _id field from the response

    # Converting MongoDB cursor to a list of dictionaries
    data_list = list(stored_data)

    # Return the stored data as JSON response
    return jsonify(data_list)

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0')
