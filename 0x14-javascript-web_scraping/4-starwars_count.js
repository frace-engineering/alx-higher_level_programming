#!/usr/bin/node
const request = require('request');

request(process.argv[2], function (error, response, body) {
  if (!error && response.statusCode === 200) {
    try {
      const results = JSON.parse(body).results;
      const count = results.reduce((acc, movie) => {
        const hasCharacter = movie.characters.some((character) => character.endsWith('/18/'));
        return hasCharacter ? acc + 1 : acc;
      }, 0);
      console.log(count);
    } catch (parseError) {
      console.error('Error parsing JSON:', parseError.message);
    }
  } else {
    console.error('Error:', error || `Unexpected status code ${response.statusCode}`);
  }
});
