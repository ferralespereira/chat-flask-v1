from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

list_users = []

@socketio.on('get user list', namespace='/')
@socketio.on('get user list', namespace='/chat')
def sendMyUserName():
    emit('get user list', {
                    'msg': 'jaaj',
                    'list_users': list_users
                    },broadcast=True)


@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)

    # if user do not exists in the lis, i add it
    exists = session['name'] in list_users
    if not exists:
        list_users.append(session['name'])

    emit('status', {
                    'msg':        session.get('name') + ' has entered the room.',
                    'list_users': list_users
                    }, room=room)


@socketio.on('text', namespace='/chat')
def text(message):
    """Sent by a client when the user entered a new message.
    The message is sent to all people in the room."""
    room = session.get('room')
    emit('message', {'msg': session.get('name') + ': ' + message['msg']}, room=room)


@socketio.on('left', namespace='/chat')
def left(message):
    """Sent by clients when they leave a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    leave_room(room)

    # when i leave_room remove the user from list_user
    list_users.remove(session['name'])
    
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

