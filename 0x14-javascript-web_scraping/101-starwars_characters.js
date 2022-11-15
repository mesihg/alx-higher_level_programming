#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

function characterRequest (characterUrl) {
  return new Promise((resolve, reject) => {
    request.get(characterUrl, (err, _resp, body) => {
      if (err !== null) {
        reject(err);
      }
      resolve(body);
    });
  });
}

request(url + process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const film = JSON.parse(body);
  const characters = film.characters;
  characters.forEach((character) => {
    characterRequest(character).then((body) => {
      const characterInfo = JSON.parse(body);
      console.log(characterInfo.name);
    }).catch(err => console.log(err));
  });
});
