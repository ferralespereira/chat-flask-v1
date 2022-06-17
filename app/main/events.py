from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

list_users = []

@socketio.on('get user list')
def getUserList():
    emit('get user list', {
                    'msg': 'jaaj',
                    'list_users': list_users
                    },broadcast=True)


@socketio.on('joined')
def joined(message):
    # if user is is loged
    name = session.get('name')
    if (name):
        
        # if user do not exists in the list, i add it
        exists = name in list_users
        if not exists:
            list_users.append(name)
        
        room = session.get('room')
        join_room(room)
        
        emit('status', {
                'msg':name + ' has entered the room.'
                }, room=room)


@socketio.on('text')
def text(message):
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

    # when i leave_room remove the user from list_user
    list_users.remove(session.get('name'))
    
    session.pop('name')

    # emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)
    emit('status', {'msg': ' has left the room.'}, room=room)

