from flask import render_template, session,g,flash

from app import app
from app.forms import LoginForm


@app.route('/', methods=['GET'])
@app.route('/login', methods=['POST'])
def index():
    form = LoginForm()
    if form.validate_on_submit():
        g.user = {'username': form.name.data}
        flash('Login success!!')
        return render_template('main.html')
    flash('has not login!!! please login!!!')
    return render_template('index.html', form=form)
