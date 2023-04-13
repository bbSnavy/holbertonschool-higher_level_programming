#!/usr/bin/node
if (process.args === undefined) {
  console.log('No argument');
} else {
  console.log(process.args[1]);
}
