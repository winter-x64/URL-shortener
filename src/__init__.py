from os import path

from flask import Flask
from flask_sqlalchemy import SQLAlchemy

# Database name for flask
db_name = "Database.db"

# Integrates SQLAlchemy with Flask
db = SQLAlchemy()


def main() -> Flask:

    # initialize the flask application
    app = Flask(import_name=__name__)

    # config the flask application
    app.config["SECRET_KEY"] = "your secret key"

    # database name
    app.config["SQLALCHEMY_DATABASE_URI"] = f"sqlite:///{db_name}"
    app.config["SQLALCHEMY_TRACK_MODIFICATIONS"] = True

    # import Tables
    from .models.models import urlbase

    # creates SQLALCHEMY object
    db.init_app(app=app)

    create_db(app=app)

    from .views import home

    app.register_blueprint(blueprint=home.home_view, url_prefix="/")

    return app


# Create a Database
def create_db(app) -> None:
    if not path.exists(path=f"instance/{db_name}"):
        with app.app_context():
            db.create_all()
        print("Creating database")
    else:
        print("Database Found")
