from flask import render_template,redirect,url_for
from . import main
from ..requests import get_quote
from .forms import *
from .. import db
from ..models import *

#views
@main.route('/tasks', methods = ['POST','GET'])
def tasks():
  '''
  view tasks page that displays the users tasks
  '''
  form = TaskForm()
  if form.validate_on_submit():
    taskitem = form.task.data

    new_task_object = Task(taskitem=taskitem)
    new_task_object.save_task()

    return redirect(url_for('main.tasks'))

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