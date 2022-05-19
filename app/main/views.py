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

@main.route('/login')
def index():
      return render_template('index.html')
    
@main.route('/user')
@login_required
def user():
    username = current_user.username
    user = User.query.filter_by(username=username).first()
    if user is None:
        abort(404)
    return render_template('profile/profile.html', user=user)

@main.route('/user/<name>/update_profile', methods=['POST', 'GET'])
@login_required
def update_profile(name):
    form = UpdateProfile()
    user = User.query.filter_by(username=name).first()
    if user is None:
        abort(404)
    if form.validate_on_submit():
        user.bio = form.bio.data
        user.save()
        return redirect(url_for('.user', name=user.username))
    return render_template('profile/update_profile.html', form=form)

@main.route('/user/<name>/update/pic',methods= ['POST'])
@login_required
def update_pic(name):
    user = User.query.filter_by(username = name).first()
    if 'photo' in request.files:
        filename = photos.save(request.files['photo'])
        path = f'photos/{filename}'
        user.profile_pic_path = path
        db.session.commit()
    return redirect(url_for('main.user',name=name))

@main.route('/tasks', methods = ['POST','GET'])
def tasks():
  '''
  view tasks page that displays the users tasks
  '''
  tasks = Task.query.order_by(Task.time.desc())
  quote = get_quote()
  form = TaskForm()

  if form.validate_on_submit():
    taskitem = form.task.data
    user_id = current_user._get_current_object().id

    new_task_object = Task(taskitem=taskitem,user_id=user_id)
    new_task_object.save_task()

    return redirect(url_for('main.tasks'))

  return render_template('tasks.html',quote=quote, form=form, tasks=tasks)


@main.route('/tasks/<task_id>/delete', methods = ['GET','POST'])
@login_required
def delete_task(task_id):
    task = Task.query.get(task_id)
    print(task)
    db.session.delete(task)
    db.session.commit()

    flash("You have deleted your task succesfully!")
    return redirect(url_for('main.tasks'))

@main.route('/tasks/<task_id>/update', methods = ['GET','POST'])
@login_required
def update_task(task_id):
    task = Task.query.get(task_id)
    if task.user != current_user:
        abort(403)
    form = TaskForm()
    if form.validate_on_submit():
        task.title = form.title.data
        task.description = form.description.data
        task.task = form.task.data
        db.session.commit()
        flash("You have updated your task!")
        return redirect(url_for('main.tasks',id = task.id)) 

    if request.method == 'GET':
        form.title.data = task.title
        form.description.data = task.description
        form.task.data = task.task
    return render_template('tasks.html', form = form)

@main.route('/tasks/<task_id>/reminders', methods = ['POST','GET'])
def reminders():

  return redirect(url_for('main.tasks'))
