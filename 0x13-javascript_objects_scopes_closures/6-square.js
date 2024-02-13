#!/usr/bin/node
const Square1 = require('./5-square');

class Square extends Square1 {
  charPrint (c = null) {
    let i, j;
    if (c === null) {
      c = 'X';
    }
    for (i = 0; i < this.height; i++) {
      for (j = 0; j < this.width; j++) { process.stdout.write(c); }
      console.log('');
    }
  }
}

module.exports = Square;
