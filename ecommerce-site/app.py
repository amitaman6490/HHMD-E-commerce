from flask import Flask, jsonify, request, make_response, redirect, url_for
from flask_bcrypt import Bcrypt
from flask_cors import CORS
from pymongo import MongoClient
from dotenv import load_dotenv
import os
import jwt
import datetime

app = Flask(__name__)
CORS(app)
bcrypt = Bcrypt()

# Load environment variables
load_dotenv()

# MongoDB connection
client = MongoClient(os.getenv('MONGODB_URI'))
db = client.get_database('ecommerce_db')

# JWT secret key
app.config['SECRET_KEY'] = os.getenv('SECRET_KEY')

# Route to serve the register.html page
@app.route('/register', methods=['GET'])
def register_form():
    return app.send_static_file('register.html')

# Route to handle user registration
@app.route('/api/register', methods=['POST'])
def register():
    hashed_password = bcrypt.generate_password_hash(request.json['password']).decode('utf-8')
    new_user = {
        'username': request.json['username'],
        'email': request.json['email'],
        'password': hashed_password
    }
    db.users.insert_one(new_user)
    return jsonify({'message': 'User registered successfully!'}), 201

# Route to serve the login.html page
@app.route('/login', methods=['GET'])
def login_form():
    return app.send_static_file('login.html')

# Route to handle user login and JWT token generation
@app.route('/api/login', methods=['POST'])
def login():
    user = db.users.find_one({'username': request.json['username']})

    if user and bcrypt.check_password_hash(user['password'], request.json['password']):
        token = jwt.encode({'username': user['username'], 'exp': datetime.datetime.utcnow() + datetime.timedelta(hours=24)}, app.config['SECRET_KEY'])
        return jsonify({'token': token}), 200

    return jsonify({'message': 'Invalid username or password!'}), 401

if __name__ == '__main__':
    app.run(debug=True)
