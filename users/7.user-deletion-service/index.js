const express = require('express');
const soap = require('soap');
const fs = require('fs');
const http = require('http');
const service = require('./services/deleteUserService');

const xml = fs.readFileSync('deleteUser.wsdl', 'utf8');

const app = express();
const server = http.createServer(app);

app.use(express.json());

soap.listen(server, '/delete', service, xml);

server.listen(3004, () => {
  console.log('SOAP Delete User Service running at http://localhost:3004/delete');
});
