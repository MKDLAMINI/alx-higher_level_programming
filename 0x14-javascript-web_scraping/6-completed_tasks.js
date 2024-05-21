#!/usr/bin/node
// write a script that computes a number of tasks completed by user id

const request = require('request');

request.get(process.argv[2], { json: true }, (error, response, body) => {
  if (error) {
    console.log(error);
    return;
  }

  const Completed = {};
  body.forEach((todo) => {
    if (todo.completed) {
      if (!Completed[todo.userId]) {
        Completed[todo.userId] = 1;
      } else {
        Completed[todo.userId] += 1;
      }
    }
  });
  console.log(Completed);
});
