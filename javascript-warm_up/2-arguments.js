#!/usr/bin/node
if (process.args === undefined) {
  console.log('No argument');
} else if (process.args.length === 1) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
