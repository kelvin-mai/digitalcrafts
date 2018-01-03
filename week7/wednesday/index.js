const express = require('express');
const app = express();

app.get('/', (req, res) => {
  res.send('Hello');
});

app.get('/:name', (req, res) => {
  res.send(`Hello ${req.params.name}`);
});

app.listen(8000, () => {
  console.log("Server started");
});
