#!/usr/bin/node
console.log(process.argv.slice(2)
  .map(it => parseInt(it))
  .reduce((result, value) => {
    if (result[0] === undefined || value > result[0]) {
      return [value, result[0]];
    }
    return result;
  }, [undefined, undefined])[1] || 0);
