#!/usr/bin/node
// console.log(process.argv.slice(2)
//   .map(it => parseInt(it))
//   .reduce((result, value) => {
//     if (result[0] === undefined || value > result[0]) {
//       if (result[1] === undefined || result[0] >= result[1]) {
//         return [value, result[0]];
//       }
//       return [value, result[1]];
//     }
//     return result;
//   }, [undefined, undefined])[1] || 0);

console.log(
  process.argv.slice(2)
    .map(it => parseInt(it))
    .reduce((acc, val) => {
      const res = [...acc];

      if (res[0] === undefined || val > res[0]) {
        if (res[1] === undefined || res[0] > res[1]) {
          res[1] = res[0];
        }
        res[0] = val;
      } else if (res[1] === undefined || val > res[1]) {
        res[1] = val;
      }

      return res;
    }, [undefined, undefined])[1] || 0
);
