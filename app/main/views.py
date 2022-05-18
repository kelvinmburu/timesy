from flask import render_template
from . import main
from ..requests import get_quote
from .forms import *
from .. import db
from ..models import *

#views
@main.route('/tasks')
def tasks():
  '''
  view tasks page that displays the users tasks
  '''
  form = TaskForm()
  if form.validate_on_submit():
    task = form.task.data

    new_task_object = Task(task=task,user_id=user_id)

  quote = get_quote()
  return render_template('tasks.html',quote=quote, form=form)

@main.route('/tasks/add')
def add_tasks():
  '''
  view tasks page that allows a user to add tasks
  '''

  return render_template('tasks.html')

@main.route('/tasks/reminder')
def add_reminder():
  '''
  view tasks page that allows a user to add a reminder
  '''

  return render_template('tasks.html')

@main.route('/tasks/reminder/send')
def send_reminder():
  '''
  view tasks page that allows a user to send reminders
  '''

  return render_template('tasks.html')