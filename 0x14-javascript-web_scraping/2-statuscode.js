#!/usr/bin/node
const request = require('request');
require('process');
const link = process.argv[2];

request(link, function (err, status, body) {
  if (err) console.error(err);
  else console.log(`code: ${status.statusCode}`);
});
