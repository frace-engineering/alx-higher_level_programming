#!/usr/bin/node
/**
 * Class square that defines a square and inherits from Square
 * of 5-square.js
 */
const BaseSquare = require('./5-square.js');
/* Use class notation and extends */
class Square extends BaseSquare {
  charPrint (c) {
    if (c === undefined) {
      c = 'X';
    }

    for (let i = 0; i < this.height; i++) {
      console.log(c.repeat(this.width));
    }
  }
}
/* Make the class accessible from outside */
module.exports = Square;
