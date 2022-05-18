from flask import render_template
from . import main

#views
@main.route('/tasks')
def tasks():
  '''
  view tasks pages that returns the users tasks
  '''

  return render_template('tasks.html')