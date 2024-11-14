from flask import Blueprint, request, jsonify
from models.database import mysql

api_bp = Blueprint("api", __name__)

@api_bp.route("/anime", methods=["GET"])
<<<<<<< HEAD
def get_anime():
=======
def get_items():
>>>>>>> 2ffc60fbc9ad54825868af7e6d9d77e5357d80cb
    cursor = mysql.connection.cursor()
    cursor.execute("SELECT * FROM anime")
    items = cursor.fetchall()
    return jsonify(items)

<<<<<<< HEAD
#Add anime into the DB
@api_bp.route("/anime", methods=["POST"])
def add_anime():
    data = request.get_json()
    title = data['title']
    episodes = data['episodes']
    genre = data['genre']
    cursor = mysql.connection.cursor()
    cursor.execute("INSERT INTO anime (title, episodes, genre) VALUES (%s, %s, %s)", (title, int(episodes), genre))
    mysql.connection.commit()
    return jsonify({"message": "Anime added successfully"})

#Update anime into the DB
@api_bp.route("/anime/<int:id>", methods=["PUT"])
def update_anime(id):
    data = request.get_json()
    title = data['title']
    episodes = data['episodes']
    genre = data['genre']
    cursor = mysql.connection.cursor()
    cursor.execute("UPDATE anime SET title = %s, episodes = %s, genre = %s WHERE id = %s", (title, episodes, genre, id))
    mysql.connection.commit()
    return jsonify({"message": "Anime updated successfully"})

#Delete anime with id from the DB
@api_bp.route("/anime/<int:id>", methods=["DELETE"])
def delete_anime(id):
    cursor = mysql.connection.cursor()
    cursor.execute("DELETE FROM anime WHERE id = %s", (id,))
    mysql.connection.commit()

    if cursor.rowcount == 0:
        return jsonify({"message": "Anime not found"})
    
    return jsonify({"message": "Anime deleted successfully"})

=======

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
>>>>>>> 2ffc60fbc9ad54825868af7e6d9d77e5357d80cb
