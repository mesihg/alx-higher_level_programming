#!/usr/bin/node

const request = require('request');

request(process.argv[2], function (err, response, body) {
  if (err) {
    console.log(err);
  } else if (response.statusCode === 200) {
    const todos = JSON.parse(body);
    const completed = {};

    todos.map((todo) => {
      if (todo.completed) {
        if (completed[todo.userId] === undefined) {
          completed[todo.userId] = 1;
        } else {
          completed[todo.userId]++;
        }
      }
      return completed;
    });
    console.log(completed);
  } else {
    console.log('code: ' + response.statusCode);
  }
});
