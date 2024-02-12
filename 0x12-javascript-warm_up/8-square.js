#!/usr/bin/node
let pa1 = process.argv[2];
if (isNaN(pa1)) { console.log('Missing size'); } else {
  pa1 = Number(pa1);
  for (let i = 0; i < pa1; i++) {
    console.log('X'.repeat(pa1));
  }
}
