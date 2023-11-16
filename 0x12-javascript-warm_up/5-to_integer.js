#!/usr/bin/node
/*
if the first argument can be converted to an integer
Print **`My number`: `<first argument converted in integer>`**
 */
if (process.argv[2] && Number(process.argv[2])) {
  console.log('My number: ' + process.argv[2]);
} else {
  console.log('Not a number');
}
