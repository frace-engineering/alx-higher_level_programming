#!/usr/bin/node
/* Print a square using fisrt arg to script as size */
let i = 0;
const size = Number(process.argv[2]);
if (isNaN(size)) {
  console.log('Missing size');
} else {
  while (i < size) {
    let row = '';
    for (let c = 0; c < size; c++)  
	row += 'X';
    	console.log(row);
    i++;
  }
}
