#!/usr/bin/node
module.exports = {
  add: (a, b) => [a, b].reduce((c, v) => c + v, 0)
};
