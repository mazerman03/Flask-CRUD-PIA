from flask import Blueprint, request, jsonify
from models.database import mysql

api_bp = Blueprint("api", __name__)

@api_bp.route("/items", methods=["GET"])
def get_items():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM items")
    items = cursor.fetchall()
    return jsonify(items)

@api_bp.route("/item", methods=["POST"])
def add_item():
    data = request.get_json()
    name = data['name']
    description = data['description']
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
    mysql.connection.commit()
    return jsonify({"message": "Item added successfully"})

# TODO: Define database table scheme, add DELETE and PUT routes. 
