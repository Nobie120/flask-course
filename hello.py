from flask import Flask, render_template
from markupsafe import escape


# create a flask instance
app = Flask(__name__)

# Create a router decorator
@app.route('/')

#def index():
#    return '<h1>Hello World!</h1>'

def index():
    return render_template("index.html")

# localhost:5000/user/Ken
@app.route('/user/<name>')

def user(name):
    return f"<h4>Hello {escape(name)}!!<h4>"
