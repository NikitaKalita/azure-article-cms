import os

class Config:
    # Flask
    SECRET_KEY = os.environ.get("SECRET_KEY", "secret123")
    FLASK_ENV = os.environ.get("FLASK_ENV", "production")

    # Azure Storage
    BLOB_CONTAINER = os.environ.get("BLOB_CONTAINER")
    BLOB_CONNECTION_STRING = os.environ.get("BLOB_CONNECTION_STRING")

    # Database (optional example)
    SQLALCHEMY_DATABASE_URI = os.environ.get("DATABASE_URL")
    SQLALCHEMY_TRACK_MODIFICATIONS = False