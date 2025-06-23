const express = require('express');
const soap = require('soap');
const fs = require('fs');
const path = require('path');
const logoutService = require('./logoutService');

const app = express();
const port = 3001;

const wsdlPath = path.join(__dirname, 'logout.wsdl');
const wsdlXml = fs.readFileSync(wsdlPath, 'utf8');

const server = app.listen(port, () => {
  console.log(`SOAP Logout Service running at http://localhost:${port}/logout`);
  soap.listen(server, '/logout', logoutService, wsdlXml);
});
