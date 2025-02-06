#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line argument
const apiUrl = process.argv[2];

// Make a GET request to the API
request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const tasks = JSON.parse(body);
    const completedTasksCount = {};

    // Loop through each task and count completed tasks per user
    tasks.forEach(task => {
      if (task.completed) {
        if (completedTasksCount[task.userId]) {
          completedTasksCount[task.userId]++;
        } else {
          completedTasksCount[task.userId] = 1;
        }
      }
    });

    // Print the users with completed tasks
    console.log(completedTasksCount);
  }
});
