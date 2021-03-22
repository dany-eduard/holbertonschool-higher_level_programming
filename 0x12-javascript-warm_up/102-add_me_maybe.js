#!/usr/bin/node

exports.addMeMaybe = function (number, thefunction) {
  number += 1;
  thefunction(number);
}
