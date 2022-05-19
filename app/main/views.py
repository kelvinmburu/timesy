from flask import render_template, redirect, request, url_for, abort, flash
from . import main
from flask_login import login_required,current_user
from ..email import mail_message
from ..models import *
from . import main
from .. import db,photos
from .forms import *
from app.requests import get_quote

#views
@main.route('/')
def index():
  '''
    View root page function that returns the index page and its data
  '''

  return render_template('index.html')

@main.route('/tasks', methods = ['POST','GET'])
def tasks():
  '''
  view tasks page that displays the users tasks
  '''
  tasks = Task.query.order_by(Task.time.desc())
  form = TaskForm()

  if form.validate_on_submit():
    taskitem = form.task.data
    user_id = current_user._get_current_object().id

    new_task_object = Task(taskitem=taskitem,user_id=user_id)
    new_task_object.save_task()

    return redirect(url_for('main.tasks'))

  quote = get_quote()
  return render_template('tasks.html',quote=quote, form=form, tasks=tasks)


@main.route('/tasks', methods = ['POST','GET'])
def tasks():
  '''
  view tasks page that displays the users tasks
  '''
  tasks = Task.query.order_by(Task.time.desc())
  form = TaskForm()

  if form.validate_on_submit():
    taskitem = form.task.data
    user_id = current_user._get_current_object().id

    new_task_object = Task(taskitem=taskitem,user_id=user_id)
    new_task_object.save_task()

    return redirect(url_for('main.tasks'))

  quote = get_quote()
  return render_template('tasks.html',quote=quote, form=form, tasks=tasks)

@main.route('/tasks/<task_id>/delete', methods = ['GET','POST'])
@login_required
def delete_task(task_id):
    task = task.query.get(task_id)
    if task.user != current_user:
        abort(403)
    db.session.delete(task)
    db.session.commit()

    flash("You have deleted your task succesfully!")
    return redirect(url_for('main.tasks'))

