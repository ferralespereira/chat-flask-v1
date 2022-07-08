from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio
from app import list_users


@socketio.on('take my name')
def takeMyName(data):
    print('**********************users***********')

    if data['user_name']:
        list_users.append(data['user_name'])
    print(list_users)

    emit('get user list', {
                    'msg': 'jaaj',
                    'list_users': list_users
                    },broadcast=True)


@socketio.on('joined')
def joined():

    print('***----------------joined----------------***')
    print('user name:')
    print(session.get('name'))

    # if user is is loged
    name = session.get('name')
    if (name):
        
        room = session.get('room')
        join_room(room)
        
        emit('status', {
                'msg':name + ' has entered the room.'
                }, room=room)

    del list_users[:]

    emit('give me your name', {
                'msg': 'message',
                'list_users': list_users
                },broadcast=True)
    


@socketio.on('text')
def text(message):

    print('***----------------text----------------***')
    print('name: '+session.get('name'))
    print('room: '+session.get('room'))

    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ': ' + message['msg']}, room=room)


@socketio.on('left')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)
        
    print('***----------------left----------------***')
    print(session.get('name'))

    emit('status', {'msg': ' has left the room.'}, room=room)

