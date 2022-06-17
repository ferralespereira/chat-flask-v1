from flask import session, redirect, url_for, render_template, request
from . import main
from .forms import LoginForm


@main.route('/', methods=['GET', 'POST'])
def index():
    form = LoginForm()
    if request.method == 'POST':
        session['name'] = form.name.data
        session['room'] = request.form['room']

        return render_template('index.html', form=form)
    
    if request.method == 'GET':
        if session.get('name'):
            form.name.data =  session['name'] 
        else:
            form.name.data =  "" 
        return render_template('index.html', form=form)