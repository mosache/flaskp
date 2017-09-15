from flask import render_template, session, g, flash, redirect, url_for, request
from app.models import User
from app import app
from app import db
from app.forms import LoginForm
from app import lm
from flask_login import login_user, current_user, login_required, logout_user


@app.before_request
def before_request():
    g.user = current_user


@lm.user_loader
def load_user(id):
    return User.query.get(int(id))


@app.route('/', methods=['POST', 'GET'])
@app.route('/login', methods=['POST', 'GET'])
def login():
    if g.user is not None and g.user.is_authenticated:
        return redirect(url_for('index'))

    form = LoginForm()
    if form.validate_on_submit():
        username = form.name.data
        pwd = form.password.data
        user = User.query.filter_by(username=username, password=pwd).first()
        if user is not None:
            g.user = user
            login_user(user)
            return redirect(request.args.get('next') or url_for('index'))
        else:
            flash('login info is not correct!!')
    return render_template('index.html', form=form)


@app.route('/logout')
def logout():
    logout_user()
    return redirect(url_for('login'))


@app.route('/index', methods=['POST', 'GET'])
@login_required
def index():
    return render_template('main.html')
