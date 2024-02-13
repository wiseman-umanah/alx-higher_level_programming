#!/usr/bin/node
const list = process.argv;
const fs = require('fs');
function getFile (fileName, hold) {
  hold = fs.readFileSync(fileName, 'utf-8');
  return (hold);
}

let f1, f2, f3;
f1 = f2 = f3 = '';
f1 = getFile(list[2], f1);
f2 = getFile(list[3], f2);
console.log(list);

fs.writeFileSync(list[4], f1 + f2);
f3 = getFile(list[4], f3);

console.log(f3);
