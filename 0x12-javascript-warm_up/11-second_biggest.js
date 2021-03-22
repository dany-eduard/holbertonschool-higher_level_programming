#!/usr/bin/node

const array = process.argv.slice(2);

if (array.length <= 1) {
  console.log(0);
} else {
  array.sort((a, b) => a - b);
  const len = array.length;
  console.log(array[len - 2]);
}
