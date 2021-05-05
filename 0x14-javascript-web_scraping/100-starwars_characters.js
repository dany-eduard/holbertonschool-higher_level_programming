#!/usr/bin/node
const request = require('request');
const url = `https://swapi-api.hbtn.io/api/films/${process.argv[2]}`;

request(url, 'utf8', (err, res, body) => {
  if (err) {
    console.log(err);
  } else {
    for (const t of JSON.parse(body).characters) {
      request(t, 'utf8', (error, res, body) => {
        if (error) throw error;
        else {
          console.log(JSON.parse(body).name);
        }
      });
    }
  }
});
