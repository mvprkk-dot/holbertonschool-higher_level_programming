#!/usr/bin/python3
"""Simple Flask API for user management."""
from flask import Flask, jsonify, request

app = Flask(__name__)
users = {}


@app.route('/')
def home():
    """Root endpoint."""
    return "Welcome to the Flask API!"


@app.route('/data')
def data():
    """List all usernames."""
    return jsonify(list(users.keys()))


@app.route('/status')
def status():
    """API status check."""
    return "OK"


@app.route('/users/<username>')
def get_user(username):
    """Retrieve user by username."""
    user = users.get(username)
    if not user:
        return jsonify({"error": "User not found"}), 404
    return jsonify(user)


@app.route('/add_user', methods=['POST'])
def add_user():
    """Add a new user."""
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
