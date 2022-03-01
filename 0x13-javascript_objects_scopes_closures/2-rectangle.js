#!/usr/bin/node
module.exports = class Rectangle {
  constructor (w, h) {
    if (w <= 0 || h <= 0 || typeof (h) === 'undefined' || typeof (w) === 'undefined') {
      const newObject = {};
    } else {
      this.width = w;
      this.height = h;
    }
  }
};
