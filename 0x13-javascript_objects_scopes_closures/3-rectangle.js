#!/usr/bin/node

module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || isNaN(w) || isNaN(h)) return;
    this.width = w;
    this.height = h;
  }

  print () {
    for (let i = 0; i < this.height; i++) {
      let stringX = '';
      for (let j = 0; j < this.width; j++) {
        stringX += 'X';
      }
      console.log(stringX);
    }
  }
};
