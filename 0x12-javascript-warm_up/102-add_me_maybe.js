#!/usr/bin/node
/* Execute theFunction() and increment number */
exports.addMeMaybe = function (number, theFunction) {
    	theFunction(++number);
}
