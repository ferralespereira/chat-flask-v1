from flask import session, redirect, url_for, render_template, request
from . import main
# from .forms import LoginForm


@main.route('/', methods=['GET', 'POST'])
def index():
    """Login form to enter a room."""
    # form = LoginForm()
    # session['name'] = form.name.data
    # session['room'] = form.room.data

    if request.method == 'POST':
        session['name'] = request.form['name']
        session['room'] = request.form['room']
        return render_template('index.html', name=session['name'])

    return render_template('index.html')