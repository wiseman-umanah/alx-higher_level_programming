#!/usr/bin/node
const request = require('request');
require('process');
const link = 'https://swapi-api.alx-tools.com/api/films/';

request(link, function (err, status, body) {
  if (err) console.error(err);
  else {
    let res = JSON.parse(body);
    (res.results[0].characters).forEach(element => {
      if (element.includes('18')) {
        request(element, function (err, status, body) {
          if (err) console.error(err);
          else {
            res = JSON.parse(body);
            console.log((res.films).length);
          }
        });
      }
    }
    );
  }
});
