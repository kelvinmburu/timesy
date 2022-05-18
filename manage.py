from flask import Flask, render_template
from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin,current_user

app = Flask(__name__)
#database instance
db = SQLAlchemy(app)

#connects app file to our database
app.config['SQLALCHEMY_DATABASE_URI'] 
app.config['SECRET_KEY']='thisisasecretkey'

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')
    

if __name__ == '__main__':
    app.run(debug=True)