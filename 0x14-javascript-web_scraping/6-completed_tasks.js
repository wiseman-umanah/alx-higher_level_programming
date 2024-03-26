#!/usr/bin/node
const request = require('request');
require('process');
const link = process.argv[2];
const users = {};
request(link, function (err, status, body) {
  if (err) console.error(err);
  else {
    const res = JSON.parse(body);
    res.forEach(element => {
      if (element.userId in users) {
        if (element.completed) { users[element.userId] += 1; }
      } else { users[element.userId] = 0; }
    });
  }
  console.log(users);
});
