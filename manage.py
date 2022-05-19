
from app import create_app,db
from flask_script import Manager,Server
from app.models import User, Task, Reminder
from  flask_migrate import Migrate, MigrateCommand
=======
from flask import Flask, render_template,url_for

# Creating appinstance
app = create_app('development')

manager = Manager(app)
migrate = Migrate(app,db)

manager.add_command('server',Server)
manager.add_command('db',MigrateCommand)

@manager.command
def test():
    """Run the unit tests."""
    import unittest
    tests = unittest.TestLoader().discover('tests')
    unittest.TextTestRunner(verbosity=2).run(tests)

@manager.shell
def make_shell_context():
    return dict(app = app,db = db,User = User, Task=Task, Reminder=Reminder )

if __name__ == '__main__':
    manager.run()
@app.route("/")
def hello_world():

    return render_template('home.html')


@app.route('/login')
def login():
    return render_template('login.html')
    

if __name__ == '__main__':
    app.run(debug=True)
