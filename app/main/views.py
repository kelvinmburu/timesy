from flask import render_template
from . import main
from flask_login import current_user

from ..models import User

#views

@main.route('/user')
@login_required
def user():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('profile/profile.html', user=user)



@main.route('/tasks')
def tasks():
  '''
  view tasks page that displays the users tasks
  '''

  return render_template('tasks.html')

@main.route('/tasks/add')
def tasks():
  '''
  view tasks page that allows a user to add tasks
  '''

 return render_template('tasks.html')

@main.route('/tasks/reminder')
def tasks():
  '''
  view tasks page that allows a user to add a reminder
  '''

 return render_template('tasks.html')

@main.route('/tasks/reminder/send')
def tasks():
  '''
  view tasks page that allows a user to send reminders
  '''

 return render_template('tasks.html')