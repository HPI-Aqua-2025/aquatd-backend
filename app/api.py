from flask import jsonify, request
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from app import db
from .models import Task, List

class task_api(Resource):
    def get(self):
        tasks = Task.query.all()
        return jsonify(tasks)
    
    def post(self):
        try: 
            data = request.get_json()
        except Exception as e:
            return jsonify({"error": "Invalid JSON", "message": str(e)}), 400

        for task_data in data:
            id = data['id']
            parent_id = data['parent_id']
            list_name = data['list_name']
            is_in_my_day = data['is_in_my_day']
            created_at = data['created_at']
            due_to = data['due_to']
            done_at = data['done_at']
            order = data['order']
            content = data['content']
            title = data['title']
        
        if task_id not in existing_task_ids:
            new_task = Task(id=id, parent_id=parent_id, list_name=list_name, is_in_my_day=is_in_my_day,created_at=created_at, due_to=due_to, done_at=done_at,order=order, content=content, title=title)
            db.session.add(new_task)
        else:
            # Hier kannst du bei Bedarf auch die bestehende Task aktualisieren
            task = Task.query.get(id)
            task.parent_id=parent_id
            task.list_name=list_name
            task.is_in_my_day=is_in_my_day
            task.created_at=created_at
            task.due_to=due_to
            task.done_at=done_at
            task.order=order
            task.content=content
            task.title=title

        for task in existing_tasks:
            if task.id not in received_task_ids:
                db.session.delete(task)
        
        

class list_api(Resource):
    def get(self):
        lists = List.query.all()
        return jsonify(lists)
    
    def post(self):
        pass

        