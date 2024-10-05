#!/usr/bin/node
const request = require('request');

const apiUrl = process.argv[2];

request(apiUrl, (error, response, body) => {
    if (error) {
        console.error(error);
        return;
    }

    if (response.statusCode !== 200) {
        console.log('Failed to fetch data!');
        return;
    }

    const films = JSON.parse(body).results;
    const wedgeAntillesId = 18;
    let count = 0;

    films.forEach(film => {
        if (film.characters) {
            film.characters.forEach(characterUrl => {
                if (characterUrl.includes(`/${wedgeAntillesId}/`)) {
                    count++;
                }
            });
        }
    });

    console.log(count);
});
