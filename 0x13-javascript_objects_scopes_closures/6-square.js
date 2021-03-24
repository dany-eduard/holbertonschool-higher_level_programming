#!/usr/bin/node

const Square5 = require('./5-square.js');

module.exports = class Square extends Square5 {
  charPrint (c) {
    if (!c) {
      c = 'X';
    }
    for (let j = this.height; j; j--) {
      console.log(c.repeat(this.width));
    }
  }
};
