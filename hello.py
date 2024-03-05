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
    stuff = "This is a <strong>Bold</strong> Text"
    favourite_pizza = ["Pepperoni", "Cheese", "Mushroom", 41]
    return render_template("user.html", 
                           user_name=name,
                           stuff=stuff,
                           favourite_pizza=favourite_pizza)

# Handling errors

#Invalid url
@app.errorhandler(404)
def page_not_found(e):
    return render_template('404.html'), 404

