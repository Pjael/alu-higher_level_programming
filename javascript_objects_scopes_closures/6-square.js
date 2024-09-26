#!/usr/bin/node
const Rectangle = require('./5-square.js');//import Rectangle class

class Square extends Rectangle {
	charPrint(c) {
		const character = c || 'X';
		for (let i = 0; i < this.height; i++) {
			console.log(character.repeat(this.width));
		}
	}
}

module.exports = Square; //Export the Square class
