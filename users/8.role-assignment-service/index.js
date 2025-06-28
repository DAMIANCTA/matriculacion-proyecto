const express = require('express');
const soap = require('soap');
const fs = require('fs');
const http = require('http');
const roleService = require('./roleService');

const xml = fs.readFileSync('./wsdl/role-assignment.wsdl', 'utf8');
const app = express();
const port = 3003;

const server = http.createServer(app);

soap.listen(server, '/assign-role', roleService, xml, () =>
  console.log(`SOAP Role Assignment Service running at http://localhost:3003/assign-role`)
);

server.listen(port);
