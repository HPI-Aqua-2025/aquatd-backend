from flask import Flask
from flask_restful import Api
from flask_sqlalchemy import SQLAlchemy
from dotenv import load_dotenv
import os

# import the blueprints for the routes
from .views import views


load_dotenv()
db = SQLAlchemy()

def create_app():
    app = Flask("app")
    
    api = Api(app)

    app.config["SECRET_KEY"] = os.getenv("MY_SECRET_KEY")
    app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///app.db'

    app.register_blueprint(views, url_prefix="/")

    db.init_app(app)


    # import of the api classes idk
    from .api import task_api, list_api

    api.add_resource(task_api, '/tasks')
    api.add_resource(list_api, '/lists')

    return app