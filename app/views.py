from flask import render_template,redirect,url_for
from app import app


@app.route('/')
def index():
    return 'Hello World'

