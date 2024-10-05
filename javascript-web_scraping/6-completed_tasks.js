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

    const tasks = JSON.parse(body);
    const completedTasksCount = {};

    tasks.forEach(task => {
        if (task.completed) {
            if (!completedTasksCount[task.userId]) {
                completedTasksCount[task.userId] = 0;
            }
            completedTasksCount[task.userId]++;
        }
    });

    console.log(completedTasksCount);
});
