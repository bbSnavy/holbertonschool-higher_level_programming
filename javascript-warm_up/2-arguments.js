#!/usr/bin/node
if (process.args === undefined) {
  console.log('No argument');
} else if (process.args.length === 2) {
  console.log('Argument found');
} else {
  console.log('Arguments found');
}
