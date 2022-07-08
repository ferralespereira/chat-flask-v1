let socket:any = io.connect('http://' + document.domain + ':' + location.port);

// socket.on('connect', function(){
    socket.emit('joined');
// });

socket.on('give me your name', function(data:any) {
    let user_name:any = document.getElementById('user-name');
    socket.emit('take my name', { user_name: user_name.innerHTML });
});

socket.on('status', function(data:any) {
    let textare_chat:any = document.getElementById('chat');
    textare_chat.value += '<' + data.msg + '>\n';
    textare_chat.scrollTop = textare_chat.scrollHeight;
});

socket.on('message', function(data:any) {
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


socket.on('get user list', function(data:any){

    let users:any = document.getElementById('users');

    // if are users connected
    if ((data.list_users).length > 0 && (data.list_users[0]).length > 0 ){
        users.innerHTML = 'Users connected: <br>';
    
        for (let user of data.list_users) {
            if (user){
                users.innerHTML += '<button type="submit" name="room" value="'+user+'" class="btn btn-primary rounded-5 m-1">'+user+'</button>';
            }
        }
    }else{
        users.innerHTML = '<button type="submit" name="room" value="go" class="btn btn-primary rounded-5 m-1">Go</button>';
    }

    // console.log(data.list_users);
    // console.log((data.list_users[0]).length);
});