#!/usr/bin/python3
"""
A simple Flask API with user management.
"""
from flask import Flask, jsonify, request


app = Flask(__name__)

# İstifadəçilər yaddaşda (in-memory) saxlanılır
users = {}


@app.route("/")
def home():
    """Welcome message for the root endpoint."""
    return "Welcome to the Flask API!"


@app.route("/data")
def get_data():
    """Returns a list of all stored usernames."""
    return jsonify(list(users.keys()))


@app.route("/status")
def get_status():
    """Returns the API status."""
    return "OK"


@app.route("/users/<username>")
def get_user(username):
    """Returns the full object for a specific username."""
    user = users.get(username)
    if user:
        return jsonify(user)
    return jsonify({"error": "User not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    """Adds a new user to the API."""
    # JSON-un düzgünlüyünü yoxla
    data = request.get_json(silent=True)
    if data is None:
        return jsonify({"error": "Invalid JSON"}), 400

    # Username-in olub-olmamasını yoxla
    username = data.get("username")
    if not username:
        return jsonify({"error": "Username is required"}), 400

    # Username-in artıq mövcud olub-olmamasını yoxla
    if username in users:
        return jsonify({"error": "Username already exists"}), 409

    # İstifadəçini əlavə et
    users[username] = data
    return jsonify({"message": "User added", "user": data}), 201


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
