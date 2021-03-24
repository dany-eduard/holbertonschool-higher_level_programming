#!/usr/bin/node

const fs = require('fs');

const read = (fileName) => {
  return fs.readFileSync(fileName, 'utf8', function(err, data) {
    if (err) {
      return console.log(err);
    }
    console.log(data);
    return (data);
  });
}


if (process.argv.length < 2 || process.argv.length > 5) {
  console.log('Arguments NOT found');
  return;
} else {
  const fileA = read(process.argv[2]);
  const fileB = read(process.argv[3]);
  const data = fileA + fileB;

  fs.writeFileSync(process.argv[5], data, function(err) {
    if (err) {
      return console.log(err);
    }
  
    console.log("Success...");
  });
}
