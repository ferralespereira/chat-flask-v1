var socket = io.connect('http://' + document.domain + ':' + location.port);
socket.emit('joined', {});
socket.on('status', function (data) {
    var textare_chat = document.getElementById('chat');
    textare_chat.value += '<' + data.msg + '>\n';
    textare_chat.scrollTop = textare_chat.scrollHeight;
});
socket.on('message', function (data) {
    var textare_chat = document.getElementById('chat');
    textare_chat.value += '<' + data.msg + '>\n';
    textare_chat.scrollTop = textare_chat.scrollHeight;
});
function sendText(e) {
    var code = e.keyCode || e.which;
    if (code == 13) {
        var text = document.getElementById('text');
        socket.emit('text', { msg: text.value });
        text.value = '';
    }
}
function leave_room() {
    socket.emit('left', {}, function () {
        socket.disconnect();
    });
}
// when i enter or refresh the page, i'll get all users that are connected
socket.emit('get user list');
socket.on('get user list', function (data) {
    var users = document.getElementById('users');
    users.innerHTML = 'Users connected: <br>';
    for (var _i = 0, _a = data.list_users; _i < _a.length; _i++) {
        var user = _a[_i];
        if (user) {
            users.innerHTML += '<button type="button" class="btn btn-primary rounded-5 m-1">' + user + '</button>';
        }
    }
});
