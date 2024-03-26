#!/usr/bin/node
const request = require('request');
require('process');
const link = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(link, function (err, status, body) {
  if (err) console.error(err);
  else {
    let res = JSON.parse(body);
    res.characters.forEach(element => {
      request(element, function (err, status, body) {
        if (err) console.error(err);
        else {
          res = JSON.parse(body);
          console.log(res.name);
        }
      });
    });
  }
});
