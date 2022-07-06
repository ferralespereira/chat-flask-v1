from flask import session, redirect, url_for, render_template, request, flash
from . import main
from .forms import LoginForm
from app import list_users

@main.route('/', methods=['GET', 'POST'])
def index():

    print('***----------------index----------------***')
    print(list_users)

    form = LoginForm(request.form)
    if request.method == 'POST':
        if form.validate():
            # if the user is already login and wrote a different name
            if session.get('name') and session.get('name') != form.name.data:
                form.name.data = session.get('name')
                print('this user is already login')
                flash('To change you Nickname you must logout', 'warning')
            else:
                session['name'] = form.name.data
                session['room'] = request.form['room']
                
                print('validation true')
                flash(session['name']+ ' Welcome!!', 'success')
        else:
            print('validation false')
            flash(form.name.errors[0], 'warning')

    if request.method == 'GET':
        if session.get('name'):
            form.name.data =  session['name']
        else:
            flash('Hi, write your Nickname and press Go!!', 'success')


    return render_template('index.html', form=form)


@main.route('/left', methods=['GET'])
def left():
    print('***----------------left----------------***')
    # remove the sesion name
    session.pop('name')
    return redirect(url_for('main.index'))