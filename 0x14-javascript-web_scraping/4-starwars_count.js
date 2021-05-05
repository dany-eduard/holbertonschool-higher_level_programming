#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
let count = 0;

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const movies = JSON.parse(body).results;
    for (let i = 0; i < movies.length; i++) {
      const characters = movies[i].characters;
      for (let j = 0; j < characters.length; j++) {
        if (characters[j] === 'https://swapi-api.hbtn.io/api/people/18/') {
          count += 1;
        }
      }
    }
    console.log(count);
  }
});
