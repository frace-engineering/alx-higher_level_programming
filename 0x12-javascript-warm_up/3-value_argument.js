#!/usr/bin/node
/* Print the first argument passed to the script */
const arg2 = process.argv[2];
if (arg2) {
  console.log(arg2);
} else {
  console.log('No argument');
}
