from flask import Flask
from flask_mysqldb import MySQL

mysql = MySQL()

def init_db(app):
    app.config.from_object("config.Config")
    mysql.init_app(app)
    return mysql
