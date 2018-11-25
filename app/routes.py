from app import app
from flask import render_template
from .forms import LoginForm



@app.route('/')
@app.route('/index')
def index():
    user = {"username": 'Elliot'}
    mangas = [
        {
            "title": "Naruto",
            "author": "Masashi Kishimoto"
        },
        {
            "title": "ZombiePowder",
            "author": "Tite Kubo"
        }
    ]
    return  render_template('index.html',title="Home", user=user,mangas=mangas)

@app.route('/login')
def login():
    form = LoginForm()
    return render_template('login.html',title='Sign In', form=form)