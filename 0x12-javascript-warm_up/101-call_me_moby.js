#!/usr/bin/node
/* Execute theFunction() x times */
exports.callMeMoby = function see(x, theFunction) {
	for(let i = 0; i < x; i++)
    		theFunction();
}
