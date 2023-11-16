#!/usr/bin/node
/* Create an empty class if width or height <= 0 */
module.exports = class Rectangle {
  constructor (w, h) {
    if (w > 0 || h > 0) {
      [this.width, this.height] = [w, h];
    }
  }
};
