#!/usr/bin/env python3
"""module creates a simple API"""

from flask import Flask
from flask import jsonify
import requests

app = Flask(__name__)

users = {
    "jane": {"name": "Jane", "age": 28, "city": "Los Angeles"},
    "john": {"name": "John", "age": 30, "city": "New York"}
}


@app.route("/")
def home():
    return "<p>Welcome to the Flask API!</p>"


@app.route("/data")
def showdata():
    return jsonify({"usernames": list(users.keys())})


@app.route("/status")
def status():
    return jsonify(message="OK"), 200


@app.route("/users/<username>")
def get_user(username):
    if username in users:
        return jsonify({"users": [username]})
    else:
        return jsonify({"Error": "user not found"}), 404


@app.route("/add_user", methods=["POST"])
def add_user():
    if request.is_json:
        data = request.get_json()
        username = data.get("username")
        if username and username not in users:
            users[username] = {
                "name": data.get("name"),
                "age": data.get("age"),
                "city": data.get("city")
            }
            return jsonify(
                {"message": "User added", "user": users[username]}), 201
        else:
            return jsonify(
                {"error": "Invalid data or user already exists"}), 400
    else:
        return jsonify({"error": "Request must be JSON"}), 400


if __name__ == "__main__":
    app.run()
