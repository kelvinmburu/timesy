from flask import render_template, request, redirect, abort,url_for
from . import main
from flask_login import login_required, current_user
from .. import db,photos
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