#!/usr/bin/node

const request = require('request');

// Get the movie ID from the command line argument
const movieId = process.argv[2];

// Build the API URL with the movie ID
const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

// Make a GET request to the Star Wars API
request.get(url, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const movie = JSON.parse(body);
    console.log(movie.title);
  }
});
