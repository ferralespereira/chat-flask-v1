let socket:any = io.connect('http://' + document.domain + ':' + location.port + (window.location.pathname) );

// when i enter or refresh the page, i'll get all users that are connected
socket.emit('get user list');

socket.on('get user list', function(data:any){

    let users:any = document.getElementById('users');

    users.innerHTML = '<button type="button" class="btn btn-primary rounded-5 m-1">'+data.user+'</button>';

    for (let user of data.list_users) {
        users.innerHTML += '<button type="button" class="btn btn-primary rounded-5 m-1">'+user+'</button>';
    }
});