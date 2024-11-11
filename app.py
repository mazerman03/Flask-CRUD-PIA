from flask import Flask
from models.database import init_db
from routes.api import api_bp

app = Flask(__name__)
mysql = init_db(app)
app.register_blueprint(api_bp)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # Host 0.0.0.0 should allow Docker access
