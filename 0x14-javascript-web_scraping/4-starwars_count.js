#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const movies = JSON.parse(body).results;
    let count = 0;
    movies.map((movie) => {
      return movie.characters.map((character) => {
        if (character.includes('18')) {
          count++;
        }
        return count;
      });
    });
    console.log(count);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
