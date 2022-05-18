from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#database instance
db = SQLAlchemy(app)

#connects app file to our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'
app.config['SECRET_KEY']='thisisasecretkey'

#database for tables
class user (db,model, UserMixin):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(20),nullable=False)
    password = db.Column(db.String(80),nullable=False)


@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')
    

if __name__ == '__main__':
    app.run(debug=True)