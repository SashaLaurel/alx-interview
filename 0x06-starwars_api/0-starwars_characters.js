#!/usr/bin/node
/*
Script that prints all characters of a Star Wars movie:
The first argument is the Movie ID - example: 3 = “Return of the Jedi”
The Star wars API must be used and using module request
*/

const request = require('request');
const movieID = process.argv.slice(2);
const endpoint = 'https://swapi-api.hbtn.io/api/films/' + movieID;

function makeRequest (array, index) {
  if (index === array.length) {
    return;
  }

  request(array[index], (error, response, body) => {
    if (error) {
      console.log(error);
    } else {
      console.log(JSON.parse(body).name);
      makeRequest(array, index + 1);
    }
  });
}

request(endpoint, (error, response, body) => {
  if (error) {
    console.log(error);
  } else {
    const chrList = JSON.parse(body).characters;
    makeRequest(chrList, 0);
  }
});
