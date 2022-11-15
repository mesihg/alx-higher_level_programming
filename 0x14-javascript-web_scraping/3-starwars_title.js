#!/usr/bin/node

const request = require('request');
const url = 'https://swapi-api.hbtn.io/api/films/';

request(url + process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const respData = JSON.parse(body);
    console.log(respData.title);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
