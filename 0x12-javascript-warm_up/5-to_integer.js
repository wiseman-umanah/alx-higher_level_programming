#!/usr/bin/node
pa1 = process.argv[2]
if (isNaN(pa1))
	console.log("Not a number")
else
	console.log(`My number: ${parseInt(pa1)}`);
