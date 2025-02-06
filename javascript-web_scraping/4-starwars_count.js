#!/usr/bin/node

const request = require('request');

// Get the API URL from the command line argument
const apiUrl = process.argv[2];

// Make a GET request to the Star Wars API
request.get(apiUrl, (err, response, body) => {
  if (err) {
    console.log(err);
  } else {
    const data = JSON.parse(body);
    const films = data.results;
    let count = 0;

    // Loop through each film and check if Wedge Antilles (ID 18) is in the characters list
    films.forEach(film => {
      if (film.characters.some(character => character.includes('18'))) {
        count++;
      }
    });

    // Print the number of films where Wedge Antilles appears
    console.log(count);
  }
});
