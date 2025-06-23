const express = require('express');
const soap = require('soap');
const fs = require('fs');
const http = require('http');
const service = require('./passwordService');

const app = express();
const wsdl = fs.readFileSync('password.wsdl', 'utf8');
const server = http.createServer(app);

soap.listen(server, '/password', service, wsdl);

server.listen(3002, () => {
  console.log("SOAP Password Change Service running at http://localhost:3002/password");
});