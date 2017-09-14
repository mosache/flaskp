from flask import render_template, session,g,flash
from app.models import User
from app import app
from app import db
from app.forms import LoginForm


@app.route('/', methods=['GET'])
@app.route('/login', methods=['POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        username = form.name.data
        pwd =form.password.data
        users = User.query.filter_by(username=username, password=pwd).all()
        if len(users) > 0:
            g.user = {'username': form.name.data}
            flash('Login success!!')
            return render_template('main.html', users=users)
        else:
            flash('login info is not correct!!')
    return render_template('index.html', form=form)
