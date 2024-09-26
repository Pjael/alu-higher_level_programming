#!/usr/bin/node
const Rectangle = require('./4-rectangle.js');//import Rectangle class

class Square extends Rectangle {
	constructor(size) {
		super(size, size);//call the rectangle constructor with width and height as size
	}
}

module.exports = Square; //Export the Square class
