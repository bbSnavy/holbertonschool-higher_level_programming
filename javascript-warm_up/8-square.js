#!/usr/bin/node
const arg = parseInt(process.argv[2]);
if (!arg) {
  console.log('Missing size');
} else {
  for (let x = 0; x < arg; x++) {
    console.log('X'.repeat(arg));
  }
}
