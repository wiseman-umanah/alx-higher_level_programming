#!/usr/bin/node
function factorial(n){
	fac = 0
	if (isNaN(n) || n <= 1)
		return(1);
	fac = n * factorial(n - 1);
	return (fac);
}
pa1 = Number(process.argv[2]);
ans = factorial(parseInt(pa1));
console.log(ans);
