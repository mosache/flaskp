from flask import render_template

from app import app
from app.forms import LoginForm


@app.route('/')
def index():
    form = LoginForm()
    return render_template('index.html', form=form)
