#!/usr/bin/node
function factorial (n) {
  let fac = 0;
  if (isNaN(n) || n <= 1) { return (1); }
  fac = n * factorial(n - 1);
  return (fac);
}
const pa1 = Number(process.argv[2]);
const ans = factorial(parseInt(pa1));
console.log(ans);
