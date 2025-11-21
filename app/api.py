from flask import jsonify
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from app import db
from .models import Task, List

class task_api(Resource):
    def get(self):
        tasks = Task.query.all()
        return jsonify(tasks)
    
    def post(self):
        pass
        

class list_api(Resource):
    def get(self):
        lists = List.query.all()
        return jsonify(lists)
    
    def post(self):
        pass