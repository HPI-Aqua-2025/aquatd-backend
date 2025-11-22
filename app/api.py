from flask import jsonify, request
from flask_restful import Resource
from flask_sqlalchemy import SQLAlchemy
from app import db
from .models import Task, List

class task_api(Resource):
    def post(self):
        try: 
            data = request.get_json()
        except Exception as e:
            return jsonify({"error": "Invalid JSON", "message": str(e)}), 400

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
    

        try:
            new_task = Task(id=id, parent_id=parent_id, list_name=list_name, is_in_my_day=is_in_my_day,created_at=created_at, due_to=due_to, done_at=done_at,order=order, content=content, title=title)
            db.session.add(new_task)
            db.session.commit()
        except Exception as e:
            return jsonify({"error": "POST REQUEST FAILED", "message": str(e)}), 400
            

    def delete(self, task_id):
        chosen_task = Task.query.filter(id=task_id)
        if chosen_task:
            db.session.delete(chosen_task)
            db.session.commit()
            return 200
        else:
            return 400

    def put(self, task_id):

        try: 
            data = request.get_json()
        except Exception as e:
            return jsonify({"error": "Invalid JSON", "message": str(e)}), 400

        parent_id = data['parent_id']
        list_name = data['list_name']
        is_in_my_day = data['is_in_my_day']
        created_at = data['created_at']
        due_to = data['due_to']
        done_at = data['done_at']
        order = data['order']
        content = data['content']
        title = data['title']

        task = Task.query.get(task_id)
        task.parent_id=parent_id
        task.list_name=list_name
        task.is_in_my_day=is_in_my_day
        task.created_at=created_at
        task.due_to=due_to
        task.done_at=done_at
        task.order=order
        task.content=content
        task.title=title
        return 200


class list_api_task(Resource):
    def get(self, list_id, task_id):
        if task_id:
            task = Task.query.filter(parent_id=list_id, id=task_id)
        else:
            task = Task.query.filter(parent_id=list_id)

        return jsonify(task), 400
    
    def post(self):
        pass

class list_api_id(Resource):
    def get(self, list_id):
        return [x.to_dict() for x in List.query.filter(id=list_id)], 200
    
    def delete(self, list_id):
        chosen_list = List.query.filter(id=list_id)
        if chosen_list:
            db.session.delete(chosen_list)
            db.session.commit()
            return 200
        else:
            return 400
        
    def put(self, list_id):
        try: 
            data = request.get_json()
        except Exception as e:
            return jsonify({"error": "Invalid JSON", "message": str(e)}), 400
        
        owner_id = data['owner_id']
        name = data['name']
        created_at = data['created_at']

        list = List.query.filter(id=list_id)
        list.owner_id = owner_id
        list.name = name
        list.create_at = created_at
        return 200
    

class list_api(Resource):
    def get(self):
        return [i.to_dict() for i in List.query.all()], 200
    
    def post(self):
        try: 
            data = request.get_json()
        except Exception as e:
            return jsonify({"error": "Invalid JSON", "message": str(e)}), 400
        
        id = data['id']
        owner_id = data['owner_id']
        name = data['name']
        created_at = data['created_at']

        new_list = List(id=id, owner_id=owner_id, name=name, created_at=created_at)
        db.session.add(new_list)
        db.session.commit()
        return 200

    