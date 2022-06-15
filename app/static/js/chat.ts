let socket:any = io.connect('http://' + document.domain + ':' + location.port + '/chat');

// socket.on('connect', function() {
    socket.emit('joined', {});
// });

socket.on('status', function(data:any) {
    let textare_chat:any = document.getElementById('chat');
    textare_chat.value += '<' + data.msg + '>\n';
    textare_chat.scrollTop = textare_chat.scrollHeight;
});

socket.on('message', function(data) {
    let textare_chat:any = document.getElementById('chat');
    textare_chat.value += '<' + data.msg + '>\n';
    textare_chat.scrollTop = textare_chat.scrollHeight;
});

function sendText(e:any){
    let code = e.keyCode || e.which;
    if (code == 13) {
        let text:any = document.getElementById('text');
        socket.emit('text', { msg: text.value });
        text.value ='';
    }
}

function leave_room() {
    socket.emit('left', {}, function () {
        socket.disconnect();
    });
}
