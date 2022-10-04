#!/usr/bin/node
const Square1 = require('./5-square.js');

module.exports = class Square extends Square1 {
  charPrint (c) {
    if (c !== undefined) {
      for (let i = 0; i < this.height; i++) {
        let stringX = '';
        for (let j = 0; j < this.width; j++) {
          stringX += c;
        }
        console.log(stringX);
      }
    } else {
      this.print();
    }
  }
};
