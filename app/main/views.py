from flask import render_template
from . import main

#views
@main.route('/tasks')
def tasks():
  '''
  view tasks page that displays the users tasks
  '''
  quote = get_quote()
  return render_template('tasks.html',quote=quote)

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