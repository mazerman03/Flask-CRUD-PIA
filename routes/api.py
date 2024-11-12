from flask import Blueprint, request, jsonify
from models.database import mysql

api_bp = Blueprint("api", __name__)

@api_bp.route("/anime", methods=["GET"])
def get_items():
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM anime")
    items = cursor.fetchall()
    return jsonify(items)


#needs to be updated to current table scheme
@api_bp.route("/item", methods=["POST"])
def add_item():
    data = request.get_json()
    name = data['name']
    description = data['description']
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO items (name, description) VALUES (%s, %s)", (name, description))
    mysql.connection.commit()
    return jsonify({"message": "Item added successfully"})

# TODO: with db table scheme update existing routes and add DELETE and PUT routes. 
