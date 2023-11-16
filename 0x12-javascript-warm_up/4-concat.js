#!/usr/bin/node
/* Print two arguments passed to the script, in the following format: <args2> “ is ” <args3>*/
const args2 = process.argv[2];
const args3 = process.argv[3];
console.log(args2 + ' is ' + args3);
