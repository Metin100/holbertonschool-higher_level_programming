#!/usr/bin/python3
from flask import Flask, jsonify, request

app = Flask(__name__)

users = {}


@app.route('/')
def home():
    return 'Welcome to the Flask API!'

@app.route('/data')
def data():
    ret_data = list(users)
    return jsonify(ret_data)

@app.route('/add_user', methods="POST")
def add_user():
    data = request.json()
    if data is None or data.get('username') is None:
        return jsonify({'error':'Username is required'}), 400
    user = {
        'username': data.get('username'),
        'age': data.get('age'),
        'name': data.get('name'),
        'city': data.get('city')
    }
    users[user.get('username')] = user
    return jsonify({'message': 'User added', 'user': user}), 201

@app.route('/users/<username>')
def username(username):
    if username is None:
        return jsonify({'error':'Username is not entered'}), 400
    if username not in users:
        return jsonify({'error': "Username can't find in data"}), 404
    return jsonify(users[username])


@app.route('status')
def status():
    return 'OK'

if __name__ == "__main__":
    app.run()