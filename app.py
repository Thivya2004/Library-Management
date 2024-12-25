from flask import Flask, request, jsonify
from flask_cors import CORS
from pymongo import MongoClient

app = Flask(__name__)
CORS(app)

# Connect to MongoDB
client = MongoClient('mongodb+srv://nthivya2004:<db_password>@librarycluster.hq64z.mongodb.net/')
db = client['library_db']
users = db['users']
books = db['books']

@app.route('/signup', methods=['POST'])
def signup():
    data = request.json
    if users.find_one({'username': data['username']}):
        return jsonify({'message': 'User already exists'}), 400
    users.insert_one(data)
    return jsonify({'message': 'User created successfully'}), 201

@app.route('/login', methods=['POST'])
def login():
    data = request.json
    user = users.find_one({'username': data['username'], 'password': data['password']})
    if user:
        return jsonify({'message': 'Login successful'}), 200
    return jsonify({'message': 'Invalid credentials'}), 401

@app.route('/books', methods=['GET', 'POST'])
def manage_books():
    if request.method == 'GET':
        book_list = list(books.find({}, {'_id': 0}))
        return jsonify(book_list)
    elif request.method == 'POST':
        data = request.json
        books.insert_one(data)
        return jsonify({'message': 'Book added'}), 201

if __name__ == '__main__':
    app.run(debug=True)
