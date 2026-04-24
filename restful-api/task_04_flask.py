#!/usr/bin/python3
"""
This module contains a simple Flask API with several endpoints to manage
users, check status, and retrieve specific data. It demonstrates basic
RESTful API functionalities using Python and Flask.
"""
from flask import Flask, jsonify, request

app = Flask(__name__)

# users is a dictionary used to store user information in memory
# where the key is the username and the value is a dictionary of user details
users = {}


@app.route('/')
def home():
    """
    Home endpoint that returns a simple greeting message to the user
    when they access the root URL of the Flask application.
    """
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """
    Data endpoint that returns a list of all usernames currently stored
    in the users dictionary as a JSON array.
    """
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """
    Status endpoint that returns a string 'OK' to indicate that the API
    is currently running and healthy for monitoring purposes.
    """
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """
    Retrieve user information based on a provided username. If the user
    exists in the dictionary, return their details; otherwise, return a 404.
    """
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route('/add_user', methods=['POST'])
def add_user():
    """
    Add a new user to the users dictionary based on the JSON payload
    sent in the request. Validates that a username is provided and
    checks for duplicates before adding.
    """
    data = request.get_json()
    if not data or 'username' not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data.get('username')
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    users[username] = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city")
    }
    return jsonify({"message": "User added", "user": users[username]}), 201


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000, debug=True)
