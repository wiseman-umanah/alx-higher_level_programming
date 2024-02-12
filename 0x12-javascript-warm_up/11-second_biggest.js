#!/usr/bin/node
if (process.argv.length <= 3) { console.log(0); } else {
  let temp = process.argv;
  temp = temp.slice(2).sort((a, b) => a - b);
  console.log(Number(temp[temp.length - 2]));
}
