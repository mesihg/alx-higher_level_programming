#!/usr/bin/node
exports.esrever = function (list) {
  const list1 = [];
  for (let i = 0; i < list.length; i++) {
    list1.push(list[list.length - 1 - i]);
  }
  return list1;
};
