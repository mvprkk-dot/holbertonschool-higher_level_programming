#!/usr/bin/python3
""" This module fetches posts from the API and prints them to the console """
from flask import Flask
from flask import jsonify, request

app = Flask(__name__)

# Initialize an empty users dictionary to store user data
users = {}

@app.route('/')
def home():
    """ Home endpoint """
    return "Welcome to the Flask API!"

@app.route('/data')
def data():
    """ Data endpoint """
    return jsonify(list(users.keys()))  # Return a list of usernames

@app.route('/status')
def status():
    """ Status endpoint """
    return "OK"

@app.route("/add_user", methods=["POST"])
def add_user():
    """ Add a new user to the system """
    data = request.get_json()
    
    # Check if username is present in the request data
    if not data or "username" not in data:
        return jsonify({"error": "Username is required"}), 400

    username = data["username"]

    # Log the current users and incoming username for debugging
    print(f"Current users: {users}")
    print(f"Incoming username: {username}")

    # Check if the user already exists
    if username in users:
        return jsonify({"error": "User already exists"}), 400

    # Add the new user
    user_data = {
        "username": username,
        "name": data.get("name"),
        "age": data.get("age"),
        "city": data.get("city"),
    }
    users[username] = user_data

    # Return success message and user data
    return jsonify({
        "message": "User added",
        "user": user_data
    }), 201


@app.route("/users/<username>")
def get_username(username):
    """ Retrieve user information by username """
    if username not in users:
        return jsonify({"error": "User not found"}), 404

    user_info = users[username]

    return jsonify(user_info)

if __name__ == "__main__":
    app.run(debug=True, port=5000)
