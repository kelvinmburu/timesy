from flask import Flask, render_template, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
#database instance
db = SQLAlchemy(app)

#connects app file to our database
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:////database.db'

@app.route("/")
def hello_world():
    return render_template('home.html')

@app.route('/login')
def login():
    return render_template('login.html')
    

if __name__ == '__main__':
    app.run(debug=True)