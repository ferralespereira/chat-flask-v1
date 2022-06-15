// let socket:any = io.connect('http://' + document.domain + ':' + location.port + '/' );
let socket:any = io.connect('http://' + document.domain + ':' + location.port + (window.location.pathname) );

// when i enter or refresh the page, i request for all users name that are connected
socket.emit('user connected');

socket.on('user connected', function(data:any){
    console.log(data);
    socket.emit('send my user name');
});

socket.on('send my user name', function(data:any){
    let users:any = document.getElementById('users');

    users.innerHTML += '<button type="button" class="btn btn-primary rounded-5 m-1">'+data.user+'</button>';
    console.log(data.user);

});

console.log(socket);