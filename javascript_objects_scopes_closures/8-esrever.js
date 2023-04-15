#!/usr/bin/node
exports.esrever = function (list) {
  return list.reduceRight((acc, element) => {
    return [...acc, element];
  }, []);
};
