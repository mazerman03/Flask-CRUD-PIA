from flask import Flask, render_template
import os
from models.database import init_db
from routes.api import api_bp

template_dir = os.path.join(os.path.dirname(os.path.abspath(__file__)), 'templates')


app = Flask(__name__, template_folder=template_dir)
mysql = init_db(app)
app.register_blueprint(api_bp)


#Rutas 
@app.route('/')
def home():
    
    return render_template('index.html')


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")  # Host 0.0.0.0 should allow Docker access
