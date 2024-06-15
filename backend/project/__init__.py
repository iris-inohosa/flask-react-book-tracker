import os
from flask import Flask
from flask_cors import CORS
from flask_sqlalchemy import SQLAlchemy

# -------------
# Configuration
# -------------
db = SQLAlchemy()

# ----------------------------
# Application Factory Function
# ----------------------------


def create_app():
    # Create Flask application
    app = Flask(__name__)

    # configure the Flask app
    config_type = os.getenv("CONFIG_TYPE", default="config.DevelopmentConfig")
    app.config.from_object(config_type)

    init_extensions(app)
    register_blueprints(app)

    with app.app_context():
        db.create_all()

    # -----------------------------------------
    # Test index route to see if app is running
    # -----------------------------------------
    @app.route("/")
    def index():
        return "App is running!"
    return app

# ----------------
# Helper functions
# ----------------


def init_extensions(app):
    db.init_app(app)
    # TODO:
    #   - add LoginManager
    #   - add csrfProtection

def register_blueprints(app):
    from project.books import books_api

    app.register_blueprint(books_api)
    # TODO:
    #   - add user blueprint
