#!/usr/bin/node
/**
 * Create an empty class if width or height <= 0 
 * print an instance of therectangle using
 * character x
 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 && h > 0) {
      [this.width, this.height] = [w, h];
    }
  }
	print() {
	for (let i = 0; i < this.height; i++) {
		let row = '';
		for (let j = 0; j < this.width; j++) {
			row += 'X';
		}
		console.log(row);
	}
     }
};
