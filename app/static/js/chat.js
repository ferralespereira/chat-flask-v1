var socket = io.connect('http://' + document.domain + ':' + location.port);
// socket.on('connect', function(){
socket.emit('joined');
// });
var user_name = document.getElementById('user-name');
socket.on('give me your name', function () {
    socket.emit('take my name', { user_name: user_name.innerHTML });
});
socket.on('get user list', function (data) {
    var users = document.getElementById('users');
    // if are users connected
    if ((data.list_users).length > 0 && (data.list_users[0]).length > 0) {
        users.innerHTML = 'Users connected: <br>';
        for (var _i = 0, _a = data.list_users; _i < _a.length; _i++) {
            var user = _a[_i];
            if (user) {
                var btn_class = 'btn btn-primary rounded-5 m-1';
                if (user == user_name.innerHTML) {
                    btn_class = 'btn btn-info rounded-5 m-1';
                }
                users.innerHTML += '<button type="submit" name="room" value="' + user + '" class="' + btn_class + '">' + user + '</button>';
            }
        }
    }
    else {
        users.innerHTML = '<button type="submit" name="room" value="go" class="btn btn-primary rounded-5 m-1">Go</button>';
    }
});
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
