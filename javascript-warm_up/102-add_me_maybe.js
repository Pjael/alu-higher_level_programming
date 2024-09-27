#!/usr/bin/node
let counter = 4;

exports.addMeMaybe = function (number, theFunction) {
  counter++;
  theFunction(counter);
};
