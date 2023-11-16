#!/usr/bin/node
/* Print x times “C is fun” Where x is the first argument of the script */
let i = 0;
if (isNaN(process.argv[2])) {
  console.log('Missing number of occurrences');
} else {
  while (i < process.argv[2]) {
    console.log('C is fun');
    i++;
  }
}
