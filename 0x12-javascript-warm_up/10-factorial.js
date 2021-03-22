#!/usr/bin/node

function factorial (n) {
  let total = 1;

  if (!n) {
    return 1;
  }

  for (let i = 1; i <= n; i++) {
    total *= i;
  }

  return total;
}

console.log(factorial(parseInt(process.argv[2])));
