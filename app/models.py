from . import db
from flask_login import UserMixin
from . import login_manager
from datetime import datetime

@login_manager.user_loader
def load_user(user_id):
    return User.query.get(int(user_id))


#User Class
class User(UserMixin,db.Model):
    __tablename__ = 'users'
    
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(255))
    email = db.Column(db.String(255),unique = True,index = True)
    role_id = db.Column(db.Integer, db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    password_secure = db.Column(db.String(255))
    
    reviews = db.relationship('Review',backref = 'user',lazy = "dynamic")
    
    def __repr__(self):
        return f'User {self.username}'
    
    
# Task Class
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key = True)
    task = db.Column(db.String(500), nullable = True)

    reminder = db.relationship('Reminder',backref='task',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(dbDateTime, default = datetime.utcnow)

    def save_task(self):
        db.session.add(self)
        db.session.commit()

    def delete_task(self):
        db.session.delete(self)
        db.session.commit()
    
    def __repr__(self):
        return f'blog {self.task}'
