#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  let numCount = 0;
  for (const num of list) {
    if (num === searchElement) {
      numCount += 1;
    }
  }
 return numCount;
};
