from flask import Flask
app = Flask(__name__)
@app.route('/')
def home():
    return "Hello from timesy!"

    if__name__ =='__main__':
    app.run(debug=True)