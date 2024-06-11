from flask import Flask
from flask_cors import CORS
from models import db
from routes.routes import api

# create and setup Flask app
app = Flask(__name__)
# CORS(app)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = False
db.init_app(app)
app.register_blueprint(api)


with app.app_context():
    db.create_all()


if __name__ == "__main__":
    app.run(debug=True)
