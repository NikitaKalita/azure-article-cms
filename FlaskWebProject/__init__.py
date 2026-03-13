import os
from flask import Flask
from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

def create_app():
    app = Flask(__name__)

    # Basic Flask config
    app.config['SECRET_KEY'] = os.environ.get("SECRET_KEY", "secret123")
    app.config['FLASK_ENV'] = os.environ.get("FLASK_ENV", "production")

    # Database (SQLite default for safety)
    app.config['SQLALCHEMY_DATABASE_URI'] = os.environ.get(
        "DATABASE_URL",
        "sqlite:///app.db"
    )
    app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

    # Azure Blob config
    app.config['BLOB_CONTAINER'] = os.environ.get("BLOB_CONTAINER", "images")
    app.config['BLOB_CONNECTION_STRING'] = os.environ.get("BLOB_CONNECTION_STRING", "")

    db.init_app(app)

    with app.app_context():
        from FlaskWebProject import views, models
        db.create_all()

    return app


app = create_app()