#!/usr/bin/node
const request = require('request');
const url = process.argv[2];

request.get(url, (err, body) => {
  if (err) {
    console.log(err);
  } else {
    let count = 0;
    for (let film of JSON.parse(body).results) {
      film.characters.forEach((character) => {
        if (character.includes('18')) {
          count++;
        }
      })
    }
    console.log(count);
  }
});
