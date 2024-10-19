#!/usr/bin/python3
from flask import Flask, request, jsonify
from werkzeug.security import generate_password_hash, check_password_hash
from flask_httpauth import HTTPBasicAuth
from flask_jwt_extended import (JWTManager, create_access_token, 
                                jwt_required, get_jwt_identity)

app = Flask(__name__)
auth = HTTPBasicAuth()
app.config['SECRET_KEY'] = 'superincrediblkey'
jwt = JWTManager(app)

users = {
    "Metin": {
        "username": "Metin",
        "password": generate_password_hash("Salam"),
        "role": "user"
    },
    "Eli": {
        "username": "Eli",
        "password": generate_password_hash("Hello"),
        "role": "admin"
    }
}

@auth.verify_password
def verify_password(username, password):
    user = users.get(username)
    if user and \
        check_password_hash(user['password'], password):
        return user


@auth.login_required
@app.route('/basic-protected', methods = ['GET'])
def basic():
    return 'Basic Auth: Access Granted'


@app.route('/login', methods=["POST"])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = verify_password(username, password)

    if user is None:
        return jsonify({'error':'Couldnt find'})
    
    access_token = create_access_token(identity=user)
    return jsonify({'access_token' : access_token})
