#!/usr/bin/node
const request = require('request');

const movieId = process.argv[2];

const url = `https://swapi-api.alx-tools.com/api/films/${movieId}`;

request(url, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

    if (response.statusCode !== 200) {
        console.log('Movie not found!');
        return;
    }

    const movieData = JSON.parse(body);
    console.log(movieData.title);
});
