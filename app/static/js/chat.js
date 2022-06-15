var socket = io.connect('http://' + document.domain + ':' + location.port + '/chat');
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
