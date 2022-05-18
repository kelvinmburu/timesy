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
    role_id = db.Column(db.Integer,db.ForeignKey('roles.id'))
    bio = db.Column(db.String(255))
    profile_pic_path = db.Column(db.String())
    secure_password = db.Column(db.String(255),nullable = False)

    tasks = db.relationship('Task', backref='user', lazy='dynamic')
    reminders = db.relationship('Reminder',backref = 'user',lazy = "dynamic")

    is_admin = db.Column(db.Boolean, default=False)

    @property
    def password(self):
        raise AttributeError('You cannot read the password attribute')

    @password.setter
    def password(self, password):
        self.secure_password = generate_password_hash(password)

    def verify_password(self,password):
        return check_password_hash(self.secure_password,password)

    def save_user(self):
        db.session.add(self)
        db.session.commit()

    def delete_user(self):
        db.session.delete(self)
        db.session.commit()

    def __repr__(self):
        return f'User {self.username}'
    
    
# Task Class
class Task(db.Model):
    __tablename__ = 'tasks'
    id = db.Column(db.Integer, primary_key = True)
    taskitem = db.Column(db.String(500), nullable = True)

    reminder = db.relationship('Reminder',backref='task',lazy='dynamic')
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    time = db.Column(db.DateTime, default = datetime.utcnow)

    def save_task(self):
        db.session.add(self)
        db.session.commit()

    def delete_task(self):
        db.session.delete(self)
        db.session.commit()

    def get_task(id):
        task = Task.query.filter_by(id=id).first()

        return task
    
    def __repr__(self):
        return f'blog {self.task}'

class Reminder(db.Model):
    __tablename__ = 'reminders'
    id = db.Column(db.Integer, primary_key = True)
    email = db.Column(db.String(255),unique = True,index = True)
    user_id = db.Column(db.Integer, db.ForeignKey('users.id'))
    task_id = db.Column(db.Integer, db.ForeignKey('tasks.id'))