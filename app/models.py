from . import db

class Task(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    parent_id = db.Column(db.String(64), primary_key=True)
    list = db.Column(db.String(64), primary_key=True)
    is_in_my_day = db.Column(db.Bool)
    created_at = db.Column(db.Integer)
    due_to = db.Column(db.Integer)
    done_at = db.Column(db.Integer)
    order = db.Column(db.Float)
    content = db.Column(db.String(64))
    title = db.Column(db.String(64))
    # repeat_every

class List(db.Model):
    id = db.Column(db.String(64), primary_key=True)
    owner_id = db.Column(db.String(64), primary_key=True)
    name = db.Column(db.String(64), primary_key=True)
    created_at = db.Column(db.Integer)
