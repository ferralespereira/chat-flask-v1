from flask import session
from flask_socketio import emit, join_room, leave_room
from .. import socketio

@socketio.on('user connected', namespace='/')
def userConnected():
    emit('user connected', {
                            'msg':' send me your user name.'
                            },broadcast=True, include_self=False)

@socketio.on('send my user name', namespace='/')
def sendMyUserName():
    emit('send my user name', {
                    'user': session['name']
                    },broadcast=True, include_self=False)



@socketio.on('joined', namespace='/chat')
def joined(message):
    """Sent by clients when they enter a room.
    A status message is broadcast to all people in the room."""
    room = session.get('room')
    join_room(room)
    emit('status', {
                    'msg':        session.get('name') + ' has entered the room.',
                    'list_users': session.get('users')
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

    # remove this user from session['users']
    # session['users']=NULL
    # session.pop('users', None)  
    # print(session)
    
    emit('status', {'msg': session.get('name') + ' has left the room.'}, room=room)

