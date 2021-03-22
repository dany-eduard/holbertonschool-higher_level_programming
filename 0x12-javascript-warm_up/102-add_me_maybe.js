#!/usr/bin/nodejs

exports.addMeMaybe = (number, thefunction) => {
  number += 1;
  thefunction(number);
}
