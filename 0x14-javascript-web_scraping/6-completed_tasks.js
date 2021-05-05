#!/usr/bin/node
const request = require('request');
const url = process.argv[2];
const tasksD = {};

request.get(url, (err, res, body) => {
  if (err) {
    console.error(err);
  } else {
    const tasks = JSON.parse(body);
    tasks.forEach((task) => {
      if (task.completed) {
        if (task.userId in tasksD) {
          tasksD[task.userId] += 1;
        } else {
          tasksD[task.userId] = 1;
        }
      }
    })
  }
  console.log(tasksD);
})
