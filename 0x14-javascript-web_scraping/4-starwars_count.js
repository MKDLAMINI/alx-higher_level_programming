#!/usr/bin/node
// prints number of movies where Wedge Antilles appears

const request = require('request');
let integer = 0;

request.get(process.argv[2], (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const data = JSON.parse(body);
    data.results.forEach((film) => {
      film.characters.forEach((character) => {
        if (character.includes(18)) {
          integer += 1;
        }
      });
    });
    console.log(integer);
  }
});
