#!/usr/bin/node
/**
 * Square class that defines a square and inherits from
 * Rectangle of 4-rectangle.js
 */
const Rectangle = require('./4-rectangle');

/* Use class notation and extends */
class Square extends Rectangle {
  constructor (size) {
    super(size, size);
  }
}
module.exports = Square;
