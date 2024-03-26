#!/usr/bin/node
const request = require('request');
require('process');
const link = `https://swapi-api.alx-tools.com/api/films/${process.argv[2]}`;

request(link, function (err, status, body) {
  if (err) console.error(err);
  else {
    const res = JSON.parse(body);
    requestCharacter(res.characters, 0);
  }
});

function requestCharacter (characters, index) {
  // Base case: if the index is equal to the length of the characters array, stop the recursion
  if (index >= characters.length) return;

  // Make the request for the current character
  request(characters[index], function (err, status, body) {
    if (err) console.error(err);
    else {
      const res = JSON.parse(body);
      console.log(res.name);
    }
    requestCharacter(characters, index + 1);
  });
}
