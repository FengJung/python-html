from app import app
from flask import render_template


@app.route('/')
@app.route('/index')
def index():

    user = {'username' : 'Jung'}
    posts = [
        {'author': {'username': 'Maria'}, 'body' : 'Ola Maria'}, 
        {'author': {'username': 'Joao'}, 'body' : 'Ola Jaao'}
    ]
    return render_template("index.html", user=user, posts = posts)
