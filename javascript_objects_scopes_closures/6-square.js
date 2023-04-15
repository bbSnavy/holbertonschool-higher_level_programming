#!/usr/bin/node
const SquareOld = require('./5-square');

class Square extends SquareOld {
  constructor (size) {
    super(size, size);
  }

  charPrint (c) {
    let v;

    v = c;
    if (v === undefined) {
      v = 'X';
    }

    for (let i = 0; i < this.size; i++) {
      console.log(v.repeat(this.size));
    }
  }
}

module.exports = Square;
