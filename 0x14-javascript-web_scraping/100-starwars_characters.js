#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';
request(url + process.argv[2], function (err, res, body) {
  if (err) {
    console.log(err);
  }
  const data = JSON.parse(body);
  const characterList = data.characters;
  for (const characterURL of characterList) {
    request(characterURL, function (err, res, body1) {
      if (err) {
        console.log(err);
      }
      const data1 = JSON.parse(body1);
      console.log(data1.name);
    });
  }
});
