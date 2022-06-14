let socket:any = io.connect('http://' + document.domain + ':' + location.port + '/');

socket.emit('get users');

socket.on('show users', function(data:any) {
    let users:any = document.getElementById('users');

    for (let user of data.list_users) {
        users.innerHTML += '<button type="button" class="btn btn-primary rounded-5 m-1">'+user+'</button>';
    }
    
    console.log(data);
});
