#!/usr/bin/node
// script that reads and prints the content of a file.
require('process');
const fs = require('fs');

fs.readFile(process.argv[2], 'utf-8', (err, data) => {
  if (err) console.error(err);
  else console.log(data);
});
