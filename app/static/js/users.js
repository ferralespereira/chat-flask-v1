var socket = io.connect('http://' + document.domain + ':' + location.port + '/');
socket.emit('get users');
socket.on('show users', function (data) {
    var users = document.getElementById('users');
    for (var _i = 0, _a = data.list_users; _i < _a.length; _i++) {
        var user = _a[_i];
        users.innerHTML += '<button type="button" class="btn btn-primary rounded-5 m-1">' + user + '</button>';
    }
    console.log(data);
});
