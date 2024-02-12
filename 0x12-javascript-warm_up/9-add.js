#!/usr/bin/node
function add (a, b) {
  console.log(a + b);
}
const pa1 = Number(process.argv[2]);
const pa2 = Number(process.argv[3]);
add(pa1, pa2);
