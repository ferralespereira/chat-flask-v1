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
            # if 'sessio name' is created
            if session.get('name'):
                # if the user wrote a different name
                if session.get('name') != form.name.data:
                    form.name.data = session.get('name')
                    print('this user is already login')
                    flash('To change you Nickname you must logout', 'warning')
            else:
                exists = form.name.data in list_users
                # if the name the user wrote is already taken
                if exists:
                    form.name.data = ''
                    print('exist')
                    flash('This Nickname had been taken, please chose another one', 'warning')
                else:
                    # create 'session name'
                    session['name'] = form.name.data

                    # add 'session name' into list_users 
                    list_users.append(session['name'])
                
                    print('validation true')
                    flash(session['name']+ ' Welcome!!', 'success')
            
            # create or update 'session room' (to enable switch betewn rooms)
            session['room'] = request.form['room']

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
    print('***----------------left GET----------------***')
    
    # remove the user from list_user
    list_users.remove(session.get('name'))

    # remove the 'sesion name' and 'sesion room'
    session.pop('name')
    session.pop('room')

    print(session.get('name'))

    return redirect(url_for('main.index'))