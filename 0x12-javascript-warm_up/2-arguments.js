#!/usr/bin/node
/* Print a message depending of the number of arguments passed */
const arg = process.argv.length;
if (arg <= 2) {
  console.log('No argument');
} if (arg === 3) {
  console.log('Argument found');
} if (arg >= 4) {
  console.log('Arguments found');
}
// console.log(arg);
