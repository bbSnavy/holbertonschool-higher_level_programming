#!/usr/bin/node
exports.nbOccurences = function (list, searchElement) {
  return list.reduce((acc, element) => {
    if (element === searchElement) {
      return acc + 1;
    }
    return acc;
  }, 0);
};
