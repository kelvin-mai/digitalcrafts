const app = require('express')(),
http = require('http').Server(app),
io = require('socket.io')(http);

app.get('/', (req, res) => {
  res.sendFile(__dirname + '/index.html');
});

io.on('connection', socket => {
  console.log('User connected');
  socket.on('chat message', msg => {
    console.log('Message: ' + msg);
    io.emit('chat message', msg);
  });
  socket.on('disconnect', () => console.log('User disconnected'));
});

http.listen(4000, () => console.log('Listening on port 4000'));
