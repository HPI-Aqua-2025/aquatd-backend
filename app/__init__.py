from flask import Flask
from dotenv import load_dotenv
import os

# import the blueprints for the routes
from .views import views


def create_app():
    app = Flask("app")
    app.config["SECRET_KEY"] = os.getenv("MY_SECRET_KEY")

    app.register_blueprint(views, url_prefix="/")

    return app