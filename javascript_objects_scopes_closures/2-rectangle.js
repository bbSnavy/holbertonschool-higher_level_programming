#!/usr/bin/node
class Rectangle {
  constructor (w, h) {
    if (w === undefined || h === undefined) {
      return;
    }

    if (w <= 0 || h <= 0) {
      return;
    }

    this.width = w;
    this.height = h;
  }
}

module.exports = Rectangle;
