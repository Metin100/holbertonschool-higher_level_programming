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
    
    return None

@auth.login_required
@app.route('/basic-protected', methods=['GET'])
def basic():
    return 'Basic Auth: Access Granted'

@app.route('/login', methods=["POST"])
def login():
    username = request.json.get('username')
    password = request.json.get('password')

    user = verify_password(username, password)

    if user is None:
        return jsonify({'error': 'user does not find'}), 401
    
    access_token = create_access_token(identity=user["username"])
    return jsonify({'token': access_token})

@app.route('/jwt-protected', methods=['GET'])
@jwt_required()
def protected():
    return "JWT Auth: Access Granted"

@app.route('/admin-only', methods=['GET'])
@jwt_required()
def admin_only():
    current_user = get_jwt_identity()
    if current_user['role'] != 'admin':
        return jsonify({'error': 'role is not admin'}), 403
    return jsonify({'Admin Access: Granted'}), 200


@jwt.unauthorized_loader
def handle_unauthorized_error(err):
    return jsonify({"error": "Missing or invalid token"}), 401

@jwt.invalid_token_loader
def handle_invalid_token_error(err):
    return jsonify({"error": "Invalid token"}), 401

@jwt.expired_token_loader
def handle_expired_token_error(err):
    return jsonify({"error": "Token has expired"}), 401

@jwt.revoked_token_loader
def handle_revoked_token_error(err):
    return jsonify({"error": "Token has been revoked"}), 401

@jwt.needs_fresh_token_loader
def handle_needs_fresh_token_error(err):
    return jsonify({"error": "Fresh token required"}), 401

if __name__ is "__main__":
    app.run()