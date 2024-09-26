#!/usr/bin/node
class Rectangle {
        constructor(w, h) {
                if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) {
                        return {};
                }
                this.width = w;
                this.height = h;
        }
//instance method that prints the rectangle using X
	print() {
		for (let i = 0; i < this.height; i++) {
			console.log('X'.repeat(this.width));
		}
	}
//instance method that exchanges width and height
	rotate() {
		const temp = this.width;
		this.width = this.height;
		this.height = temp;
		}
//instance method that multiples width and height of th rectangle by two
	double() {
		this.width *= 2
		this.height *= 2
	}
}

module.exports = Rectangle;
