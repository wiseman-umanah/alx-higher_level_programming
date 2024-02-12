#!/usr/bin/node
const pa1 = process.argv[2];
if (isNaN(pa1)) { console.log('Missing size'); } else {
  for (let i = 0; i < pa1; i++) {
    for (let j = 0; j < pa1; j++) { console.log('X'.replace('\n', '')); }
  }
}
