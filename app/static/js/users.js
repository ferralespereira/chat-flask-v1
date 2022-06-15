var socket = io.connect('http://' + document.domain + ':' + location.port + (window.location.pathname));
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
