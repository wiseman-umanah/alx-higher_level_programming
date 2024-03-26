#!/usr/bin/node
require('process');
const request = require('request');
const fs = require('fs');
const link = process.argv[2];
const file = process.argv[3];

request(link, function (err, status, body) {
  if (err) console.error(err);
  else {
    fs.writeFile(file, body, 'utf-8', (err) => {
      if (err) console.error(err);
    });
  }
});
