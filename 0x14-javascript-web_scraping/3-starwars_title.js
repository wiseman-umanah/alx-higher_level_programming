#!/usr/bin/node
const request = require('request');
require('process');
const id = process.argv[2];
const link = `https://swapi-api.alx-tools.com/api/films/${id}`;

request(link, function (err, status, body) {
  if (err) console.error(err);
  else {
    const res = JSON.parse(body);
    console.log(res.title);
  }
});
