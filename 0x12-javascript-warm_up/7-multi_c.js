#!/usr/bin/node
pa1 = process.argv[2];
if (isNaN(pa1))
	console.log("Missing number of occurrences");
else
{
	for (i = 0; i < pa1; i++)
		console.log("C is fun");
}