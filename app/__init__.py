from flask import Flask
from flask_restful import Api
from dotenv import load_dotenv
import os

# import the blueprints for the routes
from .views import views

load_dotenv()

def create_app():
    app = Flask("app")
    api = Api(app)

    app.config["SECRET_KEY"] = os.getenv("MY_SECRET_KEY")

    app.register_blueprint(views, url_prefix="/")

    from .api import HelloWorld
    api.add_resource(HelloWorld, '/')

    return app