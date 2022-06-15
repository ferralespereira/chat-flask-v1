var socket = io.connect('http://' + document.domain + ':' + location.port + '/');
// when i enter or refresh the page, i request for all users name that are connected
socket.emit('user connected');
socket.on('user connected', function (data) {
    console.log(data);
    socket.emit('send my user name');
});
socket.on('send my user name', function (data) {
    var users = document.getElementById('users');
    users.innerHTML += '<button type="button" class="btn btn-primary rounded-5 m-1">' + data.user + '</button>';
    console.log(data.user);
});
